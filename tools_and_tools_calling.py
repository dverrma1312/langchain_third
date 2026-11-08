from langchain_community import duckduckgo_search
from langchain_core import tool
from langchain_openai import chat_models
from langchain.tools import StructuredTool
from pydantic import BaseModel, Field


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

