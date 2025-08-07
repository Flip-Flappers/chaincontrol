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

from LangChain.Swagger.model.deepseek import deepseek
from LangChain.Swagger.tools.DeviceTool import DeviceTool
from LangChain.Swagger.tools.ProductTool import ProductTool



class ToolSelector:

    def __init__(self, keywords: object) -> None:
        self.think = None
        self.answer = None
        self.ans = None
        self.keywords = keywords
        self.file_name = "./tmp/tool_selector.json"
        self.toolTable = [
            {
                "toolName": "DeviceTool",
                "function": "1. Query and manage information of specified devices through << deviceName >>. \n"
                              "2. Issue commands to specified devices through << deviceName >> to achieve device control. \n"
                              "3. Use the << deviceName >> to query the historical attributes reported by the device.\n"
                              "4. Obtain device alerts by << deviceName >>.\n"
                              "5. Check the device status by << deviceName >>.\n"
                              "6. The correct deviceName is required as tool_input.\n",
            },
            {
                "toolName": "productTool",
                "function": "1. Manage and query product information through << ProductKey >>.\n"
                               "2. Obtain the corresponding configuration of the product through the << ProductKey >>.\n"
                               "3. Batch control all devices under the product through the << ProductKey >>.\n"
                               "4. Modify the corresponding configuration of the product through the << ProductKey >>.\n"
                               "5. The correct productKey is required as tool_input."
            },
            {
                "toolName": "LocalSystemTool",
                "function": "Not interacting with the device, but only interacting with the IoT software platform itself.\n"
                            "This tool calling the API of the IoT software itself to achieve addition, deletion, modification, and query for the IoT software platform.\n"
            }
        ]

        self.prompt_template = PromptTemplate(
            input_variables=["command", "KeyWords", "toolTable", "json_output"],
            template="""
                    You are an experienced IoT system expert. Users of the IoT control software often issue vague or ambiguous commands.\n
                    Your task is to choose the appropriate tool to implement user commands. IMPORTANT: You can only choose ONE tool.\n
                    Your work assistant has extracted the keywords from the user command and stored them in << KeyWords >>.\n
                    Please carefully analyze the << function >> of each tool in the << tooltable >>.\n
                    
                    Caution: Keep the user’s << COMMAND >> in mind and do not stray beyond what their command plausibly means.\n
                    IMPORTANT: The output toolName must correspond one-to-one with the << tooltable >>.\n
                    IMPORTANT: Cannot fabricate toolName that are not in the << tooltable >>.\n
                    IMPORTANT: Strictly follow the << Output Format >> for output.\n
                    IMPORTANT: The << reason >> in the output should be detailed and practical. Highly correlated with  << COMMAND >>,  << KeyWords >> and << toolTable >>\n\n
                    
                    << COMMAND >>\n
                    {command}\n\n

                    << KeyWords >>\n
                    {KeyWords}\n\n
                    
                    << toolTable >>\n
                    {toolTable}\n\n

                    << Output Format >>\n
                    {json_output}\n\n
                """
        )

        self.json_output = """
            Return a markdown code snippet with JSON object formatted as follows:\n
            ```json\n
            {\n
              
                "toolName": string, // Selected toolName\n
                "reason": string // Reasons for choosing the target tool\n
            }\n
            ```\n
            REMEMBER: "toolName" MUST be based on << COMMAND >>\n
            REMEMBER: "toolName" Must be consistent with << toolTable >>\n
            REMEMBER: If there is no corresponding tool, toolName defaults to null.\n
            """
        self.llm = deepseek()

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

            # 删除旧文件（如果存在）
            if os.path.exists(self.file_name):
                os.remove(self.file_name)

            # 写入 JSON 文件
            with open(self.file_name, mode="w", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=2)

        except json.JSONDecodeError as e:
            print(f"解析 JSON 字符串失败: {e}")
        except Exception as e:
            print(f"写入 JSON 文件时出错: {e}")
        return data

    def select_tool(self, command):

        history = []
        is_first = True

        think, answer, history = self.llm.multi_chat(
            self.prompt_template.format(command=command, KeyWords=self.keywords, toolTable=self.toolTable,
                                        json_output=self.json_output), history, is_first)

        self.think = think
        self.answer = answer
        ans = self.write_to_json(answer)
        self.ans = ans
        return self.think, self.answer, self.ans




