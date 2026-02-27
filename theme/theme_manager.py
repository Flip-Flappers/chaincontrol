class ThemeManager:
    def __init__(self):
        self.current = "light"

    def toggle(self):
        self.current = "dark" if self.current == "light" else "light"

    def get_stylesheet(self):
        return self.light_theme() if self.current == "light" else self.dark_theme()

    # 🌞 暖色玻璃
    def light_theme(self):
        return """
        QWidget {
            background-color: #FDF6EC;
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
        """

    # 🌙 深色玻璃
    def dark_theme(self):
        return """
        QWidget {
            background-color: #1E1E2E;
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
        """