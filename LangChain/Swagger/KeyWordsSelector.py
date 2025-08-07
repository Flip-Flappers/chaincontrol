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

from LangChain.Swagger.tools.DeviceTool import DeviceTool
from LangChain.Swagger.tools.ProductTool import ProductTool
from model import deepseek

class KeyWordsSelector:

    def __init__(self):
        self.think = None
        self.answer = None
        self.ans = None
        self.deviceName = None
        self.productKey = None
        self.keyWords_list = \
            [
                "deviceName: String, Unique identifier of the device",
                "productKey: String, Unique identifier of the product",
            ]

        self.prompt_template = PromptTemplate(
            input_variables=["command", "KeyWord_list", "json_output"],
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
                    {command}
                    
                    <<KeyWord List>>
                    {KeyWord_list}
    
                    << Output Format >>
                    {json_output}
                """
        )

        self.json_output = """
            Return a markdown code snippet with JSON object formatted as follows:
            ```json
            {
                "total": int, // the number of results
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
        self.llm = deepseek.deepseek()
        self.file_name = "./tmp/keywords.json"

    def clean_json_string_with_regex(self, s: str) -> str:
        # 去掉开头 ``` 或 ```json 和后面的换行
        s = re.sub(r"^\s*```(?:json)?\s*\n?", "", s, flags=re.IGNORECASE)
        # 去掉结尾的 ``` 以及其后所有内容（换行+字符），使用非贪婪模式到字符串末尾
        s = re.sub(r"```[\s\S]*$", "", s)
        return s.strip()
    def extract_json(self, text: str) -> dict:
        # 提取首个以 { 开始、} 结束，并且中间括号平衡的 JSON 对象
        stack = []
        start = end = None

        for i, char in enumerate(text):
            if char == '{':
                if not stack:
                    start = i
                stack.append('{')
            elif char == '}':
                if stack:
                    stack.pop()
                    if not stack:
                        end = i + 1
                        break

        if start is not None and end is not None:
            json_str = text[start:end]
            return json.loads(self.clean_json_string_with_regex(json_str))  # 返回 dict，可改成 return json_str 返回字符串
        else:
            raise ValueError("未找到完整的 JSON 对象")

    # Write to CSV
    def write_to_json(self, json_str):
        try:
            data = self.extract_json(json_str)

            # 检查 results 是否存在且为列表
            results = data.get("results", [])
            if not isinstance(results, list):
                raise ValueError("'results' 应该是一个列表")

            # 删除旧文件（如果存在）
            if os.path.exists(self.file_name):
                os.remove(self.file_name)

            # 写入 JSON 文件
            with open(self.file_name, mode="w", encoding="utf-8") as file:
                json.dump(results, file, ensure_ascii=False, indent=2)

        except json.JSONDecodeError as e:
            print(f"解析 JSON 字符串失败: {e}")
        except Exception as e:
            print(f"写入 JSON 文件时出错: {e}")
        return data.get("results", [])

    def select_keywords(self, command):

        history = []
        is_first = True
        keyword_map = None
        for i in range(3):
            think, answer, history = self.llm.multi_chat(self.prompt_template.format(command=command, KeyWord_list=self.keyWords_list, json_output=self.json_output), history, is_first)
            is_first = False
            self.think = think
            self.answer = answer
            ans = self.write_to_json(answer)
            self.ans = ans
            keyword_map = {item["keyWordName"]: item["KeyWord"] for item in ans}
            deviceName = keyword_map.get("deviceName")
            productKey = keyword_map.get("productKey")
            if ((deviceName == "null" or deviceName == "None" or deviceName is None or deviceName == "" or deviceName == "NULL" or DeviceTool.check_deviceName(deviceName)) and
                (productKey == "null" or productKey == "None" or productKey is None or productKey == "" or productKey == "NULL" or ProductTool.check_productKey(productKey))):
                break
            if not DeviceTool.check_deviceName(deviceName):
                history.append({'role': 'user', 'content': "注意，上一次回答是:\n" + answer + "\n, 其中deviceName回答不正确,系统中无此名称设备，请按照要求，重新解析<< User Input >>！"})
            if not ProductTool.check_productKey(productKey):
                history.append({'role': 'user', 'content': "注意，上一次回答是:\n" + answer + "\n, 其中productKey回答不正确，系统中无此名称产品，请按照要求，重新解析<< User Input >>！"})


        return self.think, self.answer, keyword_map




