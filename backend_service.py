"""ChainControl 后端服务（适配 Tkinter 客户端）。"""

from __future__ import annotations

import os
import sys
import threading
import time
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field


class ControlRequest(BaseModel):
    command: str = Field(..., min_length=1, description="用户控制命令")
    user_id: str | None = Field(default=None, description="用户标识；为空时尝试从 context.user_id 读取")
    context: Dict[str, Any] = Field(default_factory=dict, description="上下文信息")

    def resolved_user_id(self) -> str:
        context_user_id = self.context.get("user_id") if isinstance(self.context, dict) else None
        user_id = self.user_id or context_user_id or "default-user"
        return str(user_id).strip() or "default-user"


class ControlResponse(BaseModel):
    ok: bool
    user_id: str
    answer: str
    keywords: List[Dict[str, Any]] = Field(default_factory=list)
    target_tools: List[Dict[str, Any]] = Field(default_factory=list)
    raw: Dict[str, Any] = Field(default_factory=dict)


app = FastAPI(title="ChainControl Backend Service", version="0.1.0")

_inflight_users: set[str] = set()
_inflight_users_lock = threading.Lock()


def _acquire_user_slot(user_id: str) -> bool:
    with _inflight_users_lock:
        if user_id in _inflight_users:
            return False
        _inflight_users.add(user_id)
        return True


def _release_user_slot(user_id: str) -> None:
    with _inflight_users_lock:
        _inflight_users.discard(user_id)


def _safe_text(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, str):
        return value
    return str(value)


def _resolve_swagger_components() -> Dict[str, Any] | None:
    base_dir = Path(__file__).resolve().parent
    swagger_dir = base_dir / "LangChain" / "Swagger"
    if not swagger_dir.exists():
        return None

    sys.path.insert(0, str(swagger_dir))
    try:
        from start import DeviceTool, ToolSelector, greet, keywordSelector  # type: ignore

        return {
            "greet": greet,
            "keyword_selector": keywordSelector,
            "tool_selector_cls": getattr(ToolSelector, "ToolSelector", None),
            "device_tool_cls": getattr(DeviceTool, "DeviceTool", None),
        }
    except Exception:
        return None


def _run_swagger_step_pipeline(command: str, components: Dict[str, Any], step_trace: List[Dict[str, Any]]) -> Dict[str, Any]:
    """按显式步骤执行：抽槽 -> 工具选择 -> 设备控制意图识别。"""

    def add_step(
        name: str,
        detail: str,
        status: str,
        started_at: float,
        *,
        prompt: str = "",
        ai_response: str = "",
        ai_think: str = "",
    ) -> None:
        step_trace.append(
            {
                "name": name,
                "detail": detail,
                "status": status,
                "duration_ms": int((time.perf_counter() - started_at) * 1000),
                "prompt": prompt,
                "ai_response": ai_response,
                "ai_think": ai_think,
            }
        )

    keyword_selector = components.get("keyword_selector")
    tool_selector_cls = components.get("tool_selector_cls")
    device_tool_cls = components.get("device_tool_cls")

    if keyword_selector is None or tool_selector_cls is None:
        raise RuntimeError("Swagger 组件不完整，缺少 keywordSelector/ToolSelector")

    keywords: List[Dict[str, Any]] = []
    all_target_tools: List[Dict[str, Any]] = []
    all_device_actions: List[Dict[str, Any]] = []

    t_extract = time.perf_counter()
    extract_prompt = f"command={command}"
    extract_think, extract_answer, raw_keywords = keyword_selector.select_keywords(command)
    keywords = raw_keywords or []
    add_step(
        "步骤1: keywordSelector.select_keywords(command)",
        f"识别到 {len(keywords)} 个关键词槽位",
        "completed",
        t_extract,
        prompt=extract_prompt,
        ai_response=_safe_text(extract_answer),
        ai_think=_safe_text(extract_think),
    )

    if not keywords:
        add_step("执行结束", "未识别到可执行关键词，跳过设备控制", "completed", time.perf_counter())
        return {
            "ok": True,
            "answer": "未识别到可执行的设备意图。",
            "keywords": [],
            "target_tools": [],
            "raw": {
                "mode": "swagger_step_pipeline",
                "steps": step_trace,
                "device_actions": [],
            },
        }

    for index, keyword in enumerate(keywords, start=1):
        key_word_value = _safe_text(keyword.get("KeyWord"))
        key_word_name = _safe_text(keyword.get("keyWordName"))
        if key_word_name != "deviceName":
            continue

        action = _safe_text(keyword.get("action"))

        if key_word_value == "null":
            add_step(
                f"关键词#{index}",
                f"device={key_word_value or 'unknown'} 命中空槽位，跳过",
                "skipped",
                time.perf_counter(),
            )
            continue

        keyword_map = {"deviceName": key_word_value, "KeyWord": key_word_value}
        t_tool = time.perf_counter()
        selector = tool_selector_cls(keyword_map)
        tool_prompt = f"for device：{keyword_map['deviceName']}, the action is{action}"
        tool_think, tool_answer, target_tools = selector.select_tool(tool_prompt)
        selected_tools = target_tools or []
        all_target_tools.extend(selected_tools)
        add_step(
            f"步骤2: toolSelector.select_tool(...) [关键词#{index}]",
            f"device={keyword_map['deviceName']}, action={action}, tools={len(selected_tools)}",
            "completed",
            t_tool,
            prompt=tool_prompt,
            ai_response=_safe_text(tool_answer),
            ai_think=_safe_text(tool_think),
        )



        for tool_idx, tool in enumerate(selected_tools, start=1):
            tool_name = _safe_text(tool.get("toolName")) or "unknown"
            if tool_name != "DeviceTool":
                add_step(
                    f"关键词#{index} 工具#{tool_idx}",
                    f"tool={tool_name} 当前未执行，仅记录",
                    "skipped",
                    time.perf_counter(),
                )
                continue

            if device_tool_cls is None:
                add_step(
                    f"关键词#{index} 工具#{tool_idx}",
                    "DeviceTool 类缺失，无法执行设备意图识别",
                    "failed",
                    time.perf_counter(),
                )
                continue

            instructions = _safe_text(tool.get("instructions"))
            t_device = time.perf_counter()
            device_tool = device_tool_cls(keyword_map, keyword_map["deviceName"])
            device_think, device_answer, target_device_tool = device_tool.intention_recognition(instructions)
            device_targets = target_device_tool if isinstance(target_device_tool, list) else [target_device_tool]
            valid_targets = [item for item in device_targets if item]
            all_device_actions.extend(valid_targets)
            add_step(
                f"步骤3: deviceTool.intention_recognition(...) [关键词#{index}]",
                f"tool=DeviceTool, 执行结果条目={len(valid_targets)}",
                "completed",
                t_device,
                prompt=instructions,
                ai_response=_safe_text(device_answer),
                ai_think=_safe_text(device_think),
            )

    return {
        "ok": True,
        "answer": "命令处理完成，已按步骤执行抽槽与设备控制。",
        "keywords": keywords,
        "target_tools": all_target_tools,
        "raw": {
            "mode": "swagger_step_pipeline",
            "keywords_count": len(keywords),
            "target_tools_count": len(all_target_tools),
            "device_actions_count": len(all_device_actions),
            "device_actions": all_device_actions,
            "steps": step_trace,
        },
    }


