import json
import os
import csv


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


def extract_paths_to_csv(swagger_data, output_csv):
    with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["Path", "Method", "Tags", "Summary"])

        for api_path, methods in swagger_data['paths'].items():
            for method, details in methods.items():
                tags = ", ".join(details.get("tags", []))
                summary = details.get("summary", "")
                csv_writer.writerow([api_path, method.upper(), tags, summary])
    print(f"CSV file saved: {output_csv}")


def split_swagger_json(input_file, output_dir, output_csv):
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

    extract_paths_to_csv(swagger_data, output_csv)


if __name__ == "__main__":
    input_file = "swagger.json"  # 请替换为你的 Swagger JSON 文件路径
    output_dir = "output"  # 输出目录
    output_csv = "api_paths.csv"  # 输出 CSV 文件路径
    split_swagger_json(input_file, output_dir, output_csv)
