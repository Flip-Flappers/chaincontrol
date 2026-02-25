"""桌面端物联网小助手（Tkinter 版）

功能：
1. 本地桌面聊天式交互
2. 可配置后端服务地址（默认 http://127.0.0.1:8000）
3. 发送控制命令到后端 /control
4. 健康检查 /health

后端接口约定：
- POST /control
  request: {"command": "打开客厅灯", "context": {}}
  response: {"ok": true, "answer": "已为你打开客厅灯", "raw": {...}}
- GET /health
  response: {"status": "ok"}
"""

from __future__ import annotations

import json
import threading
import tkinter as tk
from tkinter import messagebox, scrolledtext
from dataclasses import dataclass, field
from typing import Any, Dict

import requests


@dataclass
class AssistantConfig:
    base_url: str = "http://127.0.0.1:8000"
    timeout_seconds: int = 20
    default_context: Dict[str, Any] = field(default_factory=dict)


class IoTAssistantClient:
    def __init__(self, config: AssistantConfig):
        self.config = config

    def health(self) -> Dict[str, Any]:
        url = f"{self.config.base_url.rstrip('/')}/health"
        response = requests.get(url, timeout=self.config.timeout_seconds)
        response.raise_for_status()
        return response.json()

    def control(self, command: str) -> Dict[str, Any]:
        url = f"{self.config.base_url.rstrip('/')}/control"
        payload = {
            "command": command,
            "context": self.config.default_context,
        }
        response = requests.post(url, json=payload, timeout=self.config.timeout_seconds)
        response.raise_for_status()
        return response.json()


class DesktopAssistantApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("ChainControl 桌面小助手")
        self.root.geometry("880x620")

        self.config = AssistantConfig()
        self.client = IoTAssistantClient(self.config)

        self._build_ui()

    def _build_ui(self) -> None:
        top_frame = tk.Frame(self.root)
        top_frame.pack(fill=tk.X, padx=10, pady=8)

        tk.Label(top_frame, text="服务地址:").pack(side=tk.LEFT)
        self.base_url_entry = tk.Entry(top_frame, width=50)
        self.base_url_entry.insert(0, self.config.base_url)
        self.base_url_entry.pack(side=tk.LEFT, padx=6)

        tk.Button(top_frame, text="健康检查", command=self.on_health_check).pack(side=tk.LEFT, padx=6)
        tk.Button(top_frame, text="更新地址", command=self.on_update_url).pack(side=tk.LEFT)

        self.chat_area = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, state=tk.DISABLED)
        self.chat_area.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 10))

        bottom_frame = tk.Frame(self.root)
        bottom_frame.pack(fill=tk.X, padx=10, pady=(0, 10))

        tk.Label(bottom_frame, text="请输入控制命令:").pack(anchor="w")
        self.command_input = tk.Text(bottom_frame, height=4)
        self.command_input.pack(fill=tk.X, pady=6)

        action_frame = tk.Frame(bottom_frame)
        action_frame.pack(fill=tk.X)
        tk.Button(action_frame, text="发送命令", command=self.on_send).pack(side=tk.LEFT)
        tk.Button(action_frame, text="清空会话", command=self.on_clear).pack(side=tk.LEFT, padx=6)

        self._append("系统", "欢迎使用桌面小助手。先点“健康检查”，再发送设备控制命令。")

    def _append(self, role: str, content: str) -> None:
        self.chat_area.configure(state=tk.NORMAL)
        self.chat_area.insert(tk.END, f"[{role}] {content}\n\n")
        self.chat_area.see(tk.END)
        self.chat_area.configure(state=tk.DISABLED)

    def on_update_url(self) -> None:
        base_url = self.base_url_entry.get().strip()
        if not base_url:
            messagebox.showwarning("提示", "服务地址不能为空")
            return
        self.config.base_url = base_url
        self.client = IoTAssistantClient(self.config)
        self._append("系统", f"服务地址已更新为：{base_url}")

    def on_health_check(self) -> None:
        def worker() -> None:
            try:
                self.on_update_url()
                result = self.client.health()
                self._append("助手", f"健康检查通过：{json.dumps(result, ensure_ascii=False)}")
            except Exception as exc:  # noqa: BLE001
                self._append("助手", f"健康检查失败：{exc}")

        threading.Thread(target=worker, daemon=True).start()

    def on_send(self) -> None:
        command = self.command_input.get("1.0", tk.END).strip()
        if not command:
            messagebox.showwarning("提示", "请输入命令")
            return

        self._append("你", command)
        self.command_input.delete("1.0", tk.END)

        def worker() -> None:
            try:
                self.on_update_url()
                result = self.client.control(command)
                answer = result.get("answer") or result.get("message") or json.dumps(result, ensure_ascii=False)
                self._append("助手", answer)
            except Exception as exc:  # noqa: BLE001
                self._append("助手", f"调用失败：{exc}")

        threading.Thread(target=worker, daemon=True).start()

    def on_clear(self) -> None:
        self.chat_area.configure(state=tk.NORMAL)
        self.chat_area.delete("1.0", tk.END)
        self.chat_area.configure(state=tk.DISABLED)
        self._append("系统", "会话已清空")


def main() -> None:
    root = tk.Tk()
    DesktopAssistantApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