def _run_control_pipeline(command: str) -> Dict[str, Any]:
    step_trace: List[Dict[str, Any]] = []

    def add_step(name: str, detail: str, status: str, started_at: float) -> None:
        step_trace.append(
            {
                "name": name,
                "detail": detail,
                "status": status,
                "duration_ms": int((time.perf_counter() - started_at) * 1000),
                "prompt": "",
                "ai_response": "",
                "ai_think": "",
            }
        )

    t_load = time.perf_counter()
    components = _resolve_swagger_components()
    if components is None:
        add_step("加载执行器", "未找到 Swagger pipeline，切换为 fallback", "completed", t_load)
        return {
            "ok": True,
            "answer": f"已收到命令：{command}（当前使用兜底流程，未接入 Swagger pipeline）",
            "keywords": [],
            "target_tools": [],
            "raw": {"mode": "fallback", "steps": step_trace},
        }

    add_step("加载执行器", "已加载 Swagger pipeline 组件", "completed", t_load)

    try:
        return _run_swagger_step_pipeline(command, components, step_trace)
    except Exception as exc:  # noqa: BLE001
        add_step("执行异常", f"流水线失败：{exc}", "failed", time.perf_counter())

        greet = components.get("greet")
        if callable(greet):
            t_fallback = time.perf_counter()
            try:
                keywords, target_tools = greet(command)
                add_step("兼容回退（start.greet）", "已使用原始 greet 成功返回结果", "completed", t_fallback)
                return {
                    "ok": True,
                    "answer": "步骤化执行失败，已回退到原始流程。",
                    "keywords": keywords or [],
                    "target_tools": target_tools or [],
                    "raw": {
                        "mode": "swagger_greet_fallback",
                        "error": str(exc),
                        "steps": step_trace,
                    },
                }
            except Exception as greet_exc:  # noqa: BLE001
                add_step("兼容回退（start.greet）", f"回退也失败：{greet_exc}", "failed", t_fallback)

        return {
            "ok": False,
            "answer": f"命令执行失败：{exc}",
            "keywords": [],
            "target_tools": [],
            "raw": {"mode": "error", "error": str(exc), "steps": step_trace},
        }


@app.get("/health")
def health() -> Dict[str, Any]:
    return {
        "status": "ok",
        "service": "chaincontrol-backend",
        "time": datetime.utcnow().isoformat() + "Z",
        "pid": os.getpid(),
    }


@app.post("/control", response_model=ControlResponse)
def control(request: ControlRequest) -> ControlResponse:
    user_id = request.resolved_user_id()
    if not _acquire_user_slot(user_id):
        raise HTTPException(status_code=409, detail=f"用户 {user_id} 有命令正在处理中，请稍后重试")

    try:
        result = _run_control_pipeline(request.command)
        result["user_id"] = user_id
        return ControlResponse(**result)
    finally:
        _release_user_slot(user_id)
