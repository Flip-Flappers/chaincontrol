import requests
from PyQt6.QtCore import QThread, pyqtSignal


class AssistantWorker(QThread):
    finished = pyqtSignal(dict)
    error = pyqtSignal(str)

    def __init__(self, base_url, command):
        super().__init__()
        self.base_url = base_url
        self.command = command

    def run(self):
        try:
            r = requests.post(
                f"{self.base_url.rstrip('/')}/control",
                json={"command": self.command, "user_id": "user-001"},
                timeout=20,
            )
            r.raise_for_status()
            self.finished.emit(r.json())
        except Exception as e:
            self.error.emit(str(e))