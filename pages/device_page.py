from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt

class DevicePage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        label = QLabel("设备页面")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label)