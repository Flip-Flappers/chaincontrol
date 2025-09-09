import ast
import json
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
from langchain_core.prompts import PromptTemplate
BASE_URL = "http://localhost:8086"

class DeviceTool:
    def __init__(self, keywords, deviceName):
        self.think = None
        self.answer = None
        self.ans =  None
        self.deviceName = deviceName
        self.devicePluginName = None
        self.keywords = keywords
        self.llm = deepseek()
        self.token = self.get_token()
        self.toolTable = [
            {
                "toolName": "Device Control Tool",
                "function": "this tool can Control the target device. such as \n"
                            "1.call the device API to send data to the device.\n"
                            "2.retrieve properties from the device.\n"
                            "3.let the device complete specified operations.\n"
                            "The functions of this device include:\n" + self.get_deviceAPIS(deviceName, self.token)[0]
            },
            {
                "toolName": "View Device Property Tool",
                "function": "this tool can Retrieve history properties reported by the device.\n"
                            "These properties are not immediately obtained from the device, but are obtained from the IOT system.\n"
                            "NOTE: If 'Device Control tool' does not support actively retrieving properties, then 'View Device Property Tool' can get the latest property. Otherwise, the latest properties should be obtained through the 'Device Control Tool'"
            },
            {
                "toolName": "View Device Alert Tool",
                "function": "this tool can Retrieve history alerts reported by the device.\n"
                            "These alerts are not immediately obtained from the device, but are obtained from the IOT system.\n"
            },
            {
                "toolName": "View Device Status Tool",
                "function": "this tool can Show the status of the device.\n"
            },
            {
                "toolName": "Modify Device properties Tool",
                "function": "this tool can Modify device properties, which 'Device Control Tool' does not support.\n"
            },
            {
                "toolName": "View Device Detail Tool",
                "function": "this tool can Show the Basic information about the device."
            }
        ]
        self.file_name = "./tmp/device_tool.json"

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

    @staticmethod
    def getDeviceDetailByName(deviceName):
        result = """
        {
            "createDept": null,
            "createBy": 1,
            "createTime": 1745896620000,
            "updateBy": 1,
            "updateTime": 1745896620000,
            "tenantId": 0,
            "id": 1,
            "productKey": "openiotgateway01",
            "productSecret": "openiotsecret01",
            "name": "iot智联智能网关01",
            "category": "OpeniotGateway",
            "nodeType": 0,
            "uid": "1",
            "img": null,
            "iconId": null,
            "transparent": false,
            "isOpenLocate": true,
            "locateUpdateType": "manual",
            "keepAliveTime": null,
            "createAt": 1649653149339,
            "deviceInfoList": [
                {
                    "createDept": null,
                    "createBy": 1,
                    "createTime": 1745896620000,
                    "updateBy": 1,
                    "updateTime": 1745897273000,
                    "tenantId": 0,
                    "id": "16891443313530testgateway0100013d",
                    "deviceId": "16891443313530testgateway0100013d",
                    "productKey": "openiotgateway01",
                    "deviceName": "4FBF58B2B0FF969A",
                    "deviceSecondName": null,
                    "model": null,
                    "secret": "bnw2Z6zNxxdBtm6N",
                    "parentId": null,
                    "uid": "1",
                    "subUid": [],
                    "locate": {
                        "longitude": null,
                        "latitude": null
                    },
                    "state": {
                        "online": false,
                        "onlineTime": null,
                        "offlineTime": null
                    },
                    "property": {},
                    "tag": {},
                    "group": {},
                    "createAt": 1689144331356,
                    "online": false
                }
            ]
        }"""
        data = json.loads(result)
        return data
    @staticmethod
    def check_deviceName(device_name, token):
        url = f"{BASE_URL}/device/getDeviceDetailByDeviceName"
        headers = {
            "Content-Type": "application/json",
            "token": f"{token}"  # 一般是这样传，具体要看你后端要求
        }
        payload = {
            "data": {
                "deviceName": device_name,
                "productKey": "None"
            },
            "requestId": 45
        }

        try:
            response = requests.post(url, json=payload, headers=headers, timeout=10)
            response.raise_for_status()
            device_info = response.json()
            print("✅ 查询成功，返回：", device_info)
            if device_info.get("data") is None:
                return False
            return True
        except requests.RequestException as e:
            print(f"❌ 查询失败: {e}")
            return False


    @staticmethod
    def getProductKeyByDeviceName(deviceName, token):

        url = f"{BASE_URL}/device/getDeviceDetailByDeviceName"
        headers = {
            "Content-Type": "application/json",
            "token": f"{token}"  # 一般是这样传，具体要看你后端要求
        }
        payload = {
            "data": {
                "deviceName": deviceName,
                "productKey": "None"
            },
            "requestId": 45
        }
        try:
            response = requests.post(url, json=payload, headers=headers, timeout=10)
            response.raise_for_status()
            device_info = response.json()
            print("✅ 查询成功，返回：", device_info)
            if device_info.get("data") is None:
                return None
            return device_info.get("data").get("productKey")
        except requests.RequestException as e:
            print(f"❌ 查询失败: {e}")
            return None


    def get_deviceAPIS(self, deviceName, token):
        url = f"{BASE_URL}/plugin/getPluginDetailByDeviceName"
        headers = {
            "Content-Type": "application/json",
            "token": f"{token}"  # 一般是这样传，具体要看你后端要求
        }
        payload = {
            "data": deviceName,
            "requestId": 45
        }
        try:
            response = requests.post(url, json=payload, headers=headers, timeout=10)
            response.raise_for_status()
            plugin_info = response.json()
            print("✅ 查询成功，返回：", plugin_info)
            if plugin_info.get("data") is None:
                return None
            self.devicePluginName = plugin_info.get("data").get("pluginId")
        except requests.RequestException as e:
            print(f"❌ 查询失败: {e}")
            return None

        url = f"{BASE_URL}/{self.devicePluginName}"
        headers = {
            "Content-Type": "application/json",
            "token": f"{token}"  # 一般是这样传，具体要看你后端要求
        }
        try:
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            device_api_info = response.json()
            print("✅ 查询成功，返回：", device_api_info)
            if device_api_info.get("data") is None:
                return None
            return str(device_api_info.get("data")), device_api_info.get("data")
        except requests.RequestException as e:
            print(f"❌ 查询失败: {e}")
            return None




    def getTargetApiBody(self, deviceName, apiName, token):
        url = f"{BASE_URL}/{self.devicePluginName}/search"
        headers = {
            "Content-Type": "application/json",
            "token": f"{token}"  # 一般是这样传，具体要看你后端要求
        }
        payload = {
            "data": apiName,
            "requestId": 45
        }
        try:
            response = requests.post(url, json=payload, headers=headers, timeout=10)
            response.raise_for_status()
            api_info = response.json()
            print("✅ 查询成功，返回：", api_info)
            if api_info.get("data") is None:
                return None
            return api_info.get("data").get("body")
        except requests.RequestException as e:
            print(f"❌ 查询失败: {e}")
            return None


    def getTargetBody(self, deviceName, targetAPI, command, current_task):
        API_prompt_template = PromptTemplate(
            input_variables=["command", "KeyWords", "API BODY", "current_task", "json_output"],
            template="""
                            You are an experienced IoT system expert. Users of the IoT control software often issue vague or ambiguous commands.\n
                            Your task is to Fill the corresponding information in the << COMMAND >> into the specified format of JSON in << API BODY >>.\n
                            The user's command may involve multiple instructions, as long as you combine the << CURRENT TASK >> to be done with the << COMMAND >>.\n
                    
                            IMPORTANT: Just need to complete the content in << CURRENT TASK >>
                
                            Your work assistant has extracted the keywords from the user command and stored them in << API BODY >>.\n
                            Please provide << API BODY>> that matches the << COMMAND >>

                            Caution: Keep the user’s << COMMAND >> in mind and do not stray beyond what their command plausibly means.\n
                            IMPORTANT: MUST Strictly follow the << Output Format >> for output\n
                            IMPORTANT: Cannot change, reduce or add 'json keys' in << API BODY >>, strictly follow the type of 'json keys' in << API BODY >>.\n\n
                            
                            << CURRENT TASK >> \n
                            {current_task}\n\n

                            << COMMAND >>\n
                            {command}\n\n

                            << KeyWords >>\n
                            {KeyWords}\n\n

                            << API BODY >>\n
                            {APIBODY}\n\n

                            << Output Format >>\n
                            {APIBODY}\n
                            {json_output}\n
                        """
        )

        API_json_output = """
                            Return a markdown code snippet with JSON object formatted as follows:\n
                            REMEMBER: the output MUST be based on << COMMAND >>\n
                            REMEMBER: the output format must be consistent with << APIBODY >>\n
                            REMEMBER: If the content is unclear, null will be filled in by default.\n
                """

        history = []
        is_first = True

        think, answer, history = self.llm.multi_chat(
            API_prompt_template.format(command=command, KeyWords=self.keywords, APIBODY=targetAPI, current_task=current_task,
                                       json_output=API_json_output), history, is_first)
        ans = self.write_to_json(answer, "./tmp/api_targetbody.json")

        return ans

    def remove_star_keys(self, data):
        """
        递归删除所有以 ** 开头的 JSON key
        """
        if isinstance(data, dict):
            return {
                k: self.remove_star_keys(v)
                for k, v in data.items()
                if not k.startswith("**")
            }
        elif isinstance(data, list):
            return [self.remove_star_keys(item) for item in data]
        else:
            return data
    def intention_recognition(self, command):
        self.prompt_template = PromptTemplate(
            input_variables=["command", "KeyWords", "toolTable", "json_output"],
            template="""
                    You are an experienced IoT system expert. Users of the IoT control software often issue vague or ambiguous commands.\n
                    Your task is to choose the appropriate tool to implement user commands.\n
                    IMPORTANT: You can choose to use multiple tools, and the system will execute all tools step by step according to the steps you choose.\n
                    IMPORTANT: If the << COMMAND >> involves multiple operations, it needs to correspond to multiple tools, each operation corresponds to a tool.\n
                    IMPORTANT: Different steps can use the same tool.\n
                    
                    Your work assistant has extracted the keywords from the user command and stored them in << KeyWords >>.\n
                    Please carefully analyze the << function >> of each tool in the << tooltable >>.\n

                    Caution: Keep the user’s << COMMAND >> in mind and do not stray beyond what their command plausibly means.\n
                    IMPORTANT: The output toolName must correspond one-to-one with the << tooltable >>.\n
                    IMPORTANT: Cannot fabricate toolName that are not in the << tooltable >>\n
                    IMPORTANT: Strictly follow the << Output Format >> for output\n
                    IMPORTANT: The << reason >> in the output should be detailed and practical. Highly correlated with  << COMMAND >>,  << KeyWords >> and << toolTable >>\n\n

                    << COMMAND >>
                    {command}\n\n

                    << KeyWords >>
                    {KeyWords}\n\n

                    << toolTable >>
                    {toolTable}\n\n

                    << Output Format >>
                    {json_output}\n\n
                """
        )

        self.json_output = """
                    Return a markdown code snippet with JSON object formatted as follows:\n
                    ```json\n
                    {\n
                        "steps": int, // Total number of steps. \n
                        "results": [\n
                        {\n
                            "step_num": 1,
                            "toolName": string, // Selected toolName of the first step.\n
                            "reason": string // Reasons for choosing the target tool of the first step.\n
                        },\n
                        {\n
                            "step_num": 2,
                            "toolName": string, // Selected toolName of the second step.\n
                            "reason": string // Reasons for choosing the target tool of the second step.\n
                        }\n
                        ]\n
                    }\n
                    ```
                    REMEMBER: "toolName" MUST be based on << COMMAND >>\n
                    REMEMBER: "toolName" Must be consistent with << toolTable >>\n
                    REMEMBER: If there is no corresponding tool, toolName defaults to null.\n
                    """

        history = []
        is_first = True

        think, answer, history = self.llm.multi_chat(
            self.prompt_template.format(command=command, KeyWords=self.keywords, toolTable=self.toolTable,
                                        json_output=self.json_output), history, is_first)

        self.think = think
        self.answer = answer
        ans = self.write_to_json(answer, self.file_name)
        self.ans = ans




        for i in range(len(ans["results"])):
            if ans["results"][i]["toolName"] == "Device Control Tool":
                API_Detail, target_apis= self.get_deviceAPIS(self.deviceName, self.token)
                target_API = self.getTargetApi(API_Detail, command, ans["results"][i]['reason'])
                targetAPIName = target_API.get("targetAPIName")
                target_url = ""
                for api in target_apis:
                    if targetAPIName == api.get("apiName"):
                        target_url = api.get("url")
                        break
                print("target_API:")
                print(target_API)
                body = self.getTargetBody(self.deviceName, self.getTargetApiBody(self.deviceName, target_API["targetAPIName"], self.token),  command, ans["results"][i]['reason'])
                print("old_body: ")
                print(body)
                body = self.remove_star_keys(body)
                print("target_body:")
                print(body)
                url = f"http://localhost:8078{target_url}"
                print("url:{}", url)
                headers = {
                    "Content-Type": "application/json",
                    "token": f"{self.token}"  # 一般是这样传，具体要看你后端要求
                }
                payload = body
                response = requests.post(url, json=payload, headers=headers, timeout=10)
                response.raise_for_status()
                api_info = response.json()
                print("✅ 调用成功：", api_info)






        return self.think, self.answer, self.ans

    def getTargetApi(self, API_Detail, command, current_task):
        API_prompt_template = PromptTemplate(
            input_variables=["command", "KeyWords", "APItable", "json_output", "current_task"],
            template="""
                    You are an experienced IoT system expert. Users of the IoT control software often issue vague or ambiguous commands.\n
                    Your task is to choose the appropriate API to implement user commands.\n
                    The user's command may involve multiple instructions, as long as you combine the << CURRENT TASK >> to be done with the << COMMAND >>.\n
                    The 'body' in << APItable >> contains the format of API calls.\n
                    
                    IMPORTANT: You can only choose one API.\n
                    IMPORTANT: Just need to complete the content in << CURRENT TASK >>

                    Your work assistant has extracted the keywords from the user command and stored them in << KeyWords >>.\n
                    Please carefully analyze the << description >> of each API in the << APItable >>.\n

                    Caution: Keep the user’s << COMMAND >> in mind and do not stray beyond what their command plausibly means.\n
                    IMPORTANT: The output ApiName must correspond one-to-one with the << APItable >>.\n
                    IMPORTANT: Cannot fabricate ApiName that are not in the << APItable >>\n
                    IMPORTANT: Strictly follow the << Output Format >> for output\n
                    IMPORTANT: The << reason >> in the output should be detailed and practical. Highly correlated with  << COMMAND >>,  << KeyWords >> and << APItable >>\n\n

                    << CURRENT TASK >> 
                    {current_task}\n\n
                    
                    << COMMAND >>
                    {command}\n\n

                    << KeyWords >>
                    {KeyWords}\n\n

                    << APItable >>
                    {APItable}\n\n

                    << Output Format >>
                    {json_output}\n\n
                """
        )

        API_json_output = """
                    Return a markdown code snippet with JSON object formatted as follows:\n
                    ```json\n
                    {\n
                        "targetAPIName": String, // targetAPI name. \n
                        "reason": string // Reasons for choosing the target tool of the second step.\n
                    }\n
                    ```
                    REMEMBER: "targetAPIName" MUST be based on << COMMAND >>\n
                    REMEMBER: "targetAPIName" Must be consistent with << APItable >>\n
                    REMEMBER: If there is no corresponding tool, targetAPIName defaults to null.\n
        """

        history = []
        is_first = True

        think, answer, history = self.llm.multi_chat(
            API_prompt_template.format(command=command, KeyWords=self.keywords, APItable=API_Detail,
                                        json_output=API_json_output, current_task=current_task), history, is_first)
        ans = self.write_to_json(answer, "./tmp/api_selector.json")

        return ans


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
            print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
            print(json_str)
            return json.loads(self.clean_json_string_with_regex(json_str))  # 返回 dict，可改成 return json_str 返回字符串
        else:
            raise ValueError("未找到完整的 JSON 对象")

    # Write to CSV
    def write_to_json(self, json_str, file_name):
        try:
            data = self.extract_json(json_str)
            # 删除旧文件（如果存在）
            if os.path.exists(file_name):
                os.remove(file_name)
            print("*********************************************************")
            print(data)
            # 写入 JSON 文件
            with open(file_name, mode="w", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=2)

        except json.JSONDecodeError as e:
            print(f"解析 JSON 字符串失败: {e}")
        except Exception as e:
            print(f"写入 JSON 文件时出错: {e}")
        return data








