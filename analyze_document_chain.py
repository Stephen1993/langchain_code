from langchain import OpenAI
from langchain.chains.summarize import load_summarize_chain
from langchain.chains import AnalyzeDocumentChain
from langchain.chains.question_answering import load_qa_chain

with open("../../state_of_the_union.txt") as f:
    state_of_the_union = f.read()

llm = OpenAI(temperature=0)
summary_chain = load_summarize_chain(llm, chain_type="map_reduce")

summarize_document_chain = AnalyzeDocumentChain(combine_docs_chain=summary_chain)
summarize_document_chain.run(state_of_the_union)
