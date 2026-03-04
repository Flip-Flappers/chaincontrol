from PyQt6.QtCore import QThread, pyqtSignal
import torch
from qwen_asr.inference.qwen3_asr import Qwen3ASRModel


class ASRLoader(QThread):
    finished = pyqtSignal(object)

    def run(self):
        device = "cuda" if torch.cuda.is_available() else "cpu"
        dtype = torch.float16 if device == "cuda" else torch.float32

        print("Loading Qwen3-ASR on", device)

        model = Qwen3ASRModel.from_pretrained(
            "../Qwen3-ASR-0.6B",
            dtype=torch.bfloat16,
            device_map="cuda",
            # attn_implementation="flash_attention_2",
            max_inference_batch_size=32,
            # Batch size limit for inference. -1 means unlimited. Smaller values can help avoid OOM.
            max_new_tokens=256,  # Maximum number of tokens to generate. Set a larger value for long audio input.
        )


        self.finished.emit(model)