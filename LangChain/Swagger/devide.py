import json
import os


def save_api_file(api_path, api_data, output_dir):
    filename = api_path.strip('/').replace('/', '_') + '.json'
    filepath = os.path.join(output_dir, filename)

    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(api_data, f, indent=2, ensure_ascii=False)
    print(f"Saved: {filepath}")


def save_definition_file(def_name, def_data, output_dir):
    filename = f"{def_name}.json"
    filepath = os.path.join(output_dir, filename)

    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(def_data, f, indent=2, ensure_ascii=False)
    print(f"Saved: {filepath}")


def split_swagger_json(input_file, output_dir):
    with open(input_file, 'r', encoding='utf-8') as f:
        swagger_data = json.load(f)

    if 'paths' not in swagger_data:
        print("Invalid Swagger JSON: No 'paths' found.")
        return

    os.makedirs(output_dir, exist_ok=True)
    definitions_dir = os.path.join(output_dir, "definitions")
    os.makedirs(definitions_dir, exist_ok=True)

    for api_path, methods in swagger_data['paths'].items():
        api_data = {
            "swagger": swagger_data.get("swagger", "2.0"),
            "info": swagger_data.get("info", {}),
            "paths": {
                api_path: methods
            }
        }
        save_api_file(api_path, api_data, output_dir)

    if 'definitions' in swagger_data:
        for def_name, def_data in swagger_data['definitions'].items():
            save_definition_file(def_name, def_data, definitions_dir)


if __name__ == "__main__":
    input_file = "swagger.json"  # 请替换为你的 Swagger JSON 文件路径
    output_dir = "output"  # 输出目录
    split_swagger_json(input_file, output_dir)
