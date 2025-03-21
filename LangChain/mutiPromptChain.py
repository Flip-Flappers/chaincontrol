import os
from langchain.prompts import ChatPromptTemplate
from langchain.output_parsers import ResponseSchema
from langchain.output_parsers import StructuredOutputParser
from langchain.chains import ConversationChain, LLMChain
from langchain.memory import ConversationBufferMemory
from deepseek import LocalChatModel
import pandas as pd
from langchain.chains.router import MultiPromptChain
from langchain.chains.router.llm_router import LLMRouterChain, RouterOutputParser
from langchain.prompts import PromptTemplate
import langchain
langchain.debug = True

physics_template = """
You are a physics expert.
You are given the following conversation between a human and an AI.
The human provides a question about physics.
You must answer the question based on the information provided in the context.

Here is a question:
{input}"""

math_template = """
You are a mathematician.
You are given the following conversation between a human and an AI.
The human provides a question about math.
You must answer the question based on the information provided in the context.

Here is a question:
{input}"""

history_template = """
You are a history expert.
You are given the following conversation between a human and an AI.
The human provides a question about history.
You must answer the question based on the information provided in the context.

Here is a question:
{input}"""

computerscience_template = """
You are a computer science expert.
You are given the following conversation between a human and an AI.
The human provides a question about computer science.
You must answer the question based on the information provided in the context.

Here is a question:
{input}"""

geography_template = """
You are a geography expert.
You are given the following conversation between a human and an AI.
The human provides a question about geography.
You must answer the question based on the information provided in the context.

Here is a question:
{input}"""

prompt_infos = [
    {
        "name": "physics",
        "description": "Good for when you need to answer questions about physics",
        "prompt_template": physics_template,
    },
    {
        "name": "math",
        "description": "Good for when you need to answer questions about math",
        "prompt_template": math_template,
    },
    {
        "name": "history",
        "description": "Good for when you need to answer questions about history",
        "prompt_template": history_template,
    },
    {
        "name": "computerscience",
        "description": "Good for when you need to answer questions about computer science",
        "prompt_template": computerscience_template,
    },
    {
        "name": "geography",
        "description": "Good for when you need to answer questions about geography",
        "prompt_template": geography_template,
    },
]

llm = LocalChatModel()
memory = ConversationBufferMemory()
destination_chains = {}
for p_info in prompt_infos:
    prompt_name = p_info["name"]
    prompt_template = p_info["prompt_template"]
    prompt = ChatPromptTemplate.from_template(template=prompt_template)
    chain = LLMChain(llm=llm, prompt=prompt, output_key="text")
    destination_chains[prompt_name] = chain

destinations = [f"{p['name']}: {p['description']}" for p in prompt_infos]
destination_str = "\n".join(destinations)

default_prompt = ChatPromptTemplate.from_template("{input}")

default_chain = LLMChain(llm=llm, prompt=default_prompt)


MULTI_PROMPT_TEMPLATE = """GIVEN a raw text input to a language model, help me route it to the correct prompt template.

<<FORMATTING>>
Return a markdown code snippet with JSON object formatted as follows:
```json
{{{{
    "destination": string \ name of the prompt to use or "DEFAULT"
    "next_inputs": string \ a potentially modified version of the original input
}}}}
```
REMEMBER: "destination" MUST be one of the candidate prompt names specified below OR it can be "DEFAULT" if the input doesn't match any of the candidate prompts
REMEMBER: "next_inputs can just be the original input if you don't think any modifications are needed

<< CANDIDATE PROMPTS >>
{destinations}

<< INPUT >>
{{input}}

<< OUTPUT (remember to include the ```json) >>"""




router_template = MULTI_PROMPT_TEMPLATE.format(destinations=destination_str)
router_prompt = PromptTemplate(
    template=router_template,
    input_variables=["input"],
    output_parser=RouterOutputParser(),
)
router_chain = LLMRouterChain.from_llm(llm, router_prompt)

mutiPromptChain = MultiPromptChain(
    router_chain=router_chain,
    destination_chains=destination_chains,
    default_chain=default_chain,
    verbose=True,
)

print(mutiPromptChain.run("觉得我的青蛙回复全文及去外婆家地区物品请问大旗网大旗网去污粉全微分请问"))
