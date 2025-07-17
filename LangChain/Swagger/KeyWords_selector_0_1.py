import concurrent
import csv
import json
import re
import os

import requests
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_ollama import OllamaLLM
from transformers import MarianMTModel, MarianTokenizer


class KeyWords_selector:

    headers = {
        "Content-Type": "application/json"
    }
    def post_json(self, url, data):
        headers = {
            "Content-Type": "application/json"
        }

        try:
            # 将 Python 对象转为 JSON 字符串
            response = requests.post(url, headers = self.headers, data=json.dumps(data))
            response.raise_for_status()  # 如果响应状态码是 4xx/5xx，会抛出异常
            print("响应状态码:", response.status_code)
            print("响应内容:", response.text)
        except requests.exceptions.RequestException as e:
            print("请求失败:", e)

    url = "http://192.168.4.163:8080/device/detail"



    KeyWords_list = \
        ["deviceName: String, Unique identifier of the device",
         "productKey: String, Unique identifier of the product",
         "action: String he action that the user wishes to trigger in << User Input >>",
         "params: map , Parameters contained in << User Input >>"
         ]

    prompt_template = PromptTemplate(
        input_variables=["translate_command", "KeyWord_list", "json_output"],
        template="""
                You are an experienced IoT system expert. Users of the IoT control software often issue vague or ambiguous commands. Your task is to extract the specified keywords from the user's COMMANDS.
                Focus on realistic and typical IoT scenarios, such as:
                - Smart home automation (e.g., controlling lights, thermostat, appliances)
                - Device scheduling (timers and routines)
                - Energy efficiency and management
                - Security monitoring (e.g., cameras, alarms)
                - Sensor integration and data monitoring
                - Remote device control and management

               
                IMPORTANT: Use detailed, professional language and logical reasoning to connect the user’s vague command to that specific intent.
                Attention: Ensure each intention is distinct, practical, and clearly described.
                Attention: Avoid vague or redundant phrasing.
                Caution: Keep the user’s perspective in mind and do not stray beyond what their command plausibly means.

                Emphasize that the goal is to help the user discover the software’s capabilities more precisely and effectively.

                << User Input >>
                {translate_command}
                
                <<KeyWord List>>
                {KeyWord_list}

                << Output Format >>
                {json_output}
            """
    )

    # 示例 JSON 输出部分
    json_output = """
        Return a markdown code snippet with JSON object formatted as follows:
        ```json
        {
            "total": 10,
            "results": [
                {
                    "id": 1, // the first KeyWord,
                    "keyWordName": string // the name of the first KeyWord in <<KeyWord List>>
                    "KeyWord": string,  
                },
                {
                    "id": 2, // the second KeyWord
                    "keyWordName": string // the type of the second KeyWord in <<KeyWord List>>
                    "KeyWord": string,  
                },
                ...
            ]
        }
        ```
        REMEMBER: "KeyWord" MUST be based on << User Input >>
        REMEMBER: "keyWordName" Must be consistent with <<KeyWord List>>
        REMEMBER: If there is no corresponding keyword, it defaults to null
        """

    llm = OllamaLLM(model="deepseek-r1:14b", base_url="http://localhost:11434", temperature=1.0)
    llm_chain = LLMChain(prompt=prompt_template, llm=llm)

    translate_model_name = "Helsinki-NLP/opus-mt-zh-en"

    file_name = "./tmp"

    def clean_json_string_with_regex(self, s: str) -> str:
        # 去除开头 ```json 或 ```，以及结尾的 ```
        cleaned = re.sub(r"^\s*```(?:json)?\s*", "", s)  # 去除开头
        cleaned = re.sub(r"\s*```\s*$", "", cleaned)  # 去除结尾
        return cleaned.strip()
    # Write to CSV
    def write_to_json(self, json_str, language):
        try:
            data = self.clean_json_string_with_regex(json_str)
            data = json.loads(data)

            # 检查 results 是否存在且为列表
            results = data.get("results", [])
            if not isinstance(results, list):
                raise ValueError("'results' 应该是一个列表")

            # 删除旧文件（如果存在）
            if os.path.exists(self.file_name + "/" + language + "_eyWords.json"):
                os.remove(self.file_name + "" + language + "_keyWords.json")

            # 写入 JSON 文件

            with open(self.file_name + "/" + language + "_keyWords.json", mode="w", encoding="utf-8") as file:
                json.dump(results, file, ensure_ascii=False, indent=2)

        except json.JSONDecodeError as e:
            print(f"解析 JSON 字符串失败: {e}")
        except Exception as e:
            print(f"写入 JSON 文件时出错: {e}")

    def find_keywords(self, command, language):




        keywords_str = ",".join(self.KeyWords_list)
        # 获取重写后的指令
        target_key_words = self.llm_chain.run(
            {"translate_command": command, "KeyWord_list": keywords_str,"json_output": self.json_output})
        target_key_words = target_key_words.split("</think>")[1]
        print(f"找到KeyWords：{target_key_words}")
        # 使用正则表达式提取 "user intent" 内容
        self.write_to_json(target_key_words, language)


    def read_column(self, file_name, column_name):
        result = []
        with open(file_name, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            header = next(reader)
            if column_name in header:
                index = header.index(column_name)
                for row in reader:
                    result.append(row[index])
        return result

    def run_find_keywords(self, text, name):
        processor = KeyWords_selector()
        print(f"开始处理：{name}")
        processor.find_keywords(text, name)

    def main(self):
        file_name = "./tmp/commands.csv"

        # 并发读取 CSV 两列
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future_translated = executor.submit(self.read_column, file_name, "Translated Command")
            future_original = executor.submit(self.read_column, file_name, "Original Command")
            Translated_Command = future_translated.result()
            Original_Command = future_original.result()

        # 并发处理 find_keywords（两个独立的 KeyWords_selector 实例）
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = [
                executor.submit(self.run_find_keywords, Translated_Command[0], "english"),
                executor.submit(self.run_find_keywords, Original_Command[0], "chinese")
            ]

            # 等待所有处理完成
            for f in concurrent.futures.as_completed(futures):
                f.result()




if __name__ == "__main__":
    commandC2E = KeyWords_selector()
    commandC2E.main()
