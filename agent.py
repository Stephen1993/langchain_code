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
from dotenv import load_dotenv
load_dotenv()

llm = OpenAI(temperature=0)
tools = load_tools(['serpapi', 'llm-math'], llm=llm)
agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True, max_iterations=3)
print(agent.agent.llm_chain.prompt.template)
agent.run('谁是莱昂纳多·迪卡普里奥的女朋友？她当前的年龄的2次方是多少？')



