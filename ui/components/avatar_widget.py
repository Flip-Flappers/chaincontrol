from PyQt6.QtWidgets import QLabel, QWidget
from PyQt6.QtGui import QPixmap, QPainter, QPainterPath
from PyQt6.QtCore import Qt


class AvatarWidget(QWidget):
    def __init__(self, image_path: str, size: int = 40, online: bool = False):
        super().__init__()

        self.size = size
        self.image_path = image_path
        self.online = online

        self.setFixedSize(size, size)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        # ===== 圆形裁剪路径 =====
        path = QPainterPath()
        path.addEllipse(0, 0, self.size, self.size)
        painter.setClipPath(path)

        pixmap = QPixmap(self.image_path)

        if not pixmap.isNull():
            pixmap = pixmap.scaled(
                self.size,
                self.size,
                Qt.AspectRatioMode.KeepAspectRatioByExpanding,
                Qt.TransformationMode.SmoothTransformation
            )
            painter.drawPixmap(0, 0, pixmap)
        else:
            painter.fillRect(self.rect(), Qt.GlobalColor.gray)

        painter.setClipping(False)

        # ===== 在线状态小绿点 =====
        if self.online:
            dot_size = int(self.size * 0.28)
            painter.setBrush(Qt.GlobalColor.green)
            painter.setPen(Qt.PenStyle.NoPen)
            painter.drawEllipse(
                self.size - dot_size,
                self.size - dot_size,
                dot_size,
                dot_size
            )