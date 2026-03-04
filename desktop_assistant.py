import sys
from PyQt6.QtWidgets import QApplication
from ui.main_window import MainWindow

def load_qwen_asr(model_path="./Qwen3-ASR-0.6B"):
    import torch
    from qwen_asr.inference.qwen3_asr import Qwen3ASRModel

    device = "cuda" if torch.cuda.is_available() else "cpu"

    # GPU 用 float16，CPU 用 float32
    dtype = torch.float16 if device == "cuda" else torch.float32

    print(f"Loading Qwen3-ASR on {device} with {dtype}")

    model = Qwen3ASRModel.from_pretrained(
        model_path,
        dtype=dtype,
        device=device,            # ⚠ 不用 device_map
        max_new_tokens=256,
    )

    model.eval()  # 防止多余开销

    return model
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()