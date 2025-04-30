import copy
import csv
import json
import logging
import os
import re
import sys

import requests
from langchain.chains import RetrievalQA
from langchain.chains.llm import LLMChain
from langchain.document_loaders import CSVLoader
from langchain.vectorstores import Chroma
from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaEmbeddings, OllamaLLM


# 设置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def remove_json_comments(json_text):
    """
    去除 JSON 字符串中的单行（//）和多行（/* */）注释
    """
    # 去除 // 单行注释
    json_text = re.sub(r'//.*', '', json_text)

    # 去除 /* */ 多行注释
    json_text = re.sub(r'/\*.*?\*/', '', json_text, flags=re.DOTALL)

    return json_text.strip()
def extract_json_objects(text):
    """
    从包含多个 JSON 片段的文本中提取所有完整的 JSON 对象
    """
    stack = []  # 记录 `{` 位置
    json_objects = []  # 存储解析出的 JSON
    start_idx = None  # JSON 起始索引

    for i, char in enumerate(text):
        if char == '{':
            if not stack:
                start_idx = i  # 记录 JSON 开始位置
            stack.append('{')  # 记录 `{`
        elif char == '}':
            if stack:
                stack.pop()  # 弹出 `{`
                if not stack:  # 栈为空，表示匹配到了完整的 JSON
                    json_str = text[start_idx:i + 1]  # 取出 JSON 字符串
                    try:
                        json_obj = json.loads(remove_json_comments(fix_single_quotes_json(json_str)))  # 解析 JSON
                        json_objects.append(json_obj)
                    except json.JSONDecodeError:
                        pass  # 忽略解析失败的部分

    return json_objects[0]
def fix_single_quotes_json(json_str: str) -> str:
    """
    修复 JSON 中的单引号，使其符合标准 JSON 规范（双引号）。
    仅修复键名和字符串值，不影响数字和布尔值。

    :param json_str: 可能含有单引号的 JSON 字符串
    :return: 修复后的 JSON 字符串
    """
    if not json_str:
        return json_str

    # 1. 修正键名的单引号，例如 {'key': 变成 {"key":
    json_str = re.sub(r"'(\w+)'\s*:", r'"\1":', json_str)

    # 2. 修正字符串值的单引号，例如: 'value' 变成: "value"
    json_str = re.sub(r':\s*\'([^\']*)\'', r': "\1"', json_str)

    return json_str
def remove_none_and_null_fields(json_obj):
    """
    递归删除 JSON 中值为 None 或 "NONE" 的字段
    :param json_obj: 输入 JSON（dict / list）
    :return: 处理后的 JSON（不含 None 和 "NONE"）
    """
    if isinstance(json_obj, dict):
        return {k: remove_none_and_null_fields(v) for k, v in json_obj.items() if v not in [None, "NONE", "", 0]}
    elif isinstance(json_obj, list):
        return [remove_none_and_null_fields(item) for item in json_obj]
    else:
        return json_obj  # 其他类型（str, int, bool）保持不变

def set_values_to_null(json_obj):
    """
        遍历 JSON 结构，将最底层（没有子节点的字段）替换为 "please update by << COMMAND >>"
        :param json_obj: 输入 JSON 对象（dict / list / str / int / bool）
        :return: 处理后的 JSON 对象
        """
    if isinstance(json_obj, dict):
        return {
            key: set_values_to_null(value) if isinstance(value, (dict, list)) else "please update by << COMMAND >>"
            for key, value in json_obj.items()
        }
    elif isinstance(json_obj, list):
        return [set_values_to_null(item) for item in json_obj]
    else:
        return "please update by << COMMAND >>"


def clean_json(data):
    """递归删除值为空的字段"""
    if isinstance(data, dict):
        return {k: clean_json(v) for k, v in data.items() if v not in (None, "", {}, [])}
    elif isinstance(data, list):
        return [clean_json(v) for v in data if v not in (None, "", {}, [])]
    else:
        return data
def main():
    try:
        llm = OllamaLLM(model="deepseek-r1:14b", base_url="http://localhost:11434", temperature=1.0)
        # 加载 CSV 文件
        loader = CSVLoader(file_path="./json_keys.csv", encoding="utf-8")
        # 读取 CSV 文件中的每一行

        data = {
            "deviceName": ""
        }

        # 转换为 JSON 字符串
        json_obj = json.dumps(data, indent=2)








        ans_json_obj = copy.deepcopy(set_values_to_null(json_obj))
        # 遍历每一行并打印


        # 填充值
        # 构建查询模板，使用 CSV 中的备选项作为上下文
        query_template = """
        You are an experienced expert in IoT systems. At present, users have found the target API, but they are not familiar with IoT software and can only issue vague commands. 
        At present, Nowadays, users want to know device details by << COMMAND >>.
        Please fill in the relevant content in the JSON field of the API according to the user's purpose and intention.
        The format of the API is shown as << API_FORMATTING >>.
        
        The user's command is shown as << COMMAND >>
        
        IMPORTANT: Fill in None if not explicitly stated in << COMMAND >>
        IMPORTANT: For fields that are not needed, MUST fill in "NONE", No matter what its current content is.
        IMPORTANT: For UNCERTAIN fields, MUST fill in "NONE", No matter what its current content is.
        IMPORTANT: For CERTAIN fields, sufficient utilization must be made base on  << COMMAND >>
        IMPORTANT: Only output the filled << API_FORMATTING >>
        IMPORTANT: The output MUST include all fields consistent with << API_FORMATTING >>.
        CAUTION: NO new fields can be added on the existing  << API_FORMATTING >>.
        << COMMAND >>
        {original_command}
       
         << API_FORMATTING >>
        {json_output}
        
        """

        file_name = "./commands.csv"
        translated_commands = []
        with open(file_name, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            # 读取表头
            header = next(reader)
            # 找到 "Translated Rewritten Command" 列的索引
            if "Translated Command" in header:
                index = header.index("Translated Command")

                # 读取数据
                for row in reader:
                    translated_commands.append(row[index])

        Rewritten_Command = []
        with open(file_name, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            # 读取表头
            header = next(reader)
            # 找到 "Translated Rewritten Command" 列的索引
            if "Rewritten Command" in header:
                index = header.index("Rewritten Command")
                # 读取数据
                for row in reader:
                    Rewritten_Command.append(row[index])

        command = translated_commands[0]

        prompt = PromptTemplate(
            input_variables=["original_command", "json_output"],
            template=query_template,
        )

        file_name = "./target_api.csv"
        target_api_names = []
        with open(file_name, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            # 读取表头
            header = next(reader)
            # 找到 "Translated Rewritten Command" 列的索引
            if "Target API Name" in header:
                index = header.index("Target API Name")

                # 读取数据
                for row in reader:
                    target_api_names.append(row[index])



        # 构建 LLMChain
        llm_chain = LLMChain(llm=llm, prompt=prompt)















        json_obj = set_values_to_null(json_obj)
        response = llm_chain.run(
            original_command=command,
            json_output=json_obj,
        )
        try:
            # 获取 "</think>" 后的部分
            json_part = response.split("</think>", 1)[1].strip()

            # 使用正则提取 JSON

            # 提取匹配的 JSON
            json_str = extract_json_objects(json_part)
            final_json_obj = remove_none_and_null_fields(json_str)# 解析 JSON
            print(final_json_obj)
            print(response)
            json_obj = remove_none_and_null_fields(final_json_obj)
            print(json_obj)

        except Exception as e:
            print(f"解析失败: {e}")



    except Exception as e:
        logger.error(f"运行时出错: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
