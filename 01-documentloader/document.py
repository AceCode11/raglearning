import os
import warnings
from dotenv import load_dotenv

load_dotenv()

warnings.filterwarnings("ignore", category=DeprecationWarning)

from langchain_community.document_loaders import TextLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash") 

prompt = PromptTemplate(
    template="Write a summary for following text -\n {poem}",
    input_variables=['poem']
)

parser = StrOutputParser()
loader = TextLoader('sample.txt', encoding='utf-8')

docs = loader.load()

chain = prompt | model | parser

print("--- Executing Secure Free Gemini Pipeline ---")
print(chain.invoke({'poem': docs[0].page_content}))