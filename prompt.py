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
from dotenv import load_dotenv
load_dotenv()

# zero-shot
# template = '我的邻居姓{lastname}, 他生了个儿子, 给他儿子起个名字'
# prompt = PromptTemplate(
#     input_variables=['lastname'],
#     template=template,
# )
#
# prompt_text = prompt.format(lastname='张')
# print(prompt_text)
# llm = OpenAI(temperature=0.9)
# print(llm(prompt_text))

examples = [
    {'word': '开心', 'antonym': '难过'},
    {'word': '高', 'antonym': '矮'},
]

template = '单词: {word}, 反义词: {antonym}'
prompt = PromptTemplate(
    input_variables=['word', 'antonym'],
    template=template,
)
few_shot_prompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt=prompt,
    prefix='给出每个单词的反义词',
    suffix='单词: {input}, 反义词:',
    input_variables=['input'],
)

prompt_text = few_shot_prompt.format(input='粗')
print(prompt_text)
llm = OpenAI(temperature=0.9)
print(llm(prompt_text))
