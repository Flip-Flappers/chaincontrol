from langchain_community.document_loaders import JSONLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import InMemoryVectorStore
import glob
import os

# 设置OpenAI API密钥
os.environ["OPENAI_API_KEY"] = "你的API密钥"


# 1. 加载JSON文件（假设你的JSON结构包含'text'字段）
def load_json_files(folder_path):
    file_paths = glob.glob(f"{folder_path}/**/*.json", recursive=True)

    documents = []
    for file_path in file_paths:
        try:
            loader = JSONLoader(
                file_path=file_path,
                jq_schema='.text',  # 根据实际结构调整
                text_content=False
            )
            documents.extend(loader.load())
        except Exception as e:
            print(f"加载文件 {file_path} 时出错: {str(e)}")

    return documents


# 2. 分割文本
def split_documents(docs):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,  # 更小的chunk适合精准检索
        chunk_overlap=150,
        separators=["\n\n", "\n", "。", "！", "？", "；"]
    )
    return text_splitter.split_documents(docs)


# 3. 创建内存向量存储
def create_vector_store(docs):
    embeddings = ()
    return InMemoryVectorStore.from_documents(docs, embeddings)


# 4. 增强型检索器
def create_retriever(vector_store, top_k=5):
    return vector_store.as_retriever(
        search_type="mmr",  # 使用最大边际相关性算法
        search_kwargs={
            "k": top_k,
            "lambda_mult": 0.3  # 多样性控制参数
        }
    )


# 主流程
def main():
    # 加载文档
    print("正在加载JSON文件...")
    documents = load_json_files("definitions")
    print(f"成功加载 {len(documents)} 个文档")

    # 分割文档
    print("分割文本中...")
    split_docs = split_documents(documents)
    print(f"生成 {len(split_docs)} 个文本块")

    # 创建向量存储
    print("创建内存向量数据库...")
    vector_store = create_vector_store(split_docs)

    # 创建检索器
    retriever = create_retriever(vector_store)

    # 交互式查询
    while True:
        query = input("\n请输入搜索内容（输入q退出）: ")
        if query.lower() == 'q':
            break

        relevant_docs = retriever.invoke(query)

        print(f"\n找到 {len(relevant_docs)} 个相关结果：")
        for i, doc in enumerate(relevant_docs):
            print(f"\n#{i + 1} 来源文件: {doc.metadata['source']}")
            print(f"相似度分数: {doc.metadata['score']:.3f}")
            print(f"内容片段: {doc.page_content[:250]}...")


if __name__ == "__main__":
    main()