import re
import csv

def extract_file_info(file_path):
    file_info = []
    max_columns = 0  # 记录最大字段数

    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

        # 根据文件名称分割文件内容成多个块
        blocks = re.split(r'-- 文件名称: ', content)[1:]  # 第一个元素为空，忽略

        for block in blocks:
            # 提取文件名称和文件描述
            name_match = re.match(r'(.+?)\s+-- 文件描述: (.+?)(?=\n-- 文件名称:|-- 使用场景:|$)', block, re.DOTALL)
            if not name_match:
                continue

            file_name = name_match.group(1).strip()[:-4]  # 去掉 .sql 后缀
            file_description = name_match.group(2).strip().replace('\n', ' ').replace('  ', ' ')  # 清理空格和换行

            # 提取列名和列注释
            column_pattern = r'\s+(\w+)\s+.*?COMMENT\s+\'(.*?)\''
            columns = re.findall(column_pattern, block)
            max_columns = max(max_columns, len(columns))  # 更新最大列数

            # 组织数据：前两列是表信息，后续是列信息（交替存储列名和列描述）
            row = [file_name, file_description]
            for col_name, col_desc in columns:
                row.append(col_name)
                row.append(col_desc)

            file_info.append(row)

    return file_info, max_columns

def save_to_csv(file_info, output_file, max_columns):
    # 生成 CSV 头部
    header = ["table_name", "table_description"]
    for i in range(1, max_columns + 1):
        header.append(f"column_{i}_name")
        header.append(f"column_{i}_description")

    # 写入 CSV
    with open(output_file, 'w', encoding='utf-8', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(header)  # 写入表头
        writer.writerows(file_info)  # 写入数据

# 示例调用
file_path = './script.sql'  # 替换为文件路径
output_file = 'pre_sql.csv'  # 输出的 CSV 文件路径

# 提取数据
file_info, max_columns = extract_file_info(file_path)

# 保存到 CSV
save_to_csv(file_info, output_file, max_columns)

print(f'文件名称和描述已保存到 {output_file}')
