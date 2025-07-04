import csv

from langchain.agents import initialize_agent, AgentType
from langchain.chains.llm import LLMChain
from langchain.tools import Tool
from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM


class ToolSelector:
    def call_device_api(command: str) -> str:
        # 实际调用你设备端API的逻辑
        return f"[DeviceAPI] Executing command on device: {command}"

    def call_platform_api(command: str) -> str:
        # 实际调用你平台API的逻辑
        return f"[PlatformAPI] Executing command on platform: {command}"

    device_tool = Tool(
        name="DeviceAPITool",
        func=call_device_api,
        description="Use this to send control commands to physical devices. Best for actions like 'restart device', 'get device status', 'turn on sensor'."
    )

    platform_tool = Tool(
        name="PlatformAPITool",
        func=call_platform_api,
        description="Use this to perform operations on the platform, such as 'add user', 'delete task', 'update configuration', or other management actions."
    )

    json_output = """
    Return a markdown code snippet with JSON object formatted as follows:
    ```json
    {
        "results":
        {
            "Action": String, // one of [DeviceAPITool, PlatformAPITool]
            "Thought": string,  // your reasoning here
            "Action Input": the specific command input here
        }
    }
    ```
    REMEMBER: "Action" MUST be one of [DeviceAPITool, PlatformAPITool],
    REMEMBER: "Action Input" MUST be based on << User Input >>
    """
    def select_tool(self) -> Tool:
        template = """
        You are an intelligent assistant responsible for choosing the correct tool to handle user commands.

        There are two tools available:
        1. DeviceAPITool - for sending control commands to a single type of product or individual device.
        2. PlatformAPITool - for addition, deletion, modification, and search of data in IoT systems.
        
        Based on the user's input, decide whether to use the 'DeviceAPITool' or 'PlatformAPITool'.

         << Output Format >>
        {json_output}

        << User Input >>
        {input}
        """
        prompt = PromptTemplate.from_template(template)

        llm = OllamaLLM(model="deepseek-r1:14b", base_url="http://localhost:11434", temperature=1.0)
        llm_chain = LLMChain(prompt=prompt, llm=llm)







        Rewritten_Command = []
        Translated_Command = []
        file_name = "commands.csv"
        with open(file_name, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)

            # 读取表头
            header = next(reader)

            # 找到 "Translated Rewritten Command" 列的索引
            if "Rewritten Command" in header:
                index = header.index("Rewritten Command")
                for row in reader:
                    Rewritten_Command.append(row[index])

        with open(file_name, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            header = next(reader)
            if "Translated Command" in header:
                index = header.index("Translated Command")
                for row in reader:
                    Translated_Command.append(row[index])


        query = Translated_Command[0]

        result = llm_chain.run({"input": query, "json_output": self.json_output})

        # 获取中间过程输出（包含 Thought 和 Action 信息）
        print(result)


