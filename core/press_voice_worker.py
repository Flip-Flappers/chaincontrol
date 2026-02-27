import numpy as np
import sounddevice as sd
from faster_whisper import WhisperModel
from PyQt6.QtCore import QThread, pyqtSignal


class PressVoiceWorker(QThread):
    finished_text = pyqtSignal(str)
    audio_level = pyqtSignal(object)

    def __init__(self):
        super().__init__()
        self.running = False
        self.audio_data = []
        self.model = WhisperModel("base", compute_type="int8")

    def run(self):
        self.running = True
        sample_rate = 16000

        def callback(indata, frames, time, status):
            if not self.running:
                return
            self.audio_data.append(indata.copy())
            self.audio_level.emit(indata)

        with sd.InputStream(
            samplerate=sample_rate,
            channels=1,
            callback=callback
        ):
            while self.running:
                sd.sleep(50)

        audio = np.concatenate(self.audio_data, axis=0)
        audio = np.squeeze(audio)

        segments, _ = self.model.transcribe(audio, language="zh")

        text = ""
        for segment in segments:
            text += segment.text

        self.finished_text.emit(text)

    def stop(self):
        self.running = False