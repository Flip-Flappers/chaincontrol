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
        
        QPushButton#micBtn {
            background-color: rgba(100,150,255,200);
        }
        """

    # 🌞 暖色玻璃
    def light_theme(self):
        return """
        QWidget#container {
            background-color: #F6EFE6;   /* 更高级的奶油底色 */
        }

        QWidget {
            color: #4A3A2A;   /* 更柔和的深棕 */
            font-family: "Microsoft YaHei";
            font-size: 14px;
        }

        QFrame#GlassCard {
            background-color: rgba(255,255,255,160);
            border-radius: 20px;
        }

        QPushButton {
            background-color: rgba(219,122,55,210);   /* 柔和橙棕 */
            border-radius: 16px;
            padding: 6px 14px;
            color: #FFFFFF;
        }

        QPushButton:hover {
            background-color: #C76A2E;   /* 更自然的hover */
        }

        QTextEdit {
            background-color: rgba(255,255,255,200);
            border-radius: 14px;
            padding: 8px;
            color: #4A3A2A;
        }

        QPushButton#closeBtn {
            background-color: #D64541;   /* 不刺眼的红 */
            border-radius: 14px;
            color: white;
        }

        QPushButton#closeBtn:hover {
            background-color: #B03A2E;
        }

        QPushButton#minBtn {
            background-color: #E0B326;   /* 柔黄 */
            border-radius: 14px;
            color: white;
        }

        QPushButton#minBtn:hover {
            background-color: #C79E1D;
        }

        QWidget#TitleBar {
            background-color: #EFE5D8;   
            border-top-left-radius: 22px;
            border-top-right-radius: 22px;
        } 
         
          
        """

    def dark_theme(self):
        return """
        QWidget#container {
            background-color: #1B1F2B;   /* 蓝灰夜色 */
        }

        QWidget {
            color: #E8DCCD;   /* 柔和米白 */
            font-family: "Microsoft YaHei";
            font-size: 14px;
        }

        QFrame#GlassCard {
            background-color: rgba(38,42,58,210);
            border-radius: 20px;
        }

        QPushButton {
            background-color: rgba(176,58,46,220);   /* 酒红 */
            border-radius: 16px;
            padding: 6px 14px;
            color: #FFFFFF;
        }

        QPushButton:hover {
            background-color: #943126;
        }

        QTextEdit {
            background-color: rgba(45,50,70,220);
            border-radius: 14px;
            padding: 8px;
            color: #F2EDE6;
        }

        QPushButton#closeBtn {
            background-color: #A93226;
            border-radius: 14px;
            color: white;
        }

        QPushButton#minBtn {
            background-color: #D68910;
            border-radius: 14px;
            color: white;
        }

        QWidget#TitleBar {
            background-color: #24283A;
            border-top-left-radius: 22px;
            border-top-right-radius: 22px;
        }
        """