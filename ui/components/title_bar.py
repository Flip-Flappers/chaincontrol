from PyQt6.QtWidgets import QWidget, QHBoxLayout, QPushButton
from PyQt6.QtCore import Qt, pyqtSignal

from ui.components.avatar_widget import AvatarWidget


class TitleBar(QWidget):
    close_clicked = pyqtSignal()
    minimize_clicked = pyqtSignal()
    theme_clicked = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setObjectName("TitleBar")
        self.setFixedHeight(50)
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)

        layout = QHBoxLayout(self)
        layout.setContentsMargins(15, 5, 15, 5)
        layout.setSpacing(10)

        # 左侧按钮
        self.close_btn = QPushButton("✕")
        self.close_btn.setObjectName("closeBtn")
        self.close_btn.setFixedSize(28, 28)
        self.close_btn.clicked.connect(self.close_clicked.emit)

        self.min_btn = QPushButton("—")
        self.min_btn.setObjectName("minBtn")
        self.min_btn.setFixedSize(28, 28)
        self.min_btn.clicked.connect(self.minimize_clicked.emit)

        layout.addWidget(self.close_btn)
        layout.addWidget(self.min_btn)

        layout.addStretch()

        # 主题按钮
        self.theme_btn = QPushButton("🌙")
        self.theme_btn.setObjectName("themeBtn")
        self.theme_btn.setFixedSize(36, 36)
        self.theme_btn.clicked.connect(self.theme_clicked)
        layout.addWidget(self.theme_btn)

        # ⭐ 头像在内部创建
        self.avatar = AvatarWidget(
            image_path="./assets/avatar.png",
            size=36,
            online=True
        )

        layout.addWidget(self.avatar)

