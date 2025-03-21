import os
import csv


def split_csv(input_file, output_dir):
    # 如果输出目录不存在，则创建
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 读取原始 CSV 文件
    with open(input_file, newline='', encoding='utf-8') as infile:
        reader = csv.reader(infile)
        header = next(reader)  # 假设第一行是表头

        # 遍历每一行并生成一个新的 CSV 文件
        for i, row in enumerate(reader, start=1):
            output_file = os.path.join(output_dir, f"output_{i}.csv")
            with open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
                writer = csv.writer(outfile)
                writer.writerow(header)  # 写入表头
                writer.writerow(row)  # 写入当前行

    print("拆分完成！")


# 使用方法：调用 `split_csv` 并传入 CSV 文件路径和输出目录
split_csv('pre_sql.csv', './haha')  # 示例：输出到 './haha' 目录
