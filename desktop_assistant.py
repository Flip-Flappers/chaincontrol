"""桌面端物联网小助手（Tkinter 版，Discord 风格）。"""

from __future__ import annotations

import json
import threading
import tkinter as tk
from dataclasses import dataclass, field
from tkinter import messagebox, scrolledtext, ttk
from typing import Any, Dict, Iterable

import requests


@dataclass
class AssistantConfig:
    base_url: str = "http://127.0.0.1:8000"
    timeout_seconds: int = 20
    default_user_id: str = "user-001"
    default_context: Dict[str, Any] = field(default_factory=dict)


class IoTAssistantClient:
    def __init__(self, config: AssistantConfig):
        self.config = config

    def health(self) -> Dict[str, Any]:
        url = f"{self.config.base_url.rstrip('/')}/health"
        response = requests.get(url, timeout=self.config.timeout_seconds)
        response.raise_for_status()
        return response.json()

    def control(self, command: str, user_id: str) -> Dict[str, Any]:
        url = f"{self.config.base_url.rstrip('/')}/control"
        payload = {
            "command": command,
            "user_id": user_id,
            "context": self.config.default_context,
        }
        response = requests.post(url, json=payload, timeout=self.config.timeout_seconds)
        response.raise_for_status()
        return response.json()


class DesktopAssistantApp:
    BG = "#313338"
    PANEL = "#2B2D31"
    INPUT = "#1E1F22"
    FG = "#DBDEE1"
    MUTED = "#949BA4"
    BRAND = "#5865F2"

    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("ChainControl - Assistant")
        self.root.geometry("980x700")
        self.root.configure(bg=self.BG)

        self.config = AssistantConfig()
        self.client = IoTAssistantClient(self.config)
        self.sending = False
        self._typing_tick = 0

        self._build_ui()

    def _build_ui(self) -> None:
        self._build_styles()

        container = tk.Frame(self.root, bg=self.BG)
        container.pack(fill=tk.BOTH, expand=True)

        header = tk.Frame(container, bg=self.PANEL, height=64)
        header.pack(fill=tk.X, padx=12, pady=(12, 8))
        header.pack_propagate(False)

        tk.Label(
            header,
            text="# chaincontrol-assistant",
            bg=self.PANEL,
            fg=self.FG,
            font=("Segoe UI", 13, "bold"),
        ).pack(side=tk.LEFT, padx=14)

        self.status_label = tk.Label(
            header,
            text="● idle",
            bg=self.PANEL,
            fg=self.MUTED,
            font=("Segoe UI", 10),
        )
        self.status_label.pack(side=tk.RIGHT, padx=14)

        top = tk.Frame(container, bg=self.BG)
        top.pack(fill=tk.X, padx=12, pady=(0, 8))

        tk.Label(top, text="服务地址", bg=self.BG, fg=self.MUTED).pack(side=tk.LEFT)
        self.base_url_entry = tk.Entry(top, width=35, bg=self.INPUT, fg=self.FG, insertbackground=self.FG, relief=tk.FLAT)
        self.base_url_entry.insert(0, self.config.base_url)
        self.base_url_entry.pack(side=tk.LEFT, padx=8)

        tk.Label(top, text="用户ID", bg=self.BG, fg=self.MUTED).pack(side=tk.LEFT, padx=(8, 0))
        self.user_id_entry = tk.Entry(top, width=16, bg=self.INPUT, fg=self.FG, insertbackground=self.FG, relief=tk.FLAT)
        self.user_id_entry.insert(0, self.config.default_user_id)
        self.user_id_entry.pack(side=tk.LEFT, padx=8)

        ttk.Button(top, text="健康检查", command=self.on_health_check, style="Accent.TButton").pack(side=tk.LEFT, padx=4)
        ttk.Button(top, text="更新地址", command=self.on_update_url, style="Soft.TButton").pack(side=tk.LEFT, padx=4)

        chat_panel = tk.Frame(container, bg=self.PANEL)
        chat_panel.pack(fill=tk.BOTH, expand=True, padx=12, pady=(0, 8))

        self.chat_area = scrolledtext.ScrolledText(
            chat_panel,
            wrap=tk.WORD,
            state=tk.DISABLED,
            bg=self.PANEL,
            fg=self.FG,
            relief=tk.FLAT,
            insertbackground=self.FG,
            font=("Segoe UI", 10),
            padx=12,
            pady=12,
        )
        self.chat_area.pack(fill=tk.BOTH, expand=True)

        self.chat_area.tag_configure("你", foreground="#FFFFFF", font=("Segoe UI", 10, "bold"))
        self.chat_area.tag_configure("助手", foreground="#A6D189", font=("Segoe UI", 10, "bold"))
        self.chat_area.tag_configure("步骤", foreground="#9CDCFE", font=("Segoe UI", 10, "bold"))
        self.chat_area.tag_configure("Prompt", foreground="#F6BD60")
        self.chat_area.tag_configure("AI思考", foreground="#CBA6F7")
        self.chat_area.tag_configure("AI返回", foreground="#89DCEB")
        self.chat_area.tag_configure("系统", foreground=self.MUTED)

        footer = tk.Frame(container, bg=self.BG)
        footer.pack(fill=tk.X, padx=12, pady=(0, 12))

        self.command_input = tk.Text(
            footer,
            height=4,
            bg=self.INPUT,
            fg=self.FG,
            insertbackground=self.FG,
            relief=tk.FLAT,
            font=("Segoe UI", 10),
        )
        self.command_input.pack(fill=tk.X)

        action = tk.Frame(footer, bg=self.BG)
        action.pack(fill=tk.X, pady=(8, 0))

        self.progress = ttk.Progressbar(action, mode="indeterminate", length=180)
        self.progress.pack(side=tk.LEFT)

        self.send_button = ttk.Button(action, text="发送命令", command=self.on_send, style="Accent.TButton")
        self.send_button.pack(side=tk.RIGHT, padx=(6, 0))
        ttk.Button(action, text="清空会话", command=self.on_clear, style="Soft.TButton").pack(side=tk.RIGHT)

        self._append("系统", "欢迎使用桌面小助手。现在界面为 Discord 风格深色主题，发送时会显示动态状态。")

    def _build_styles(self) -> None:
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Accent.TButton", background=self.BRAND, foreground="#FFFFFF", borderwidth=0, padding=(12, 6))
        style.map("Accent.TButton", background=[("active", "#4752C4"), ("disabled", "#4E56A6")])
        style.configure("Soft.TButton", background=self.PANEL, foreground=self.FG, borderwidth=0, padding=(12, 6))
        style.map("Soft.TButton", background=[("active", "#3B3D45")])

    def _append(self, role: str, content: str) -> None:
        self.chat_area.configure(state=tk.NORMAL)
        prefix = f"{role}: "
        self.chat_area.insert(tk.END, prefix, role)
        self.chat_area.insert(tk.END, f"{content}\n\n")
        self.chat_area.see(tk.END)
        self.chat_area.configure(state=tk.DISABLED)

    def _append_async(self, role: str, content: str) -> None:
        self.root.after(0, lambda: self._append(role, content))

    def _set_status(self, text: str, active: bool) -> None:
        self.status_label.configure(text=text, fg=("#3BA55D" if active else self.MUTED))

    def _animate_typing(self) -> None:
        if not self.sending:
            self._set_status("● idle", active=False)
            return
        dots = "." * ((self._typing_tick % 3) + 1)
        self._set_status(f"● processing{dots}", active=True)
        self._typing_tick += 1
        self.root.after(420, self._animate_typing)

    def _set_sending(self, sending: bool) -> None:
        self.sending = sending
        new_state = tk.DISABLED if sending else tk.NORMAL
        self.send_button.configure(state=new_state)
        self.command_input.configure(state=new_state)
        if sending:
            self.progress.start(10)
            self._typing_tick = 0
            self._animate_typing()
        else:
            self.progress.stop()
            self._set_status("● idle", active=False)

    def _set_sending_async(self, sending: bool) -> None:
        self.root.after(0, lambda: self._set_sending(sending))

    def _render_steps(self, user_id: str, steps: Iterable[Dict[str, Any]]) -> None:
        for index, step in enumerate(steps, start=1):
            name = step.get("name", f"步骤{index}")
            detail = step.get("detail", "")
            status = step.get("status", "unknown")
            duration_ms = step.get("duration_ms")
            prompt = step.get("prompt", "")
            ai_response = step.get("ai_response", "")
            ai_think = step.get("ai_think", "")
            cost = f"，耗时 {duration_ms}ms" if duration_ms is not None else ""
            self._append_async("步骤", f"({user_id}) {index}. {name} [{status}] - {detail}{cost}")
            if prompt:
                self._append_async("Prompt", f"({user_id}) {prompt}")
            if ai_think:
                self._append_async("AI思考", f"({user_id}) {ai_think}")
            if ai_response:
                self._append_async("AI返回", f"({user_id}) {ai_response}")

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
                self.root.after(0, self.on_update_url)
                result = self.client.health()
                self._append_async("助手", f"健康检查通过：{json.dumps(result, ensure_ascii=False)}")
            except Exception as exc:  # noqa: BLE001
                self._append_async("助手", f"健康检查失败：{exc}")

        threading.Thread(target=worker, daemon=True).start()

    def on_send(self) -> None:
        if self.sending:
            messagebox.showinfo("提示", "当前用户命令正在处理中，请稍后再发")
            return

        user_id = self.user_id_entry.get().strip() or self.config.default_user_id
        command = self.command_input.get("1.0", tk.END).strip()
        if not command:
            messagebox.showwarning("提示", "请输入命令")
            return

        self._append("你", f"({user_id}) {command}")
        self.command_input.delete("1.0", tk.END)
        self._set_sending(True)

        def worker() -> None:
            try:
                self._append_async("步骤", f"({user_id}) 1/4 收到命令，准备请求后端")
                self.root.after(0, self.on_update_url)
                self._append_async("步骤", f"({user_id}) 2/4 正在调用 /control")
                result = self.client.control(command, user_id)
                self._append_async("步骤", f"({user_id}) 3/4 后端返回，正在整理步骤详情")

                raw = result.get("raw") if isinstance(result, dict) else {}
                steps = raw.get("steps", []) if isinstance(raw, dict) else []
                if steps:
                    self._render_steps(user_id, steps)

                answer = result.get("answer") or result.get("message") or json.dumps(result, ensure_ascii=False)
                self._append_async("步骤", f"({user_id}) 4/4 展示最终结果")
                self._append_async("助手", f"({user_id}) {answer}")
            except requests.HTTPError as exc:
                if exc.response is not None and exc.response.status_code == 409:
                    self._append_async("助手", f"({user_id}) 命令被拒绝：该用户已有命令在处理中")
                else:
                    self._append_async("助手", f"调用失败：{exc}")
            except Exception as exc:  # noqa: BLE001
                self._append_async("助手", f"调用失败：{exc}")
            finally:
                self._set_sending_async(False)

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
