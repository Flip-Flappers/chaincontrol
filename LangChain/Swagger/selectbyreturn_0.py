import csv
import re

from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_ollama import OllamaLLM

# 创建一个指令重写模板
from transformers import MarianMTModel, MarianTokenizer

original_command = "用户提问:帮我重启设备123。"
src_text = []
src_text.append(original_command)
model_name = "Helsinki-NLP/opus-mt-zh-en"
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)
translated = model.generate(**tokenizer(src_text, return_tensors="pt", padding=True))
translate_command = [tokenizer.decode(t, skip_special_tokens=True) for t in translated][0].split(":")[1]
print(translate_command)






# 创建一个指令重写模板
prompt_template = PromptTemplate(
    input_variables=["translate_command", "json_output"],
    template="""
        You are an experienced IoT system expert. Currently, users are not familiar with your IoT software and can only issue vague commands. 
        Please analyze the 10 possible user intentions based on their input to assist them in better utilizing the IoT control software. Users will explore the IoT software more accurately based on your explanation.

        << User Input >>
        {translate_command}

        << FORMATTING >>
        {json_output}

        IMPORTANT: The 10 identified intentions are independent and unrelated to each other.
        Attention: Each intention should be as detailed as possible.
        Attention: Each intention should be reasonable, professional, and logical.
        Caution: Consider from the user's perspective and do not deviate from their intention.
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


# 创建LLMChain时需要传入prompt参数
llm_chain = LLMChain(prompt=prompt_template, llm=llm)  # 注意这里改为prompt_template



# 获取重写后的指令
rewritten_command = llm_chain.run({"translate_command": translate_command, "json_output": json_output})
rewritten_command = rewritten_command.split("</think>")[1]

print(f"重写后的指令：{rewritten_command}")
# 使用正则表达式提取 "user intent" 内容
pattern = r'"user intent"\s*:\s*"([^"]+)"'
matches = re.findall(pattern, rewritten_command)


file_name = "commands.csv"

# Write to CSV
with open(file_name, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    # Write the header (optional)
    writer.writerow(["Rewritten Command", "Translated Command", "Original Command"])

    for rewritten_command in matches:




        writer.writerow([rewritten_command, translate_command, original_command])

print(f"Commands have been written to {file_name}")