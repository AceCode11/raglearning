from ingest import load_and_chunk

from langchain_community.retrievers import BM25Retriever
from langchain_community.vectorstores import FAISS
from langchain_classic.retrievers import EnsembleRetriever
from langchain_community.embeddings import HuggingFaceEmbeddings



def create_hybrid_retriever():
    chunks = load_and_chunk()
    print(f"loaded {len(chunks)} chunks")


    bm25_retriever = BM25Retriever.from_documents(chunks)

    bm25_retriever.k = 4
    
    

    embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

    vector_store = FAISS.from_documents(chunks , embeddings)

    vector_retriever = vector_store.as_retriever(search_kwargs={"k" : 4})

    hybrid_retriever = EnsembleRetriever(
        retrievers = [
            bm25_retriever , 
            vector_retriever
        ] , 
        weights=[0.5 , 0.5]
    )

    return hybrid_retriever
