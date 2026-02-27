class ThemeManager:
    def __init__(self):
        self.current = "light"

    def toggle(self):
        self.current = "dark" if self.current == "light" else "light"

    def get_stylesheet(self):
        return self.base_style() + (
            self.light_theme() if self.current == "light" else self.dark_theme()
        )

    # ⭐⭐⭐ 新增：主窗口基础样式（圆角关键）
    def base_style(self):
        return """
        QMainWindow {
            background: transparent;
        }

        QWidget#container {
            border-radius: 22px;
        }
        
        QPushButton {
            border: none;
        }
        """

    # 🌞 暖色玻璃
    def light_theme(self):
        return """
        QWidget#container {
            background-color: #FDF6EC;
        }

        QWidget {
            color: #5E4631;
            font-family: "Microsoft YaHei";
            font-size: 14px;
        }

        QFrame#GlassCard {
            background-color: rgba(255,255,255,140);
            border-radius: 20px;
        }

        QPushButton {
            background-color: rgba(230,126,34,220);
            border-radius: 16px;
            padding: 6px 14px;
            color: white;
        }

        QPushButton:hover {
            background-color: #D35400;
        }

        QTextEdit {
            background-color: rgba(255,255,255,180);
            border-radius: 14px;
            padding: 8px;
        }
        
        QPushButton#closeBtn {
            background-color: #E74C3C;
            border-radius: 14px;
            color: white;
        }
        
        QPushButton#closeBtn:hover {
            background-color: #C0392B;
        }
        
        QPushButton#minBtn {
            background-color: #F1C40F;
            border-radius: 14px;
            color: white;
        }
        
        QPushButton#minBtn:hover {
            background-color: #D4AC0D;
        }
        
        QWidget#TitleBar {
            background-color: #F5EBDD;   /* 浅色实体背景 */
            border-top-left-radius: 22px;
            border-top-right-radius: 22px;
        }
        """

    # 🌙 深色玻璃
    def dark_theme(self):
        return """
        QWidget#container {
            background-color: #1E1E2E;
        }

        QWidget {
            color: #F5E6D3;
            font-family: "Microsoft YaHei";
            font-size: 14px;
        }

        QFrame#GlassCard {
            background-color: rgba(40,40,60,200);
            border-radius: 20px;
        }

        QPushButton {
            background-color: rgba(231,76,60,220);
            border-radius: 16px;
            padding: 6px 14px;
            color: white;
        }

        QPushButton:hover {
            background-color: #C0392B;
        }

        QTextEdit {
            background-color: rgba(50,50,70,200);
            border-radius: 14px;
            padding: 8px;
            color: white;
        }
        
        QPushButton#closeBtn {
            background-color: #C0392B;
            border-radius: 14px;
            color: white;
        }
        
        QPushButton#minBtn {
            background-color: #F39C12;
            border-radius: 14px;
            color: white;
        }
        
        QWidget#TitleBar {
            background-color: #2A2A3C;   /* 深色实体背景 */
            border-top-left-radius: 22px;
            border-top-right-radius: 22px;
        }
        """