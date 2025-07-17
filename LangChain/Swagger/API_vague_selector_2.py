import os
import csv
import json

class API_vague_selector:
    # 指定文件路径
    csv_file_path = "./tmp/selectbyreturn.csv"  # 包含查询关键字的 CSV
    folder_path = "output"  # 搜索 JSON 文件的文件夹
    reference_csv = "api_paths_english.csv"  # 参考 CSV（存储 path -> tags, summary）
    output_csv_file = "./tmp/matched_results.csv"  # 输出 CSV

    def main(self):
        # 读取 CSV 文件中的字符串
        search_strings = set()
        with open(self.csv_file_path, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            header = next(reader)  # 获取表头
            if "className" in header:
                class_name_column_index = header.index("className")  # 获取 className 列的索引
                for row in reader:
                    if len(row) > class_name_column_index:  # 确保这一行包含 className 列
                        search_strings.add(row[class_name_column_index].strip())  # 添加 className 列的内容

        # 存储匹配的 JSON 文件
        matched_files = {}

        # 遍历文件夹，查找包含关键字的 JSON 文件
        for root, _, files in os.walk(self.folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                        content = f.read()
                        matches = [s for s in search_strings if s in content]
                        if matches:
                            matched_files[file_path] = matches
                except Exception as e:
                    print(f"无法读取文件 {file_path}: {e}")

        # **解析 JSON 提取 path**
        matched_paths = []
        matched_reasons = []
        for file, matches in matched_files.items():
            try:
                with open(file, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    if "paths" in data:
                        for path, methods in data["paths"].items():
                            for method, details in methods.items():
                                reason = "This API has"
                                if isinstance(details, dict):
                                    for match in matches:
                                        with open(self.csv_file_path, "r", encoding="utf-8") as f:
                                            reader = csv.reader(f)
                                            header = next(reader)  # 获取表头

                                            # 假设 className 和 content 分别在以下列
                                            class_name_column_index = header.index("className")  # 根据列名查找索引
                                            content_column_index = header.index("contents")  # 假设 'content' 是列名

                                            # 遍历 CSV 文件中的每一行
                                            for row in reader:
                                                # 假设你要查找的值在某一列（例如第 0 列），并且与 matches 中的某个元素匹配
                                                if match in row[0]:  # 假设匹配是针对第一列，你可以修改为其他列
                                                    content = row[content_column_index].split("Property Name: ")[1]
                                                    reason += " Property: " + content + ","
                                    print(reason[: -1] + ".")
                                    matched_paths.append(path)  # 只存储 path
                                    matched_reasons.append(reason[: -1] + ".")
            except Exception as e:
                print(f"无法解析 JSON 文件 {file}: {e}")

        # **读取参考 CSV（存储 path -> tags, summary）**
        path_info = {}
        with open(self.reference_csv, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                path_info[row["Path"]] = (row["Tags"], row["Summary"])  # 以 path 为键存储

        # **匹配 path，获取 tags 和 summary**
        matched_data = []
        for path in matched_paths:
            tags, summary = path_info.get(path, ("", ""))  # 如果找不到，默认空字符串
            matched_data.append([path, tags, summary, matched_reasons[matched_paths.index(path)]])

        # **写入 CSV**
        with open(self.output_csv_file, "w", encoding="utf-8", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["API path", "Tags", "Summary", "Reason"])  # CSV 头部
            writer.writerows(matched_data)

        print(f"匹配结果已保存至 {self.output_csv_file}")
