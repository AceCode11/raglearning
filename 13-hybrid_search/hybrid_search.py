from langchain_core.documents import Document
from langchain_community.retrievers import BM25Retriever
from langchain_community.vectorstores import FAISS
from langchain_classic.retrievers import EnsembleRetriever
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_community.embeddings import HuggingFaceEmbeddings



load_dotenv()
docs = [

    Document(
        page_content="AWS EC2 is a cloud computing service that provides virtual machines."
    ),

    Document(
        page_content="Docker is a platform used for containerization."
    ),

    Document(
        page_content="Kubernetes is used to orchestrate containers across multiple servers."
    ),

    Document(
        page_content="BCP187 is an Azure Bicep deployment error."
    ),

    Document(
        page_content="Terraform is an Infrastructure as Code tool."
    ),

    Document(
        page_content="Random Forest is an ensemble machine learning algorithm."
    )
]

#bm25 retriver
bm25_retriever = BM25Retriever.from_documents(docs)

bm25_retriever.k = 2

#vector search

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

vectorstore = FAISS.from_documents(docs , embeddings)

vector_retriver = vectorstore.as_retriever(search_kwargs = {"k":2})

#hybrid retriever
hybrid_retriever = EnsembleRetriever(
    retrievers = [
        bm25_retriever , vector_retriver
    ] , 
    weights = [
        0.5 , 0.5
    ]
)

query = input("Ask Question: ")


#bm25 results
bm25_results = bm25_retriever.invoke(query)

for doc in bm25_results:
    print(doc.page_content)
    print()

#vector results
vector_results = vector_retriver.invoke(query)

for doc in vector_results:
    print(doc.page_content)
    print()

#hybrid results
hybrid_results = hybrid_retriever.invoke(query)

for doc in hybrid_results:
    print(doc.page_content)
    print()

