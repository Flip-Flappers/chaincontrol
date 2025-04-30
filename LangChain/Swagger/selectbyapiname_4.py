import csv
import json
import logging
import os
import re
import sys

from langchain.chains import RetrievalQA
from langchain.document_loaders import CSVLoader
from langchain.vectorstores import Chroma
from langchain_ollama import OllamaEmbeddings, OllamaLLM


# 设置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    try:
        # 加载 CSV 文件
        loader = CSVLoader(file_path="./filtered_results.csv", encoding="utf-8")
        docs = loader.load()


        llm = OllamaLLM(model="deepseek-r1:14b", base_url="http://localhost:11434", temperature=1.0)
        embeddings = OllamaEmbeddings(model="bge-m3", base_url="http://localhost:11434")

        # Chroma 索引的持久化存储路径
        persist_directory = "./filtered_tmp_api_paths_english"
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
        At the same time, you have a list of API. I need you to return the target API name that is most relevant to the user's needs.
        You need to indicate the reason for choosing the target API name and the reason for excluding other API name in the REASON.
        
        IMPORTANT: You must consider all APIs comprehensively before coming to a conclusion.
        << QUERY >>
        {original_command}
       

         << FORMATTING >>
        {json_output}
        """


        json_output = """
            Return a markdown code snippet with JSON object fomatted as follows:
            ```json
            {
                "results": 
                {
                    "target API name": string,  // the API name answer with best match of the << QUERY >>,
                    "reason": string  // the reason for choosing the target API name and the reason for excluding other API name.
                }
                
            }
            ```
            REMEMBER: "target API name" MUST be one of the candidate name specified in the list.
    
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

        # 创建 RetrievalQA
        askchain = RetrievalQA.from_chain_type(
            llm=llm,
            retriever=retriever,
            chain_type="stuff",
            return_source_documents=True,
            verbose=True,
        )



        # 调用 askchain 来得到答案和相关文档
        response = askchain(query)

        # 输出回答和源文档
        print("Answer:", response["result"])
        for idx, doc in enumerate(response["source_documents"]):
            print(f"Document {idx + 1}:")
            print(doc.page_content)  # 输出文档的具体内容
            print("-" * 50)  # 分隔符


        match = re.search(r'"target API name"\s*:\s*"([^"]+)"', response["result"].split("</think>")[1])
        if match:
            target_api_name = match.group(1)
            print("Target API Name:", target_api_name)
            with open('target_api.csv', 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(['Target API Name'])  # 写表头
                writer.writerow([target_api_name])  # 写数据

            print("已保存到 target_api.csv")

    except Exception as e:
        logger.error(f"运行时出错: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
