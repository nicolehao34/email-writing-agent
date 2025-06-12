# A class that consists of all the agents and their tools.

from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_groq import ChatGroq
from langchain_chroma import Chroma
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from .structure_outputs import *
from .prompts import *


class Agents():
    def __init__(self):
        # Choose which LLMs to use for each agent (GPT-4o, Gemini, LLAMA3,...)
        llama = ChatGroq(model_name="llama-3.3-70b-versatile", temperature=0.1)
        gemini = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.1)
        
        # QA Assistant chat
        
        
        # Categorize Email Chain
        
        # Query design for RAG retrieval
        
        # Generate answers to queries (using RAG)
        
        # compose a draft email based on category and related informations
        
        
        # Verify the generated email