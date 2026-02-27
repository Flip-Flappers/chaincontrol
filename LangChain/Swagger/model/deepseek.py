import os
from openai import OpenAI








class deepseek:

    def __init__(self):

        self.client = OpenAI(
            api_key=os.getenv("DASHSCOPE_API_KEY"),
            base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
        )
        self.model = "deepseek-v3.2"



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


        completion = self.client.chat.completions.create(
            model="deepseek-v3.2",
            messages=history,
            extra_body={"enable_thinking": False},
            stream=True,
            stream_options={
                "include_usage": True
            },
        )
        reasoning_content = ""  # 完整思考过程
        answer_content = ""  # 完整回复
        is_answering = False  # 是否进入回复阶段
        print("\n" + "=" * 20 + "思考过程" + "=" * 20 + "\n")

        for chunk in completion:
            if not chunk.choices:
                print("\n" + "=" * 20 + "Token 消耗" + "=" * 20 + "\n")
                print(chunk.usage)
                continue

            delta = chunk.choices[0].delta

            # 只收集思考内容
            if hasattr(delta, "reasoning_content") and delta.reasoning_content is not None:
                if not is_answering:
                    print(delta.reasoning_content, end="", flush=True)
                reasoning_content += delta.reasoning_content

            # 收到content，开始进行回复
            if hasattr(delta, "content") and delta.content:
                if not is_answering:
                    print("\n" + "=" * 20 + "完整回复" + "=" * 20 + "\n")
                    is_answering = True
                print(delta.content, end="", flush=True)
                answer_content += delta.content
        history.append({'role': 'assistant', 'content': answer_content})
        return reasoning_content, answer_content, history