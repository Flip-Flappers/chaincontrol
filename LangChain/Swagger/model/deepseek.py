import os
from openai import OpenAI








class deepseek:

    def __init__(self):

        self.client = OpenAI(
            api_key=os.getenv("DASHSCOPE_API_KEY"),
            base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
        )
        self.model = "deepseek-r1-0528"



    def single_chat(self, content):
        completion = self.client.chat.completions.create(
            model = self.model,  # 此处以 deepseek-r1 为例，可按需更换模型名称。
            messages=[
                {'role': 'user', 'content': content}
            ]
        )

        # 通过reasoning_content字段打印思考过程
        print("思考过程：")
        print(completion.choices[0].message.reasoning_content)

        # 通过content字段打印最终答案
        print("最终答案：")
        print(completion.choices[0].message.content)

        think = completion.choices[0].message.reasoning_content

        answer = completion.choices[0].message.content


        return think, answer

    def multi_chat(self, content, history, is_first):
        if is_first:
            history.append({'role': 'user', 'content': content})
        completion = self.client.chat.completions.create(model=self.model, messages=history)
        think = completion.choices[0].message.reasoning_content
        answer = completion.choices[0].message.content
        history.append({'role': 'assistant', 'content': answer})

        # 通过reasoning_content字段打印思考过程
        print("思考过程：")
        print(completion.choices[0].message.reasoning_content)

        # 通过content字段打印最终答案
        print("最终答案：")
        print(completion.choices[0].message.content)

        return think, answer, history