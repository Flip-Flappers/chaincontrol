import numpy as np
from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QPainter, QColor, QPen
from PyQt6.QtCore import QTimer


class WaveWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.setMinimumHeight(60)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(30)

    def update_level(self, audio_chunk):
        self.level = np.abs(audio_chunk).mean()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        width = self.width()
        height = self.height()

        bar_count = 20
        bar_width = width / bar_count

        for i in range(bar_count):
            bar_height = self.level * height * np.random.uniform(0.5, 1.2)
            x = i * bar_width
            y = (height - bar_height) / 2

            painter.setBrush(QColor(100, 180, 255))
            painter.setPen(Qt.PenStyle.NoPen)
            painter.drawRoundedRect(
                int(x),
                int(y),
                int(bar_width * 0.6),
                int(bar_height),
                4,
                4,
            )