from langchain_community import duckduckgo_search
from langchain_core import tool
from langchain_openai import chat_models
from langchain.tools import StructuredTool
from pydantic import BaseModel, Field
from langchain.tools import BaseTool
from typing import Type
from langchain.agents import initialize_agent, AgentType

#this is using decorator
@tool
def multiply(x : int, y : int) -> int:
    """this is to multiply 2 numbers"""
    return x * y


class Addition(BaseModel):
    a : int = Field(required=True, description="The first number to add")
    b: int = Field(required=True, description="The second number to add")
    
def multiply(x : int, y : int) -> int:
    return x * y

multiply_tool = StructuredTool.from_function(
    function = multiply,
    name = "multiply",
    description = "Multiply two numbers",
    args_schema = Addition
)

class multiplytool(BaseTool):
    name : str = "multiply"
    description : str = "this is to multiply two numbers"
    args_schema : type[BaseModel] = Addition
    
    def _run(self, a: int, b: int) -> int:
        return a * b

@tool
def addition(a: int , b: int) -> int:
    """this is for the addition"""
    return a+ b

class multiplytool:
    def get_tools(self):
        return [addition, multiply]
    
data = multiplytool()

tools = data.get_tools()

for tool in tools:
    for tool in tools:
        print(tool.name, "=>", tool.description)


agent = initialize_agent(
    llm = llm,
    tools = [multiply, addition],
    agent = AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
    verbose = True
)

data = agent.invoke({"input": query})