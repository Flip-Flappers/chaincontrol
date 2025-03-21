from langchain.chains import RetrievalQA
from langchain.document_loaders import CSVLoader
from langchain.vectorstores import DocArrayInMemorySearch
from langchain.indexes import VectorstoreIndexCreator
from typing import List
import logging
import sys

from bgem3 import CustomEmbeddings
from deepseek import LocalChatModel

# 设置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def create_qa_system(file_path: str) -> RetrievalQA:
    """创建问答系统"""
    try:
        # 加载文档
        loader = CSVLoader(file_path=file_path, encoding="utf-8")
        documents = loader.load()

        # 初始化模型
        llm = LocalChatModel()
        embedding = CustomEmbeddings()

        # 创建索引
        index = VectorstoreIndexCreator(
            vectorstore_cls=DocArrayInMemorySearch,
            embedding=embedding,
        ).from_loaders([loader])

        db = DocArrayInMemorySearch.from_documents(
            documents,
            embedding,
        )

        ans = db.similarity_search(query="帮我首先调用删除接口，再调用获取数据。")
        print(ans)

        # 创建检索器和QA链
        retriever = index.vectorstore.as_retriever()

        return RetrievalQA.from_chain_type(
            llm=llm,
            retriever=retriever,
            chain_type="stuff",
            verbose=True,
        )
    except Exception as e:
        logger.error(f"创建QA系统时出错: {e}")
        raise


def main():
    try:
        file = "./output.csv"
        qa_system = create_qa_system(file)
        PROMPT_TEMPLATE = """You are an interface administrator, please think carefully and help me determine how many commands need to be EXECUTED according to the instructions in << INPUT >>, and then follow the steps given in << INPUT >> to list the CORRESPONDING url and name of each command.

        <<FORMATTING>>
        Return a markdown code snippet with JSON object formatted as follows:
        ```json
        {{{{
            "total_step": int
            "answer": [{
                "step_number": 1
                "url": string \ the data about api.url in output.csv 
                "name": string \ the data about api.name in output.csv 
            },
            {
                "step": 2
                "url": string 
                "name": string 
            },
            ...
            ]
        }}}}
        ```
        REMEMBER: "total_step" MUST be an Integer，MUST be consistent with the number in the json list
        
        
        
        
        
        
        
        REMEMBER: "name" MUST be one of the candidate name specified in output.csv

        << INPUT >>
        我要删除接口，然后删除接口，然后注册接口，再删除接口，最后获取
        
        
        
        
        
        
        
        
        
        
        接口的配置。

        << OUTPUT (remember to include the ```json) >>"""

        query = PROMPT_TEMPLATE
        result = qa_system.run(query)
        print(result)

    except FileNotFoundError:
        logger.error(f"找不到文件: {file}")
        sys.exit(1)
    except Exception as e:
        logger.error(f"运行时出错: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
