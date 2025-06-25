import csv
import re
import os

from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_ollama import OllamaLLM
from transformers import MarianMTModel, MarianTokenizer



prompt_template = PromptTemplate(
    input_variables=["translate_command", "json_output"],
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

llm = OllamaLLM(model="deepseek-r1:1.5b", base_url="http://localhost:11434", temperature=1.0)
llm_chain = LLMChain(prompt=prompt_template, llm=llm)

translate_model_name = "Helsinki-NLP/opus-mt-zh-en"
tokenizer = MarianTokenizer.from_pretrained(translate_model_name)
translate_model = MarianMTModel.from_pretrained(translate_model_name)

# Write to CSV
def write_to_csv(file_name, matches, translate_command, original_command):
    with open(file_name, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        # Write the header (optional)
        writer.writerow(["Rewritten Command", "Translated Command", "Original Command"])

        for rewritten_command in matches:
            writer.writerow([rewritten_command, translate_command, original_command])

file_name = "commands.csv"
def translate_command(command):
    if os.path.exists(file_name):
        os.remove(file_name)

    original_command = "用户提问:" + command
    src_text = []
    src_text.append(original_command)
    translated = translate_model.generate(**tokenizer(src_text, return_tensors="pt", padding=True))
    translate_command = [tokenizer.decode(t, skip_special_tokens=True) for t in translated][0].split(":")[1]
    print(translate_command)


    # 获取重写后的指令
    rewritten_command = llm_chain.run({"translate_command": translate_command, "json_output": json_output})
    rewritten_command = rewritten_command.split("</think>")[1]

    print(f"重写后的指令：{rewritten_command}")
    # 使用正则表达式提取 "user intent" 内容
    pattern = r'"user intent"\s*:\s*"([^"]+)"'
    matches = re.findall(pattern, rewritten_command)

    write_to_csv(file_name, matches, translate_command, original_command)

    print(f"Commands have been written to {file_name}")



