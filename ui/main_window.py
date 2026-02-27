import sys

from PyQt6.QtGui import QMouseEvent
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
from ui.components.title_bar import TitleBar


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self._drag_pos = None
        self.setWindowFlags(self.windowFlags() | Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
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



        self.title_bar = TitleBar()

        self.title_bar.close_clicked.connect(self.close)
        self.title_bar.minimize_clicked.connect(self.showMinimized)
        self.title_bar.theme_clicked.connect(self.toggle_theme)

        main_layout.addWidget(self.title_bar)
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

    def toggle_theme(self):
        self.theme_manager.toggle()
        self.setStyleSheet(self.theme_manager.get_stylesheet())

        btn = self.title_bar.theme_btn

        if btn.text() == "🌙":
            btn.setText("☀")
        else:
            btn.setText("🌙")

    # =========================
    # 允许拖动窗口
    # =========================
    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self._drag_pos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event: QMouseEvent):
        if self._drag_pos:
            delta = event.globalPosition().toPoint() - self._drag_pos
            self.move(self.pos() + delta)
            self._drag_pos = event.globalPosition().toPoint()

    def mouseReleaseEvent(self, event: QMouseEvent):
        self._drag_pos = None