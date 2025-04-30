import csv
import json
import re


# 读取 Swagger API 文档
def read_swagger_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


# 查找指定接口的地址
def find_endpoint(markdown_content, target_endpoint):

    endpoint_pattern = r'`' + re.escape(target_endpoint) + r'`'

    # 查找接口位置
    endpoint_matches = re.findall(endpoint_pattern, markdown_content)

    if not endpoint_matches:
        return None

    # 找到接口地址的位置
    endpoint_index = markdown_content.find(endpoint_matches[0])

    # 从接口位置开始查找下面的第一个 JavaScript 代码块
    relevant_content = markdown_content[endpoint_index:]

    # 查找第一个 JavaScript 代码块
    code_block_pattern = r'```javascript\n(.*?)\n```'

    # 查找第一个匹配的 JavaScript 代码块
    javascript_code = re.search(code_block_pattern, relevant_content, re.DOTALL)

    if javascript_code:
        return javascript_code.group(1)  # 返回匹配的 JavaScript 代码
    return None

def convert_to_json(found_endpoints):
    # 转换为 JSON 格式字符串
    json_obj = json.loads(found_endpoints)
    return json_obj


def print_json_keys(json_obj, parent_key=''):
    if isinstance(json_obj, dict):
        for key, value in json_obj.items():
            new_key = f"{parent_key}.{key}" if parent_key else key
            print(f"Field: {new_key}")  # 输出字段名字
            if isinstance(value, (dict, list)):  # 检查是否有儿子key
                print(f"    {new_key} has children.")  # 有儿子key
            print_json_keys(value, new_key)  # 递归调用处理子字段
    elif isinstance(json_obj, list):
        for index, item in enumerate(json_obj):
            new_key = f"{parent_key}[{index}]"
            print(f"Field: {new_key}")  # 输出字段名字
            if isinstance(item, (dict, list)):  # 检查是否有儿子key
                print(f"    {new_key} has children.")  # 有儿子key
            print_json_keys(item, new_key)

def write_json_keys_to_csv(json_obj, parent_key='', writer=None):
    if isinstance(json_obj, dict):
        for key, value in json_obj.items():
            new_key = f"{parent_key}.{key}" if parent_key else key
            has_children = 'Yes' if isinstance(value, (dict, list)) else 'No'  # 判断是否有儿子
            writer.writerow([new_key, has_children])  # 写入 CSV
            write_json_keys_to_csv(value, new_key, writer)  # 递归调用处理子字段
    elif isinstance(json_obj, list):
        for index, item in enumerate(json_obj):
            new_key = f"{parent_key}[{index}]"
            has_children = 'Yes' if isinstance(item, (dict, list)) else 'No'  # 判断是否有儿子
            writer.writerow([new_key, has_children])  # 写入 CSV
            write_json_keys_to_csv(item, new_key, writer)


def main():
    swagger_file = 'Swagger API.md'  # Swagger API 文档路径
    target_endpoint = '/device/list'  # 目标接口路径

    file_name = "./target_api.csv"
    target_endpoints = []
    with open(file_name, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        # 读取表头
        header = next(reader)
        # 找到 "Translated Rewritten Command" 列的索引
        if "Target API Name" in header:
            index = header.index("Target API Name")

            # 读取数据
            for row in reader:
                target_endpoints.append(row[index])

    target_endpoint = target_endpoints[0]

    # 读取 Swagger 文件内容
    markdown_content = read_swagger_file(swagger_file)

    # 查找指定接口的地址
    found_endpoints = find_endpoint(markdown_content, target_endpoint)

    json_obj = convert_to_json(found_endpoints)
    # 写入到文件
    with open("output.json", "w", encoding="utf-8") as json_file:
        json.dump(json_obj, json_file, ensure_ascii=False, indent=4)
    print('JSON Object:')
    print(json_obj)
    # 假设 json_obj 是你转换后的 JSON 对象
    json_obj = convert_to_json(found_endpoints)

    # 打开一个 CSV 文件并写入数据
    with open('json_keys.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Field Name', 'Has Children'])  # 写入表头
        write_json_keys_to_csv(json_obj, writer=writer)

    print("CSV file 'json_keys.csv' has been created.")

    print_json_keys(json_obj)
if __name__ == '__main__':
    main()
