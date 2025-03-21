import requests
from langchain.llms.base import LLM
from typing import Any, List, Mapping, Optional


class LocalChatModel(LLM):
    def _call(self, prompt: str, stop: Optional[List[str]] = None) -> str:
        """
        发送请求到本地模型生成答案
        """
        url = "http://localhost:11434/api/generate"
        data = {
            "model": "deepseek-r1:1.5b",
            "prompt": prompt,
            "stream": False,
            "temperature": 0
        }
        response = requests.post(url, json=data)
        ans = response.json().get("response", "Error: No response")
        print("deepseek_ans:~~~~~~~~~~~~~~~~~" + ans)
        return ans.split("</think>")[-1].strip()

    def invoke(self, prompt: str, stop: Optional[List[str]] = None, config: Optional[Mapping[str, Any]] = None) -> str:
        """
        覆盖`invoke`方法以便langchain正确使用
        """
        print(config)
        return self._call(self.generate_prompt(prompt, config), stop)

    @property
    def _identifying_params(self) -> Mapping[str, Any]:
        return {"endpoint": "http://localhost:11434/api/generate"}

    @property
    def _llm_type(self) -> str:
        return "custom_local_llm"
