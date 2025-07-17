import csv
import re
import os

from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_ollama import OllamaLLM
from transformers import MarianMTModel, MarianTokenizer


class CommandC2E:

    prompt_template = PromptTemplate(
        input_variables=["translate_command", "json_output", "english_key_words", "chinese_key_words"],
        template="""
            You are an experienced IoT system expert. Users of the IoT control software often issue vague or ambiguous commands. Your task is to analyze each command and identify 10 possible user intentions.
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

    file_name = "./tmp/commands.csv"

    # Write to CSV
    def write_to_csv(self, file_name, translate_command, original_command):
        with open(file_name, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)

            # Write the header (optional)
            writer.writerow(["Translated Command", "Original Command"])


            writer.writerow([translate_command, original_command])


    def translate_command(self, command):
        if os.path.exists(self.file_name):
            os.remove(self.file_name)

        original_command = "用户提问:" + command
        src_text = []
        src_text.append(original_command)

        tokenizer = MarianTokenizer.from_pretrained(self.translate_model_name)
        translate_model = MarianMTModel.from_pretrained(self.translate_model_name)

        translated = translate_model.generate(**tokenizer(src_text, return_tensors="pt", padding=True))
        translate_command = [tokenizer.decode(t, skip_special_tokens=True) for t in translated][0].split(":")[1]
        print(translate_command)



        self.write_to_csv(self.file_name, translate_command, original_command)

        print(f"Commands have been written to {self.file_name}")

if __name__ == "__main__":
    commandC2E = CommandC2E()
    commandC2E.translate_command("帮我将设备MS-INS-010的温度调成-1")
