import requests
from typing import List
from langchain.embeddings.base import Embeddings


class CustomEmbeddings(Embeddings):
    """
    LangChain 兼容的自定义 Embeddings 类，使用本地 API 生成文本向量。
    """

    def __init__(self, api_url: str = 'http://localhost:11434/api/embeddings', model: str = 'bge-m3'):
        self.api_url = api_url
        self.model = model

    def embed_query(self, text: str) -> List[float]:
        """用于查询文本的嵌入（单个文本）"""
        return self._get_embedding(text)

    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        """用于文档嵌入（批量处理多个文本）"""
        return [self._get_embedding(text) for text in texts]

    def _get_embedding(self, text: str) -> List[float]:
        """调用本地 API 获取文本嵌入"""
        try:
            response = requests.post(
                self.api_url,
                json={'model': self.model, 'prompt': text},
                timeout=10
            )
            response.raise_for_status()
            embedding = response.json().get('embedding')
            if not embedding:
                raise ValueError("API 返回的 embedding 为空")
            return embedding
        except requests.exceptions.RequestException as e:
            raise ConnectionError(f"Embedding API 请求失败: {e}")
        except (ValueError, KeyError) as e:
            raise ValueError(f"处理 embedding 响应失败: {e}")

