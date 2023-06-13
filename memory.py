from dotenv import load_dotenv
load_dotenv()
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
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.llms import OpenAI
from langchain.memory import ChatMessageHistory
from langchain import ConversationChain
from langchain.schema import messages_from_dict, messages_to_dict

history = ChatMessageHistory()
history.add_user_message('在吗?')
history.add_ai_message('有什么事?')
print(history.messages)

llm = OpenAI(temperature=0)
conversation = ConversationChain(llm=llm, verbose=True)
conversation.predict(input='小明有1只猫')
conversation.predict(input='小刚有2只狗')
conversation.predict(input='小明和小刚一共有几只宠物?')

dicts = messages_to_dict(history.messages)
print(dicts)
new_messages = messages_from_dict(dicts)
print(new_messages)
