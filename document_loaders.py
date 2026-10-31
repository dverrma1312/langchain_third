from langchain_core.runnables import RunnableSequence, RunnableBranch, RunnableLambda, RunnableParallel, RunnablePassthrough
from langchain_openai import OpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader, WebBaseLoader


load_dotenv()

model = OpenAI()

object = PyPDFLoader('C:/Users/HP/Downloads/Telegram Desktop/AI.pdf')

result = object.load()

data = DirectoryLoader(
    path = 'books',
    glob = '*.pdf',
    loader_cls= PyPDFLoader
)

result2 = data.lazy_load()

for doc in result2:
    print(doc.page_content)
    
    
url = 'some_url.///'

object1 = WebBaseLoader(url)

result3 = object1.load()

print(result3[0].page_content)