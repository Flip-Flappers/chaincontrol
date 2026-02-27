from PyQt6.QtWidgets import QFrame, QLabel, QHBoxLayout

class MessageItem(QFrame):
    def __init__(self, text, is_user=True):
        super().__init__()

        layout = QHBoxLayout(self)
        layout.setContentsMargins(10, 5, 10, 5)

        bubble = QLabel(text)
        bubble.setWordWrap(True)
        bubble.setMaximumWidth(400)
        bubble.setStyleSheet("""
            QLabel {
                padding: 10px 14px;
                border-radius: 16px;
                background-color: rgba(255,255,255,200);
            }
        """)

        if is_user:
            layout.addStretch()
            layout.addWidget(bubble)
        else:
            layout.addWidget(bubble)
            layout.addStretch()