from langchain_core.runnables import RunnableSequence, RunnableBranch, RunnableLambda, RunnableParallel, RunnablePassthrough
from langchain_openai import chatOpenAI, OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain_core.prompts import PromptTemplate
from langchain.schema import Documents
from dotenv import load_dotenv
from langchain_core.output_parsers import PydanticOutputParser, strOutputParser
from pydantic import BaseModel, Field
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader, WebBaseLoader

load_dotenv()

model = chatOpenAI()

prompt = PromptTemplate(template='what is the name of this {topic}', input_variables= ['topic'])

parser = strOutputParser()

doc = Documents(
    page_content = '',
    metadata = {'data': 'dtat'}
)

vector= Chroma(
    embedding_function = OpenAIEmbeddings,
    Persistdirectory = 'vector_db',
    collection_name = 'first'
)

vector.add_documetnts(doc)

vector.get(include= [])

vector.similarity_search(query = "", k= 8)

vector.update_documents(document_id = '', docement = updated_document)

