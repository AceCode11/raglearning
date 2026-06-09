from langchain_text_splitters import RecursiveCharacterTextSplitter


text = """
The field of Artificial Intelligence has been completely transformed by the 
introduction of Large Language Models (LLMs) and Retrieval-Augmented Generation 
(RAG). While traditional LLMs are limited by a static knowledge cutoff date, 
a RAG pipeline solves this bottleneck by allowing the model to dynamically 
fetch relevant facts from an external vector database before generating a 
response. This process relies heavily on initial data ingestion, where raw 
documents like PDFs, text files, and web pages are parsed using specialized 
document loaders. Once loaded, the text is broken down into smaller, semantic 
chunks, converted into high-dimensional vector embeddings, and indexed for 
lightning-fast similarity searches.

"""

splitter = RecursiveCharacterTextSplitter(
    chunk_size = 200 , 
    chunk_overlap = 0

)

chunks = splitter.split_text(text)

print(len(chunks))
print(chunks)