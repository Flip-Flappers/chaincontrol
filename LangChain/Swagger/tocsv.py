import os
import json
import csv
import logging

# 设置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 定义输入输出目录
INPUT_DIR = "./definitions"
OUTPUT_DIR = "./csv_definitions"

# 确保输出目录存在
os.makedirs(OUTPUT_DIR, exist_ok=True)

def convert_json_to_csv(json_file, csv_file):
    """将 JSON 文件转换为 CSV"""
    try:
        with open(json_file, "r", encoding="utf-8") as f:
            data = json.load(f)

        title = data.get("title", "Unknown")
        properties = data.get("properties", {})

        # 解析 properties
        rows = []
        for prop_name, prop_info in properties.items():
            prop_type = prop_info.get("type", "Unknown")
            prop_format = prop_info.get("format", "")
            rows.append([prop_name, prop_type, prop_format])

        # 写入 CSV
        with open(csv_file, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Property Name", "Type", "Format"])  # CSV 头部
            writer.writerows(rows)

        logger.info(f"转换完成: {csv_file}")

    except Exception as e:
        logger.error(f"转换 {json_file} 失败: {e}")

def main():
    json_files = [f for f in os.listdir(INPUT_DIR) if f.endswith(".json")]
    for json_file in json_files:
        json_path = os.path.join(INPUT_DIR, json_file)
        csv_path = os.path.join(OUTPUT_DIR, json_file.replace(".json", ".csv"))
        convert_json_to_csv(json_path, csv_path)

if __name__ == "__main__":
    main()
