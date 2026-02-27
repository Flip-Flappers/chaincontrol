import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow,
    QWidget, QHBoxLayout, QVBoxLayout,
    QStackedWidget, QPushButton
)
from PyQt6.QtCore import Qt

from ui.components.sidebar import Sidebar
from pages.console_page import ConsolePage
from pages.device_page import DevicePage
from pages.log_page import LogPage
from theme.theme_manager import ThemeManager
from ui.components.avatar_widget import AvatarWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("玻璃拟态聊天系统")
        self.resize(1100, 700)

        self.theme_manager = ThemeManager()
        self.setStyleSheet(self.theme_manager.get_stylesheet())


        central = QWidget()
        self.setCentralWidget(central)

        main_layout = QVBoxLayout(central)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(10)

        # ===== 顶部栏（右上角主题按钮）=====
        top_bar = QHBoxLayout()
        top_bar.addStretch()



        self.theme_btn = QPushButton("🌙")
        self.theme_btn.setFixedSize(40, 40)
        self.theme_btn.clicked.connect(self.toggle_theme)

        top_bar.addWidget(self.theme_btn)
        main_layout.addLayout(top_bar)

        # ===== 左上角头像 =====
        self.avatar = AvatarWidget(
            image_path="./assets/avatar.png",
            size=40,
            online=True  # 是否显示在线状态
        )

        top_bar.addWidget(self.avatar)

        # ===== 主体区域 =====
        content_layout = QHBoxLayout()
        content_layout.setSpacing(20)

        self.sidebar = Sidebar()
        self.sidebar.page_changed.connect(self.change_page)

        self.stack = QStackedWidget()
        self.stack.addWidget(ConsolePage())
        self.stack.addWidget(DevicePage())
        self.stack.addWidget(LogPage())

        content_layout.addWidget(self.sidebar)
        content_layout.addWidget(self.stack)

        main_layout.addLayout(content_layout)

    # =========================
    # 页面切换
    # =========================
    def change_page(self, index):
        self.stack.setCurrentIndex(index)

    # =========================
    # 主题切换
    # =========================
    def toggle_theme(self):
        self.theme_manager.toggle()
        self.setStyleSheet(self.theme_manager.get_stylesheet())

        # 切换图标
        if self.theme_btn.text() == "🌙":
            self.theme_btn.setText("☀")
        else:
            self.theme_btn.setText("🌙")