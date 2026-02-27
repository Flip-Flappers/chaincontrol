"""单入口启动脚本：同时启动后端服务与桌面端助手。"""

from __future__ import annotations

import argparse
import subprocess
import sys
import time
from typing import Optional

import requests

from desktop_assistant import main as run_desktop_app


def _wait_for_backend(base_url: str, timeout_seconds: int = 20) -> bool:
    health_url = f"{base_url.rstrip('/')}/health"
    deadline = time.time() + timeout_seconds
    while time.time() < deadline:
        try:
            response = requests.get(health_url, timeout=1.5)
            if response.ok:
                return True
        except Exception:  # noqa: BLE001
            pass
        time.sleep(0.4)
    return False


def _start_backend(host: str, port: int) -> subprocess.Popen[str]:
    cmd = [
        sys.executable,
        "-m",
        "uvicorn",
        "backend_service:app",
        "--host",
        host,
        "--port",
        str(port),
    ]
    return subprocess.Popen(cmd)


def _stop_backend(proc: Optional[subprocess.Popen[str]]) -> None:
    if proc is None:
        return
    if proc.poll() is not None:
        return

    proc.terminate()
    try:
        proc.wait(timeout=5)
    except subprocess.TimeoutExpired:
        proc.kill()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="同时启动 ChainControl 后端和 Tkinter 客户端")
    parser.add_argument("--host", default="127.0.0.1", help="后端监听 host，默认 127.0.0.1")
    parser.add_argument("--port", type=int, default=8000, help="后端监听 port，默认 8000")
    parser.add_argument(
        "--wait-timeout",
        type=int,
        default=20,
        help="等待后端健康检查通过的最大秒数，默认 20",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    base_url = f"http://{args.host}:{args.port}"

    backend_proc: Optional[subprocess.Popen[str]] = None
    try:
        backend_proc = _start_backend(args.host, args.port)
        ready = _wait_for_backend(base_url, timeout_seconds=args.wait_timeout)
        if not ready:
            raise RuntimeError(f"后端启动超时：{base_url}")

        run_desktop_app()
    finally:
        _stop_backend(backend_proc)


if __name__ == "__main__":
    main()
