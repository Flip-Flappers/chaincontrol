import json
import logging
import os
import sys

from langchain.chains import RetrievalQA
from langchain.document_loaders import CSVLoader
from langchain.vectorstores import Chroma
from langchain.indexes import VectorstoreIndexCreator
from langchain_ollama import OllamaEmbeddings, OllamaLLM

from bgem3 import CustomEmbeddings
from deepseek import LocalChatModel
import pandas as pd

# 设置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    try:
        # 加载 CSV 文件
        loader = CSVLoader(file_path="./matched_results.csv", encoding="utf-8")
        docs = loader.load()


        llm = OllamaLLM(model="deepseek-r1:1.5b", base_url="http://localhost:11434", temperature=1.0)
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
        retriever = vector_store.as_retriever(search_kwargs={"k": 5})

        # 构建查询模板，使用 CSV 中的备选项作为上下文
        query_template = """Given a list of available APIs and summaries:
        << QUERY >>
        Check all the online devices for me

        <<FORMATTING>>
        Return a markdown code snippet with JSON object formatted as follows:
        ```json
        {
            "total": 5,
            "results": [
                {
                    "API name": string,  // the API name answer with best match of the << QUERY >>,
                    "reason": string  // the reason of the target API name
                },
                ...
            ]
        }
        ```
        REMEMBER: "total" MUST be 5 and MUST be consistent with the number in the json list,
        REMEMBER: "API name" MUST be one of the candidate names specified in the list.

        << OUTPUT (remember to include the ```json) >>
        """

        # 创建 RetrievalQA
        askchain = RetrievalQA.from_chain_type(
            llm=llm,
            retriever=retriever,
            chain_type="stuff",
            return_source_documents=True,
            verbose=True,
        )



        # 调用 askchain 来得到答案和相关文档
        response = askchain(query_template)

        # 输出回答和源文档
        print("Answer:", response["result"])
        for idx, doc in enumerate(response["source_documents"]):
            print(f"Document {idx + 1}:")
            print(doc.page_content)  # 输出文档的具体内容
            print("-" * 50)  # 分隔符

    except Exception as e:
        logger.error(f"运行时出错: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
