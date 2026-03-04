import io
import os
import tempfile

import numpy as np
import sounddevice as sd
import torch
from PyQt6.QtCore import QThread, pyqtSignal
import soundfile as sf

class StreamingVoiceWorker(QThread):
    partial_text = pyqtSignal(str)   # 实时文本
    finished_text = pyqtSignal(str)  # 最终文本
    audio_level = pyqtSignal(object)

    def __init__(self, model):
        super().__init__()

        self.model = model
        self.running = False
        self.sample_rate = 16000

        self.buffer = []
        self.full_audio = []

        # 每多少秒识别一次
        self.chunk_seconds = 0.6
        self.chunk_size = int(self.sample_rate * self.chunk_seconds)

    # =============================
    # 主线程分块识别错误
    # =============================
    def run(self):
        print("STREAMING STARTED")

        self.running = True
        self.buffer.clear()
        self.full_audio.clear()

        def callback(indata, frames, time, status):

            if not self.running:
                return

            audio = indata.copy().flatten()

            self.buffer.append(audio)
            self.full_audio.append(audio)
            self.audio_level.emit(indata)

            # 达到 chunk_size 就识别
            current_len = sum(len(x) for x in self.buffer)

            if current_len >= self.chunk_size:
                chunk = np.concatenate(self.buffer)
                self.buffer.clear()

                self.process_chunk(chunk)

        try:
            self.stream = sd.InputStream(
                samplerate=self.sample_rate,
                channels=1,
                dtype="float32",
                callback=callback
            )

            self.stream.start()

            while self.running:

                sd.sleep(50)

            self.stream.stop()
            self.stream.close()

        except Exception as e:
            print("录音异常:", e)
            return

        # 最终识别
        if self.full_audio:
            final_audio = np.concatenate(self.full_audio)
            self.process_final(final_audio)

    # =============================
    # 分块识别
    # =============================
    def process_chunk(self, audio_np):

        self.partial_text.emit("录音中")



    # =============================
    # 最终识别
    # =============================
    def process_final(self, audio_np):
        try:
            # 创建临时 wav 文件
            with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
                wav_path = f.name

            # 写入 wav
            sf.write(wav_path, audio_np, 16000)

            print("识别中:", wav_path)

            # 调用模型（必须传路径）
            result = self.model.transcribe(
                audio=wav_path,
                language="Chinese"
            )

            text = result[0].text if result else ""
            self.finished_text.emit(text)

        except Exception as e:
            print("最终识别错误:", e)
            self.finished_text.emit("识别失败")

        finally:
            # 删除临时文件
            try:
                if os.path.exists(wav_path):
                    os.remove(wav_path)
            except:
                pass


    # =============================
    # 停止
    # =============================
    def stop(self):
        self.running = False
        self.wait()