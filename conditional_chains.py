from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableBranch, RunnableLambda
from pydantic import BaseModel, Field
from typing import Literal

class Feedback(BaseModel):
    sentiment : Literal['positive', 'negative'] = Field(description="what is the sentiment of this")

load_dotenv()

model = ChatOpenAI()

parser = PydanticOutputParser(pydantic_object= Feedback)

prompt1 = PromptTemplate(template = 'what is the data about this {topic}', input_variables= ['topic'], partial_variables= parser.get_format_instructions())

sentiment_result = prompt1 | model | parser

prompt2 = PromptTemplate(
    template='Write an appropriate response to this positive feedback \n {feedback}',
    input_variables=['feedback']
)

prompt3 = PromptTemplate(
    template='Write an appropriate response to this negative feedback \n {feedback}',
    input_variables=['feedback']
)

final_result = RunnableBranch(
    (lambda x: x.sentiment == 'positive' , prompt2 | model | parser),
    (lambda x: x.sentiment == 'negative' , prompt3 | model | parser)
    , RunnableLambda(lambda x: "could not find sentiment")
)

chain = sentiment_result | final_result

result = chain.invoke({'topic' : 'cricket'})

print(result)

chain.get_graph.print_ascii()
