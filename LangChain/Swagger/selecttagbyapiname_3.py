import csv
import json
import logging
import os
import re
import sys

import pandas as pd
from langchain.chains import RetrievalQA
from langchain.document_loaders import CSVLoader
from langchain.vectorstores import Chroma
from langchain.indexes import VectorstoreIndexCreator
from langchain_ollama import OllamaEmbeddings, OllamaLLM


# 设置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    try:
        # 加载 CSV 文件
        from langchain.document_loaders import CSVLoader

        # 加载 CSV 文件
        loader = CSVLoader(file_path="./matched_results.csv", encoding="utf-8")
        docs = loader.load()

        api_names = []
        for idx, doc in enumerate(docs, start=1):  # 使用 enumerate 为每个文档添加序号
            lines = doc.page_content.split("\n")  # 按行分割
            for line in lines:
                if "API path:" in line:
                    api_name = line.split("API path:")[-1].strip()  # 获取 API path
                    api_names.append(f"{idx}. {api_name}")  # 添加序号和 API 名称

        # 将所有 API 名称连接为一个字符串
        api_names_str = "\n".join(api_names)  # 每个 API 名称一行

        print(api_names_str)  # 输出带序号的 API 名称

        llm = OllamaLLM(model="deepseek-r1:14b", base_url="http://localhost:11434", temperature=1.0)
        embeddings = OllamaEmbeddings(model="bge-m3", base_url="http://localhost:11434")

        # Chroma 索引的持久化存储路径
        persist_directory = "./tmp_api_paths_english"
        vector_store = None
        if os.path.exists(persist_directory) and os.listdir(persist_directory):
            print("检测到已有 Chroma 数据库，直接加载...")
            vector_store = Chroma(persist_directory=persist_directory, embedding_function=OllamaEmbeddings(model="bge-m3"))
        else:
            print("未找到已有数据，重新计算嵌入...")
            vector_store = Chroma.from_documents(docs, embeddings, persist_directory=persist_directory)
            vector_store.persist()  # 持久化存储

        # 获取检索器
        retriever = vector_store.as_retriever(search_kwargs={"k": 100})

        # 构建查询模板，使用 CSV 中的备选项作为上下文


        query_template = """
        You are an experienced IoT system expert. Currently, users are not familiar with your IoT software and can only issue vague commands. 
        User's vague needs are displayed in the << QUERY >>.
        At the same time, you have a list of API interfaces, each of which has a tag. I need you to return the tag that is most relevant to the user's needs.
        IMPORTANT: You must consider all APIs comprehensively before coming to a conclusion.
        << QUERY >>
     
        {original_command}
       
        
        << FORMATTING >>
        {json_output}
        
        CAUTION: Only when the virtual device is EXPLICITLY stated in << QUERY >> then the tags can be virtual device, OTHERWISE the tag MUST CANNOT BE virtual device.
        """

        json_output = """
       
        Return a markdown code snippet with JSON object fomatted as follows:
        ```json
        {
            "results": 
            {
                "tag": string,  // the tag answer with best match of the << QUERY >>,
                "reason": string  // the reason of the target tag
            }
        }
        ```
        REMEMBER: "tag" MUST be one of the candidate names specified in csv.
        
        << OUTPUT (remember to include the ```json) >>
        """

        file_name = "./commands.csv"
        translated_commands = []
        with open(file_name, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            # 读取表头
            header = next(reader)
            # 找到 "Translated Rewritten Command" 列的索引
            if "Translated Command" in header:
                index = header.index("Translated Command")

                # 读取数据
                for row in reader:
                    translated_commands.append(row[index])

        Rewritten_Command = []
        with open(file_name, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            # 读取表头
            header = next(reader)
            # 找到 "Translated Rewritten Command" 列的索引
            if "Rewritten Command" in header:
                index = header.index("Rewritten Command")
                # 读取数据
                for row in reader:
                    Rewritten_Command.append(row[index])


        command = translated_commands[0]
        command += " Users may wish to implement the following functions:"
        for i, rewritten_command in enumerate(Rewritten_Command):
            command += str("\n")
            command += str(i) + str(".")
            command += str(rewritten_command)

        query = query_template.format(original_command=command, json_output=json_output)
        print(query)
        # 创建 RetrievalQA
        askchain = RetrievalQA.from_chain_type(
            llm=llm,
            retriever=retriever,
            chain_type="stuff",
            return_source_documents=True,
            verbose=True,
        )
        # 调用 askchain 来得到答案和相关文档
        response = askchain(query).get("result")
        print(response)
        match = re.search(r'"tag":\s*"([^"]+)"', response)

        if match:
            tag_value = match.group(1)
        else:
            tag_value = ""
        print("Answer:", tag_value)
        # 输出回答和源文档
        file_name = "matched_results.csv"
        df = pd.read_csv(file_name, encoding="utf-8")


        # 过滤匹配的行
        filtered_df = df[df["Tags"] == tag_value]

        # 保存筛选后的数据到新 CSV 文件
        filtered_file_name = "filtered_results.csv"
        filtered_df.to_csv(filtered_file_name, index=False, encoding="utf-8")

        print(f"筛选后的数据已保存到 {filtered_file_name}")




    except Exception as e:
        logger.error(f"运行时出错: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
