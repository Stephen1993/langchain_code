import os
from langchain import OpenAI
from langchain.llms import AzureOpenAI
from langchain.chat_models import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage, SystemMessage, ChatMessage
from langchain.prompts import (
    ChatPromptTemplate,
    PromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
    FewShotPromptTemplate,
)
from langchain.chains import LLMChain, SimpleSequentialChain
from dotenv import load_dotenv
load_dotenv()

template = '我的邻居姓{lastname}, 他生了个儿子, 给他儿子起个名字'
prompt = PromptTemplate(
    input_variables=['lastname'],
    template=template,
)

# prompt_text = prompt.format(lastname='张')
# print(prompt_text)
llm = OpenAI(temperature=0.9)
chain = LLMChain(llm=llm, prompt=prompt)

second_prompt = PromptTemplate(
    input_variables=['childname'],
    template='邻居的儿子叫{childname}, 给他起一个小名',
)

chain_two = LLMChain(llm=llm, prompt=second_prompt)

overall_chain = SimpleSequentialChain(chains=[chain, chain_two], verbose=True)

print(overall_chain.run('张'))
