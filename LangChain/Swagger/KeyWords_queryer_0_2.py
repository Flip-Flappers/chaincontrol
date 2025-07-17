import concurrent
import csv
import json
import re
import os
import uuid

import requests
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_ollama import OllamaLLM
from transformers import MarianMTModel, MarianTokenizer


class Command_Refine:
    def __init__(self):
        self.base_url = "http://localhost:8086"

    def get_token(self):
        token_url = f"{self.base_url}/openapi/v1/getToken"
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
            response = requests.post(token_url, json=payload)
            response.raise_for_status()
            res_json = response.json()
            # 假设 token 在 res_json["data"]["token"] 中
            self.token = res_json.get("data", {}).get("requestId")
            if not self.token:
                raise ValueError("Token not found in response")
            print("Token 获取成功:", self.token)
        except requests.RequestException as e:
            print("获取 Token 出错:", e)
        except ValueError as ve:
            print("解析 Token 出错:", ve)

    def _post_with_token(self, url, payload):
        headers = {
            "token": f"{self.token}"  # 按需调整前缀
        }
        try:
            response = requests.post(url, json=payload, headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"请求失败: {e}")
            return None
    def getDeviceDetail(self, deviceName):
        url = f"{self.base_url}/device/getDeviceDetailByDeviceName"
        payload = {
            "requestId": str(uuid.uuid4()),  # 生成唯一请求 ID
            "data": deviceName
        }
        try:
            response = self._post_with_token(url, payload=payload)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error getting device detail: {e}")
            return None

    def get_thingModel(self, deviceId):
        url = f"{self.base_url}/device/getThingModel"
        payload = {
            "requestId": str(uuid.uuid4()),  # 生成唯一请求 ID
            "data": {
                "deviceId": deviceId
            }
        }
        try:
            response = self._post_with_token(url, payload=payload)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error getting thing model: {e}")
            return None

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
    def main(self):
        file_name = "./tmp/commands.csv"

        # 并发读取 CSV 两列
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future_translated = executor.submit(self.read_column, file_name, "Translated Command")
            future_original = executor.submit(self.read_column, file_name, "Original Command")
            Translated_Command = future_translated.result()
            Original_Command = future_original.result()

        with open('./tmp/chinese_keyWords.json', 'r', encoding='utf-8') as file:
            chinese_data = json.load(file)


        with open('./tmp/english_keyWords.json', 'r', encoding='utf-8') as file:
            english_data = json.load(file)
        self.get_token()
        deviceName = "null"
        for keyword in chinese_data:
            if keyword['keyWordName'] == "deviceName":
                deviceName = keyword["KeyWord"]

        deviceDetail = self.getDeviceDetail(deviceName)


        thingModel = self.get_thingModel(deviceName)









if __name__ == "__main__":
    commandC2E = Command_Refine()
    commandC2E.main()
