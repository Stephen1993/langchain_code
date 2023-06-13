from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from dotenv import load_dotenv
load_dotenv()

embeddings = OpenAIEmbeddings()
text = '你好'

query_result = embeddings.embed_query(text)
doc_result = embeddings.embed_documents([text])

print(query_result)
print(doc_result)