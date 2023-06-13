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
    HumanMessagePromptTemplate
)
from dotenv import load_dotenv
load_dotenv()

chat = ChatOpenAI(temperature=0)
# 返回json格式字符串，按照每项参数拆分，不要说明和解释信息
message = [
    SystemMessage(content='返回json格式，按照每项参数拆分，不要说明和解释信息'),
    HumanMessage(content='告诉我特斯拉model Y汽车的尺寸参数'),
]
print(chat(message))

system_template = '你是一个把{input}翻译成{output}的助手'
system_template_prompt = SystemMessagePromptTemplate.from_template(system_template)
human_template = '{text}'
human_template_prompt = HumanMessagePromptTemplate.from_template(human_template)
chat_prompt = ChatPromptTemplate.from_messages([system_template_prompt, human_template_prompt])
message = chat_prompt.format_prompt(input='英语', output='中文', text='hello')
print(message)
print(chat(message.to_messages()))
