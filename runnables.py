from langchain_core.runnables import RunnableSequence, RunnableBranch, RunnableLambda, RunnableParallel, RunnablePassthrough
from langchain_openai import OpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

load_dotenv()

model = OpenAI()

class data(BaseModel):
    st : int = Field(description= 'what is the name of this')
    
    
parser = PydanticOutputParser(pydantic_object=data)

prompt1 = PromptTemplate(template='what is the name of this {topic}', input_variables= ['topic'])

prompt2 = PromptTemplate(template='summarise about positive {thing}', input_variables= ['thing'])

prompt3 = PromptTemplate(template='summarise this negative {over}', input_variables= ['over'])

new = RunnableParallel(
    'first': RunnableSequence(prompt1, model , parser, prompt2, model , parser)
    'second': RunnableSequence(prompt1, model , parser, prompt3, model , parser)
    )

result = new.invoke({'topic' : 'cricket'})

result2 = RunnableBranch(
    (lambda x: (x.st) > 12 , RunnableSequence(prompt2, model , parser)),
    RunnablePassthrough
)

print("i have done it so i am printing this as hardcoded")