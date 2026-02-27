from PyQt6.QtWidgets import QFrame, QVBoxLayout, QPushButton
from PyQt6.QtCore import pyqtSignal

class Sidebar(QFrame):
    page_changed = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self.setFixedWidth(180)
        self.setObjectName("GlassCard")

        layout = QVBoxLayout(self)
        layout.setContentsMargins(15, 20, 15, 20)
        layout.setSpacing(15)

        buttons = [
            ("控制台", 0),
            ("设备", 1),
            ("日志", 2),

        ]

        for text, index in buttons:
            btn = QPushButton(text)
            btn.clicked.connect(lambda _, i=index: self.page_changed.emit(i))
            layout.addWidget(btn)

        layout.addStretch()