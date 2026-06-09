from langchain_community.document_loaders import WebBaseLoader
from langchain_community.document_loaders import TextLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv


load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash") 

prompt = PromptTemplate(
    template="answer the following question -\n {question} from the foll text -\n {text}",
    input_variables=['question' , 'text']
)

parser = StrOutputParser()
loader = TextLoader('sample.txt', encoding='utf-8')


url = "https://www.samsung.com/in/smartphones/galaxy-s26-ultra/"


loader = WebBaseLoader(
    url
)

docs  = loader.load()

'''
print(len(docs))

print(docs[0].page_content)
'''

chain = prompt | model | parser

print(chain.invoke(
    {
        'question':'which processor is used in the product?' , 
        'text' : docs[0].page_content
    }
)
)
