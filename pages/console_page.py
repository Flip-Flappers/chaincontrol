from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout,
    QFrame, QTextEdit, QPushButton,
    QScrollArea, QApplication
)
from PyQt6.QtCore import Qt

from core.assistant_worker import AssistantWorker
from ui.components.message_item import MessageItem


class ConsolePage(QWidget):
    def __init__(self):
        super().__init__()

        self.base_url = "http://127.0.0.1:8000"
        self.worker = None

        self.init_ui()

    # =========================
    # UI 初始化
    # =========================
    def init_ui(self):
        layout = QVBoxLayout(self)
        layout.setSpacing(20)
        layout.setContentsMargins(0, 0, 0, 0)

        # ===== 消息区 =====
        message_card = QFrame()
        message_card.setObjectName("GlassCard")

        message_layout = QVBoxLayout(message_card)
        message_layout.setContentsMargins(20, 20, 20, 20)

        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.scroll.setStyleSheet("border: none;")

        self.chat_container = QWidget()
        self.chat_layout = QVBoxLayout(self.chat_container)
        self.chat_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.chat_layout.setSpacing(6)

        self.scroll.setWidget(self.chat_container)
        message_layout.addWidget(self.scroll)

        layout.addWidget(message_card, 1)

        # ===== 输入区 =====
        input_card = QFrame()
        input_card.setObjectName("GlassCard")

        input_layout = QHBoxLayout(input_card)
        input_layout.setContentsMargins(15, 15, 15, 15)

        self.input_box = QTextEdit()
        self.input_box.setFixedHeight(60)

        send_btn = QPushButton("发送")
        send_btn.clicked.connect(self.send_message)

        input_layout.addWidget(self.input_box)
        input_layout.addWidget(send_btn)

        layout.addWidget(input_card)

        self.add_message("系统已连接到 127.0.0.1:8000", False)

    # =========================
    # 添加消息
    # =========================
    def add_message(self, text: str, is_user: bool):
        self.chat_layout.addWidget(MessageItem(text, is_user))

        QApplication.processEvents()
        self.scroll.verticalScrollBar().setValue(
            self.scroll.verticalScrollBar().maximum()
        )

    # =========================
    # 发送消息
    # =========================
    def send_message(self):
        text = self.input_box.toPlainText().strip()
        if not text:
            return

        # 显示用户消息
        self.add_message(text, True)
        self.input_box.clear()

        # 后台线程请求
        self.worker = AssistantWorker(self.base_url, text)
        self.worker.finished.connect(self.handle_result)
        self.worker.error.connect(self.handle_error)
        self.worker.start()

    # =========================
    # 处理后端返回
    # =========================
    def handle_result(self, result: dict):
        if not result.get("ok"):
            self.add_message("执行失败：" + result.get("answer", ""), False)
            return

        # 显示最终结果
        answer = result.get("answer", "")
        self.add_message("结果：\n" + answer, False)

        # 显示步骤日志
        raw = result.get("raw", {})
        steps = raw.get("steps", [])

        if steps:
            self.add_message("—— 执行步骤 ——", False)

        for step in steps:
            name = step.get("name", "")
            detail = step.get("detail", "")
            status = step.get("status", "")
            duration = step.get("duration_ms", 0)

            step_text = (
                f"{name}\n"
                f"状态: {status}\n"
                f"耗时: {duration} ms\n"
                f"{detail}"
            )

            self.add_message(step_text, False)

    # =========================
    # 错误处理
    # =========================
    def handle_error(self, msg: str):
        self.add_message("网络错误: " + msg, False)

    # =========================
    # Enter 发送 / Shift+Enter 换行
    # =========================
    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Return:
            if event.modifiers() == Qt.KeyboardModifier.ShiftModifier:
                super().keyPressEvent(event)
            else:
                self.send_message()
        else:
            super().keyPressEvent(event)