import concurrent
import csv
import json
import re
import os

from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_ollama import OllamaLLM
from transformers import MarianMTModel, MarianTokenizer


class Command_Refine:
    prompt_template = PromptTemplate(
        input_variables=["translate_command", "json_output", "english_key_words", "chinese_key_words"],
        template="""
            You are an experienced IoT system expert. Users of the IoT control software often issue vague or ambiguous commands. The <<English Key Words>> and <<Chinese Key Words>> are summaries of user instructions compiled by another IoT expert. Your task is to analyze each command and identify 10 possible user intentions.
            Focus on realistic and typical IoT scenarios, such as:
            - Smart home automation (e.g., controlling lights, thermostat, appliances)
            - Device scheduling (timers and routines)
            - Energy efficiency and management
            - Security monitoring (e.g., cameras, alarms)
            - Sensor integration and data monitoring
            - Remote device control and management

            For each of the 10 intentions:
            IMPORTANT: Use detailed, professional language and logical reasoning to connect the user’s vague command to that specific intent.
            Attention: Ensure each intention is distinct, practical, and clearly described.
            Attention: Avoid vague or redundant phrasing.
            Caution: Keep the user’s perspective in mind and do not stray beyond what their command plausibly means.

            Emphasize that the goal is to help the user discover the software’s capabilities more precisely and effectively.

            << User Input >>
            {translate_command}

            <<English Key Words>>
            {english_key_words}

            <<Chinese Key Words>>
            {chinese_key_words}

            << Output Format >>
            {json_output}

            Important: Each of the 10 identified intentions should be independent and unrelated to each other.
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
                "id": 1, // the first user intent
                "user intent": string,  // the user intent
            },
            {
                "id": 2, // the second user intent
                "user intent": string,  // the user intent
            },
            ...
        ]
    }
    ```
    REMEMBER: "total" MUST be 10 and MUST be consistent with the number in the json list,
    REMEMBER: "user intent" MUST be based on << User Input >>
    """

    llm = OllamaLLM(model="deepseek-r1:14b", base_url="http://localhost:11434", temperature=1.0)
    llm_chain = LLMChain(prompt=prompt_template, llm=llm)

    translate_model_name = "Helsinki-NLP/opus-mt-zh-en"

    file_name = "./tmp/refine_commands.csv"

    # Write to CSV
    def write_to_csv(self, file_name, matches, translate_command, original_command):
        with open(file_name, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)

            # Write the header (optional)
            writer.writerow(["Rewritten Command", "Translated Command", "Original Command"])

            for rewritten_command in matches:
                writer.writerow([rewritten_command, translate_command, original_command])
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
    def refine_command(self):
        file_name = "./tmp/commands.csv"

        # 并发读取 CSV 两列
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future_translated = executor.submit(self.read_column, file_name, "Translated Command")
            future_original = executor.submit(self.read_column, file_name, "Original Command")
            Translated_Command = future_translated.result()
            Original_Command = future_original.result()

        with open('./tmp/chinese_keyWords.json', 'r', encoding='utf-8') as file:
            data = json.load(file)


        chinese_key_words = ", ".join(f"{item['keyWordName']}={item['KeyWord']}" for item in data)

        with open('./tmp/english_keyWords.json', 'r', encoding='utf-8') as file:
            data = json.load(file)


        english_key_words = ", ".join(f"{item['keyWordName']}={item['KeyWord']}" for item in data)

        # 获取重写后的指令
        rewritten_command = self.llm_chain.run(
            {"translate_command": Translated_Command, "json_output": self.json_output, "english_key_words": english_key_words, "chinese_key_words": chinese_key_words})
        rewritten_command = rewritten_command.split("</think>")[1]

        print(f"重写后的指令：{rewritten_command}")
        # 使用正则表达式提取 "user intent" 内容
        pattern = r'"user intent"\s*:\s*"([^"]+)"'
        matches = re.findall(pattern, rewritten_command)


        self.write_to_csv(self.file_name, matches, Translated_Command, Original_Command)

        print(f"Commands have been written to {self.file_name}")


if __name__ == "__main__":
    command_Refine = Command_Refine()
    command_Refine.refine_command()

