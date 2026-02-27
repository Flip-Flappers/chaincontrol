import speech_recognition as sr
from PyQt6.QtCore import QThread, pyqtSignal


class VoiceWorker(QThread):
    result_ready = pyqtSignal(str)
    error_occurred = pyqtSignal(str)

    def run(self):
        recognizer = sr.Recognizer()

        try:
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source)

            text = recognizer.recognize_google(audio, language="zh-CN")
            self.result_ready.emit(text)

        except Exception as e:
            self.error_occurred.emit(str(e))