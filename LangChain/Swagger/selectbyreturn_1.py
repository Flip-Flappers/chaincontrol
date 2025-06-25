import csv
from langchain_community.document_loaders import CSVLoader
from langchain_ollama import OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
import glob
import os
import shutil


def load_csv_files(folder_path):
    """ 加载 CSV 文件，并将文件名加入 metadata """
    file_paths = glob.glob(f"{folder_path}/**/*.csv", recursive=True)
    documents = []

    for file_path in file_paths:
        loader = CSVLoader(file_path=file_path)
        file_docs = loader.load()

        # 将文件名作为 metadata，并修改 page_content 加入文件名信息
        file_name = os.path.basename(file_path)
        for doc in file_docs:
            doc.metadata["source"] = file_name  # 文件名
            doc.page_content = f"[{file_name}] {doc.page_content}"  # 在内容前加上文件名

        documents.extend(file_docs)

    return documents


def split_documents(docs):
    """ 使用递归分词器分割文档，确保文件名仍然可见 """
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=50,
        chunk_overlap=25,
        separators=["\n\n", "\n", "。", "！", "？", "；"]
    )

    split_docs = text_splitter.split_documents(docs)

    for doc in split_docs:
        if "source" in doc.metadata:
            file_name = doc.metadata["source"]
            doc.page_content = f"[{file_name}] {doc.page_content}"

    return split_docs


def create_vector_store(docs):
    """ 复用已有 Chroma 数据，避免重复计算向量 """
    persist_directory = "select_by_definitions_chroma_db"
    if os.path.exists(persist_directory):
        shutil.rmtree(persist_directory)

    # 检查 Chroma 数据库是否已经存在
    if os.path.exists(persist_directory) and os.listdir(persist_directory):
        print("检测到已有 Chroma 数据库，直接加载...")
        return Chroma(persist_directory=persist_directory, embedding_function=OllamaEmbeddings(model="bge-m3"))

    print("未找到已有数据，重新计算嵌入...")
    embeddings = OllamaEmbeddings(model="bge-m3", base_url="http://localhost:11434")
    vector_store = Chroma.from_documents(docs, embeddings, persist_directory=persist_directory)
    vector_store.persist()  # 持久化存储
    return vector_store


def create_retriever(vector_store, top_k=10):
    """ 创建检索器，支持 MMR 方式，优先匹配文件名 """
    return vector_store.as_retriever(
        search_type="mmr",  # 使用最大边际相关性算法
        search_kwargs={
            "k": top_k,
            "lambda_mult": 0.3  # 多样性控制参数
        }
    )


def save_documents_to_csv(relevant_docs, output_file="selectbyreturn.csv"):


    if os.path.exists(output_file):
        os.remove(output_file)
    """ 将相关文档的文件名和内容片段保存为 CSV 文件 """
    with open(output_file, mode="w", newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # 写入 CSV 文件头
        writer.writerow(["className", "contents"])

        # 写入每个相关文档的信息
        # 使用一个 set 记录已经写入的文件名
        written_files = set()

        for i, doc in enumerate(relevant_docs):
            file_name = doc.metadata.get("source", "未知文件")[:-4]  # 获取文件名
            content_snippet = doc.page_content

            # 只有当 file_name 不在 set 中时才写入
            if file_name not in written_files:
                writer.writerow([file_name, content_snippet])
                written_files.add(file_name)  # 记录已写入的文件名

    print(f"相关文档已保存至 {output_file}")


def main():


    print("正在加载 CSV 文件...")
    documents = load_csv_files("csv_definitions")
    print(f"成功加载 {len(documents)} 个文档")

    print("分割文本中...")
    split_docs = split_documents(documents)
    print(f"生成 {len(split_docs)} 个文本块")

    print("创建 Chroma 向量数据库...")
    vector_store = create_vector_store(split_docs)
    retriever = create_retriever(vector_store)

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

            # 读取数据
            for row in reader:
                Rewritten_Command.append(row[index])
    with open(file_name, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)

        # 读取表头
        header = next(reader)
        if "Translated Command" in header:
            index = header.index("Translated Command")
            for row in reader:
                Translated_Command.append(row[index])

    all_relevant_docs = []
    for query in Rewritten_Command:

        relevant_docs = retriever.invoke(query)
        all_relevant_docs.append(relevant_docs)
        print(f"\n找到 {len(relevant_docs)} 个相关结果：")
        for i, doc in enumerate(relevant_docs):
            file_name = doc.metadata.get("source", "未知文件")
            print(f"\n#{i + 1} 文件名: {file_name}")
            print(f"内容片段: {doc.page_content[:250]}...")
    query = Translated_Command[0]
    relevant_docs = retriever.invoke(query)
    all_relevant_docs.append(relevant_docs)
    print(f"\n找到 {len(relevant_docs)} 个相关结果：")
    for i, doc in enumerate(relevant_docs):
        file_name = doc.metadata.get("source", "未知文件")
        print(f"\n#{i + 1} 文件名: {file_name}")
        print(f"内容片段: {doc.page_content[:250]}...")
    # 保存相关文档到 CSV
    save_documents_to_csv(relevant_docs)


if __name__ == "__main__":
    main()
