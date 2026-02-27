"""
单入口启动脚本：同时启动后端服务与 PyQt6 桌面助手。
"""

from __future__ import annotations

import argparse
import subprocess
import sys
import time
from typing import Optional

import requests


# 🔥 改成你的 PyQt 主程序文件名
from desktop_assistant import main as run_desktop_app


def _wait_for_backend(base_url: str, timeout_seconds: int = 20) -> bool:
    health_url = f"{base_url.rstrip('/')}/health"
    deadline = time.time() + timeout_seconds

    while time.time() < deadline:
        try:
            response = requests.get(health_url, timeout=1.5)
            if response.ok:
                return True
        except Exception:
            pass
        time.sleep(0.4)

    return False


def _start_backend(host: str, port: int) -> subprocess.Popen:
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


def _stop_backend(proc: Optional[subprocess.Popen]) -> None:
    if not proc:
        return

    if proc.poll() is None:
        proc.terminate()
        try:
            proc.wait(timeout=5)
        except subprocess.TimeoutExpired:
            proc.kill()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="同时启动 ChainControl 后端和 PyQt6 客户端"
    )
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8000)
    parser.add_argument("--wait-timeout", type=int, default=20)

    return parser.parse_args()


def main() -> None:
    args = parse_args()
    base_url = f"http://{args.host}:{args.port}"

    backend_proc: Optional[subprocess.Popen] = None

    try:
        print("🔍 检查后端是否已运行...")

        # 👇 先检测是否已启动
        if _wait_for_backend(base_url, timeout_seconds=2):
            print("✅ 检测到后端已运行，跳过启动")
        else:
            print("🚀 启动后端服务...")
            backend_proc = _start_backend(args.host, args.port)

            print("⏳ 等待后端健康检查...")
            ready = _wait_for_backend(base_url, args.wait_timeout)

            if not ready:
                raise RuntimeError(f"后端启动超时：{base_url}")

        print("🖥 启动桌面端...")
        run_desktop_app()

    finally:
        # 👇 只关闭我们自己启动的后端
        if backend_proc:
            print("🛑 关闭后端服务...")
            _stop_backend(backend_proc)


if __name__ == "__main__":
    main()