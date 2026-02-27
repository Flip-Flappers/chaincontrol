from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt

class LogPage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        label = QLabel("日志页面")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label)