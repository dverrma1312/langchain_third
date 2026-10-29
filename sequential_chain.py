from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser


load_dotenv()  # Load environment variables from .env file

model = ChatOpenAI()

prompt = PromptTemplate(template = 'what is the latest article on {topic}', input_variables= ['topic'])
prompt2 = PromptTemplate(template = 'sink this{data}', input_variables= ['data'])

parser = StrOutputParser()

chain = prompt | model | parser | model | parser 

result = chain.invoke({'topic' : 'cricket'})

print(result)
