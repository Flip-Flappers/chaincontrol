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
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List

from fastapi import FastAPI
from pydantic import BaseModel, Field


class ControlRequest(BaseModel):
    command: str = Field(..., min_length=1, description="用户控制命令")
    context: Dict[str, Any] = Field(default_factory=dict, description="上下文信息")


class ControlResponse(BaseModel):
    ok: bool
    answer: str
    keywords: List[Dict[str, Any]] = Field(default_factory=list)
    target_tools: List[Dict[str, Any]] = Field(default_factory=list)
    raw: Dict[str, Any] = Field(default_factory=dict)


app = FastAPI(title="ChainControl Backend Service", version="0.1.0")


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
    greet = _resolve_swagger_greet()

    if greet is None:
        return {
            "ok": True,
            "answer": f"已收到命令：{command}（当前使用兜底流程，未接入 Swagger pipeline）",
            "keywords": [],
            "target_tools": [],
            "raw": {"mode": "fallback"},
        }

    try:
        keywords, target_tools = greet(command)
        return {
            "ok": True,
            "answer": "命令已解析并执行，请查看 raw 字段获取详细结果。",
            "keywords": keywords or [],
            "target_tools": target_tools or [],
            "raw": {
                "mode": "swagger_pipeline",
                "keywords_count": len(keywords or []),
                "target_tools_count": len(target_tools or []),
            },
        }
    except Exception as exc:  # noqa: BLE001
        return {
            "ok": False,
            "answer": f"命令执行失败：{exc}",
            "keywords": [],
            "target_tools": [],
            "raw": {"mode": "error", "error": str(exc)},
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
    result = _run_control_pipeline(request.command)
    return ControlResponse(**result)
