from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout,
    QFrame, QTextEdit, QPushButton,
    QScrollArea, QApplication
)
from PyQt6.QtCore import Qt

from core.assistant_worker import AssistantWorker
from ui.components.message_item import MessageItem
from ui.components.wave_widget import WaveWidget
from core.press_voice_worker import StreamingVoiceWorker


class ConsolePage(QWidget):
    def __init__(self):
        super().__init__()

        self.base_url = "http://127.0.0.1:8000"
        self.worker = None
        self.asr_model = None

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

        self.wave = WaveWidget()
        self.wave.hide()

        self.mic_btn = QPushButton("🎤 按住说话")
        self.mic_btn.setObjectName("micBtn")

        self.mic_btn.pressed.connect(self.start_recording)
        self.mic_btn.released.connect(self.stop_recording)

        send_btn = QPushButton("发送")
        send_btn.clicked.connect(self.send_message)

        input_layout.addWidget(self.input_box)
        input_layout.addWidget(send_btn)

        layout.addWidget(self.wave)
        layout.addWidget(self.mic_btn)
        layout.addWidget(input_card)

        self.add_message("系统已连接到 127.0.0.1:8000", False)

    # ======================
    # 启动语音识别
    # ======================
    def start_recording(self):
        if self.worker and self.worker.isRunning():
            return

        if not self.asr_model:
            return

        self.mic_btn.setText("🔴 录音中...")
        self.wave.show()

        self.worker = StreamingVoiceWorker(self.asr_model)

        self.worker.audio_level.connect(self.wave.update_level)
        self.worker.partial_text.connect(self.update_partial_text)
        self.worker.finished_text.connect(self.update_final_text)

        self.worker.start()

    def stop_recording(self):
        self.mic_btn.setText("🎤 按住说话")
        self.wave.hide()

        if self.worker and self.worker.isRunning():
            self.worker.stop()

    # ======================
    # 语音识别回调
    # ======================
    def update_partial_text(self, text):
        self.input_box.setPlainText(text)
        cursor = self.input_box.textCursor()
        cursor.movePosition(cursor.MoveOperation.End)
        self.input_box.setTextCursor(cursor)

    def update_final_text(self, text):
        self.input_box.setPlainText(text)

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

        self.add_message(text, True)
        self.input_box.clear()

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

        answer = result.get("answer", "")
        self.add_message("结果：\n" + answer, False)

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