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
BASE_URL = "http://localhost:8086"
class KeyWordsSelector:

    def __init__(self):
        self.think = None
        self.answer = None
        self.ans = None
        self.deviceName = None
        self.productKey = None
        self.keyWords_list = \
            [
                "deviceName: String, Unique identifier of the device.\n",
                "productKey: String, Unique identifier of the product.\n",
            ]

        self.prompt_template = PromptTemplate(
            input_variables=["command", "KeyWord_list", "json_output"],
            template="""
                    You are an experienced IoT system expert. Users of the IoT control software often issue vague or ambiguous commands. \n
                    ## The First Task： you need to extract the specified keywords from the << User Input >>.\n
                    Focus on realistic and typical IoT scenarios, such as:\n
                    - Smart home automation (e.g., controlling lights, thermostat, appliances)\n
                    - Device scheduling (timers and routines)\n
                    - Energy efficiency and management\n
                    - Security monitoring (e.g., cameras, alarms)\n
                    - Sensor integration and data monitoring\n
                    - Remote device control and management\n
                    - IMPORTANT: If there are multiple keywords, use different IDs to distinguish them.\n
                    
                    
                    ## FOR Device Create Task
                    The device creation task is a special task that is mainly processed in three steps:\n
                     1. Confirm whether the relevant device is mentioned (such as being in the same product as XXX device).\n
                     2. If the relevant device is mentioned, the task will be considered as one of the tasks for XXX device.\n 
                     3. If not mentioned, the specific device Name and productKey need to be found before creating the device.\n
                    - IMPORTANT: For newly created device tasks, these newly created device names cannot be used as keywords.\n
                    - IMPORTANT: If the device creation task mentions related devices, it will be treated as a task for related devices. The relevant devices will provide corresponding functions and create new devices. At this point, this task will be one of the tasks for the relevant devices.\n
                    - IMPORTANT: If the device creation task mentions related devices, it will be treated as a task for related devices. The relevant devices will provide corresponding functions and create new devices. At this point, this task will be one of the tasks for the relevant devices.\n
                    - IMPORTANT: If the device creation task mentions related devices, it will be treated as a task for related devices. The relevant devices will provide corresponding functions and create new devices. At this point, this task will be one of the tasks for the relevant devices.\n
                    - IMPORTANT: If the task is create device, the Name of device to be created must be add in task. such as: the Name of device to be created is XXXXX\n
                 
                    
                    - IMPORTANT: Each action must contain a keywords and Specific actions according to  << COMMAND >> . For multiple actions, use 1., 2., 3... Describe by points\n
    
                    
                    ## The Second Task: you need to extract the corresponding action for each keyword in << User Input >>.\n
                    - IMPORTANT: The action must include the keyWordName, keyword and all actions corresponding to the keyword, preferably using the exact words in << User Input >>.\n
                    - IMPORTANT: The action content referred to needs to be clearly displayed. When mentioning a product, there should be a product name, and when mentioning a device, there should be a device name.\n\n
                   
                    ## IMPORTANT
                    IMPORTANT: Use detailed, professional language and logical reasoning to connect the user’s vague command to that specific intent.\n
                    Attention: Ensure each intention is distinct, practical, and clearly described.\n
                    Attention: Avoid vague or redundant phrasing.\n
                    Caution: Keep the user’s perspective in mind and do not stray beyond what their command plausibly means.\n
                    Caution: Cannot Skip any Command!\n
                    Caution: Cannot Skip any Command!\n
                    Caution: Cannot Skip any Command!\n
                    
                    Emphasize that the goal is to help the user discover the software’s capabilities more precisely and effectively.\n\n
    
                    << User Input >>\n
                    {command}\n\n
                    
                    <<KeyWord List>>\n
                    {KeyWord_list}\n\n
    
                    << Output Format >>\n
                    {json_output}\n\n
                """
        )

        self.json_output = """
            Return a markdown code snippet with JSON object formatted as follows:\n
            ```json\n
            {
                "total": int, // the number of results\n
                "results": [\n
                    {
                        "id": 1, // the first KeyWord,\n
                        "keyWordName": string // the name of the first KeyWord in <<KeyWord List>>\n
                        "KeyWord": string,  \n
                        "action": string 1. 2. 3. // the corresponding action for the first keyword in << User Input >>.\
                    },
                    {
                        "id": 2, // the second KeyWord\n
                        "keyWordName": string // the type of the second KeyWord in <<KeyWord List>>\n
                        "KeyWord": string,  \n
                        "action": string 1. 2. 3.  // the corresponding action for the second keyword in << User Input >>\
                    },\n
                    ...\n
                ]\n
            }\n
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

    @staticmethod
    def get_token():
        url = f"{BASE_URL}/openapi/v1/getToken"
        headers = {"Content-Type": "application/json"}

        payload = {
            "requestId": "13",
            "data": {
                "appid": "admin",
                "password": "123456",
                "identifier": "fd4b1aacdf9a0b334c4b3f616812bb12",
                "timestamp": "20240901",
                "tenantId": "452748015218757"
            }
        }

        try:
            response = requests.post(url, json=payload, headers=headers, timeout=10)
            response.raise_for_status()
            data = response.json()
            print("✅ getToken 返回:", data)

            # 这里根据实际返回的 JSON 结构提取 token
            token = data.get("data", {}).get("requestId")
            print("✅ 解析出的 token:", token)
            return token
        except requests.RequestException as e:
            print(f"❌ 获取 token 失败: {e}")
            return None
    def select_keywords(self, command):


        history = []
        is_first = True
        for i in range(3):
            think, answer, history = self.llm.multi_chat(self.prompt_template.format(command=command, KeyWord_list=self.keyWords_list, json_output=self.json_output), history, is_first)
            is_first = False
            self.think = think
            self.answer = answer
            ans = self.write_to_json(answer)
            keyword_map = {item["keyWordName"]: item["KeyWord"] for item in ans}
            deviceName = keyword_map.get("deviceName")
            productKey = keyword_map.get("productKey")
            self.ans = ans
            token = self.get_token()
            if ((deviceName == "null" or deviceName == "None" or deviceName is None or deviceName == "" or deviceName == "NULL" or DeviceTool.check_deviceName(deviceName, token)) and
                (productKey == "null" or productKey == "None" or productKey is None or productKey == "" or productKey == "NULL" or ProductTool.check_productKey(productKey))):
                break
            if not DeviceTool.check_deviceName(deviceName, token):
                history.append({'role': 'user', 'content': "注意，上一次回答是:\n" + answer + "\n, 其中deviceName回答不正确,系统中无此名称设备，请按照要求，重新解析<< User Input >>！"})
            if not ProductTool.check_productKey(productKey):
                history.append({'role': 'user', 'content': "注意，上一次回答是:\n" + answer + "\n, 其中productKey回答不正确，系统中无此名称产品，请按照要求，重新解析<< User Input >>！"})
        return self.think, self.answer, self.ans




