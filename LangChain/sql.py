import json

from langchain.chains import RetrievalQA
from langchain.chains.llm import LLMChain
from langchain.chains.sql_database.query import create_sql_query_chain
from langchain.document_loaders import CSVLoader
from langchain.vectorstores import DocArrayInMemorySearch
from langchain.indexes import VectorstoreIndexCreator
from typing import List
from langchain.sql_database import SQLDatabase
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.agents import create_sql_agent
import logging
import sys

from langchain_community.tools import QuerySQLDatabaseTool
from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM

from langchain_community.document_loaders import UnstructuredMarkdownLoader
from langchain_ollama import ChatOllama

from bgem3 import CustomEmbeddings
from deepseek import LocalChatModel

# 设置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def load_json_from_file(json_file_path):
    """加载JSON文件并返回数据"""
    try:
        with open(json_file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    except Exception as e:
        logger.error(f"加载JSON文件时出错: {e}")
        sys.exit(1)



def main():
    try:

        loader = CSVLoader(file_path="./pre_sql.csv", encoding="utf-8")
        documents = loader.load()

        # 初始化模型
        llm1 = LocalChatModel()
        embedding = CustomEmbeddings()

        # 创建索引
        index = VectorstoreIndexCreator(
            vectorstore_cls=DocArrayInMemorySearch,
            embedding=embedding,
        ).from_loaders([loader])
        retriever = index.vectorstore.as_retriever(search_kwargs={"k": 5})

        database_uri = "mysql+pymysql://root:neoLab@127.0.0.1:3306/ueiot"

        db = SQLDatabase.from_uri(database_uri)

        # 初始化模型
        llm = OllamaLLM(model="deepseek-r1:14b", base_url="http://localhost:11434")

        query_template = """Given a list of table name and description in CSV", Carefully analyze table names, table descriptions, column names, column descriptions, search for table name that match the following criteria:
         << QUERY >>
        帮我查询哪些设备是在线的

         <<FORMATTING>>
        Return a markdown code snippet with JSON object formatted as follows:
        ```json
        {{{{
            "total_table": 5,
            "answer": [{{
                "table name": string \ the table name answer with best match of the  << QUERY >>,
                "reason: string \ the reason of the target table name
            }},
            {{
                "table name": string \ the table name answer with second match of the  << QUERY>>,
                "reason: "reason: string \ the reason of the target table name
            }},
            ...
            ]
        }}}}
        ```
        REMEMBER: "total_table" MUST be 5 and MUST be consistent with the number in the json list,
        REMEMBER: "table name" MUST be one of the candidate name specified in pre_sql.csv,
        REMEMBER:  Return the top 5 matching table name in pre_sql.csv from the list about << QUERY >>,
        REMEMBER:  Carefully analyze table names, table descriptions, column names, column descriptions. ESPECIALLY column descriptions,
    

        << OUTPUT (remember to include the ```json) >>
        """

        askchain = RetrievalQA.from_chain_type(
            llm=llm1,
            retriever=retriever,
            chain_type="map_rerank",
            verbose=True,
        )



        result = askchain.run(query_template)

        print(result)


        querychain = create_sql_query_chain(llm, db)

        PROMPT_TEMPLATE = """You are a sql agent, please think carefully and help me determine how many commands need to be EXECUTED according to the instructions in << INPUT >>, and then follow the steps given in << INPUT >> to list each sql command.
                << ASSIST >>
                You must use the table in the following list:
                    {{input}}
                    
                <<FORMATTING>>
                Return a markdown code snippet with JSON object formatted as follows:
                ```json
                {{{{
                    "total_step": int,
                    "answer": [{{
                        "step_number": 1,
                        "sql": string \ the SQL answer with step one 
                    }},
                    {{
                        "step_number": 2,
                        "sql": string \ the SQL answer with step two
                    }},
                    ...
                    ]
                }}}}
                ```
                REMEMBER: "total_step" MUST be an Integer，MUST be consistent with the number in the json list
                REMEMBER: "sql" MUST be formatted as a sql and be useful with << INPUT >>, the target table must in << ASSIST >>

                << INPUT >>
                帮我查询哪些设备是在线的?

                << OUTPUT (remember to include the ```json) >>"""

        query = PROMPT_TEMPLATE.format(input = result)
        print(query)

        execute_query = QuerySQLDatabaseTool(db = db)
        chain = querychain
        result = chain.invoke({"question":query})
        print(result)

    except Exception as e:
        logger.error(f"运行时出错: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
