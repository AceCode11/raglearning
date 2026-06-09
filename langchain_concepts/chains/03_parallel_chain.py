from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from langchain_core.runnables import RunnableParallel

load_dotenv()


model1 = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

model2 = ChatGroq(model="llama-3.3-70b-versatile")

prompt1 = PromptTemplate(
    template = "Generate short and simple note from the foll text \n {text}" , 
    input_variables = ['text']
)

prompt2 = PromptTemplate(
    template = "Generate short question answers from the followwing text \n {text}" , 
    input_variables= ['text']
)

prompt3 = PromptTemplate(
    template = "merge the provided notes and quiz into a single document \n {notes} and {quiz}" ,
    input_variables =['notes' , 'quiz']
)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'notes' : prompt1 | model1 | parser , 
    'quiz' : prompt2 | model2 | parser
})

merge_chain = prompt3 |model1 | parser

chain = parallel_chain | merge_chain

text = '''Retrieval-augmented generation (RAG) is a technique that enables large language models (LLMs) to retrieve and incorporate new information from external data sources.[1] With RAG, LLMs first refer to a specified set of documents, then respond to user queries. These documents supplement information from the LLM's pre-existing training data.[2] This allows LLMs to use domain-specific and/or updated information that is not available in the training data.[2] For example, this enables LLM-based chatbots to access internal company data or generate responses based on authoritative sources.
RAG improves LLMs by incorporating information retrieval before generating responses.[3] Unlike LLMs that rely on static training data, RAG pulls relevant text from databases, uploaded documents, or web sources.[1] According to Ars Technica, "RAG is a way of improving LLM performance, in essence by blending the LLM process with a web search or other document look-up process to help LLMs stick to the facts." This method helps reduce AI hallucinations,[3] which have caused chatbots to describe policies that don't exist, or recommend nonexistent legal cases to lawyers that are looking for citations to support their arguments.
RAG also reduces the need to retrain LLMs with new data, saving on computational and financial costs.[1] Beyond efficiency gains, RAG also allows LLMs to include sources in their responses, so users can verify the cited sources. This provides greater transparency, as users can cross-check retrieved content to ensure accuracy and relevance.
'''
result = chain.invoke({'text' : text})
print(result)