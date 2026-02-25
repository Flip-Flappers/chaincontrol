"""ChainControl 后端服务（适配 Tkinter 客户端）

提供接口：
- GET /health
- POST /control

默认启动：
    uvicorn backend_service:app --host 0.0.0.0 --port 8000
"""

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


def _resolve_swagger_greet():
    """动态加载 LangChain/Swagger/start.py 中的 greet 方法。"""
    base_dir = Path(__file__).resolve().parent
    swagger_dir = base_dir / "LangChain" / "Swagger"
    if not swagger_dir.exists():
        return None

    sys.path.insert(0, str(swagger_dir))
    try:
        from start import greet  # type: ignore

        return greet
    except Exception:
        return None


def _run_control_pipeline(command: str) -> Dict[str, Any]:
    """执行控制流水线。

    优先复用现有 Swagger 流程（start.greet）。
    若加载失败，返回兜底响应，保证桌面客户端可用。
    """
    step_trace: List[Dict[str, Any]] = []

    def add_step(name: str, detail: str, status: str, started_at: float) -> None:
        step_trace.append(
            {
                "name": name,
                "detail": detail,
                "status": status,
                "duration_ms": int((time.perf_counter() - started_at) * 1000),
            }
        )

    t0 = time.perf_counter()
    greet = _resolve_swagger_greet()
    if greet is None:
        add_step("加载执行器", "未找到 Swagger pipeline，切换为 fallback", "completed", t0)
        return {
            "ok": True,
            "answer": f"已收到命令：{command}（当前使用兜底流程，未接入 Swagger pipeline）",
            "keywords": [],
            "target_tools": [],
            "raw": {"mode": "fallback", "steps": step_trace},
        }

    add_step("加载执行器", "已加载 Swagger pipeline", "completed", t0)

    t1 = time.perf_counter()
    try:
        keywords, target_tools = greet(command)
    except Exception as exc:  # noqa: BLE001
        add_step("执行命令解析", f"执行失败：{exc}", "failed", t1)
        return {
            "ok": False,
            "answer": f"命令执行失败：{exc}",
            "keywords": [],
            "target_tools": [],
            "raw": {"mode": "error", "error": str(exc), "steps": step_trace},
        }

    add_step("执行命令解析", "命令解析与工具选择完成", "completed", t1)

    t2 = time.perf_counter()
    normalized_keywords = keywords or []
    normalized_target_tools = target_tools or []
    add_step(
        "结果整理",
        f"keywords={len(normalized_keywords)}, target_tools={len(normalized_target_tools)}",
        "completed",
        t2,
    )

    return {
        "ok": True,
        "answer": "命令已解析并执行，请查看步骤详情。",
        "keywords": normalized_keywords,
        "target_tools": normalized_target_tools,
        "raw": {
            "mode": "swagger_pipeline",
            "keywords_count": len(normalized_keywords),
            "target_tools_count": len(normalized_target_tools),
            "steps": step_trace,
        },
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
