from langchain import PromptTemplate
from langchain.chains import LLMBashChain
from langchain.llms import OpenAI
from langchain.chains.llm_bash.prompt import BashOutputParser
from dotenv import load_dotenv
load_dotenv()

llm = OpenAI(temperature=0)
text = "Please write a bash script that prints 'Hello World' to the console."
bash_chain = LLMBashChain(llm=llm)
bash_chain.run(text)