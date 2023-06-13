import os
from langchain import OpenAI, SerpAPIWrapper
from langchain.llms import AzureOpenAI
from langchain.chat_models import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage, SystemMessage, ChatMessage
from langchain import PromptTemplate
from langchain.output_parsers import CommaSeparatedListOutputParser
from dotenv import load_dotenv
load_dotenv()

llm = OpenAI(model_name='text-davinci-003', n=2, temperature=0.3)
# print(llm('给我讲一个笑话'))
# print(llm.generate(['给我讲一个故事', '给我讲一个笑话']))


# https://python.langchain.com/en/latest/modules/models/chat/integrations/azure_chat_openai.html
# llm = AzureOpenAI(
#     openai_api_base='http://xxx',
#     model_name="text-davinci-003",
#     n=2,
#     temperature=0.3,
#     openai_api_type="azure",
#     openai_api_version="2023-03-15-preview",)
# print(llm('给我讲一个笑话'))

def search_func(input, extra_string=''):
    print(input)
    if dict == type(input):
        input = input.values().to_string()
    input = input + extra_string
    search = SerpAPIWrapper()
    info = search.run(input)
    print(input, ':', info)
    template = """
    已知信息: {info}
    请根据已知的信息回答: {input}
    注意: 回答的信息要包含在已知信息中，只输出答案，不要说明和解释信息
    """
    prompt_template = PromptTemplate(template=template, input_variables=["info", "input"])
    return llm(prompt=prompt_template.format(info=info, input=input))

print(search_func({'input': '莱昂纳多·迪卡普里奥'}))