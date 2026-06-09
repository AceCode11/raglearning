import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

from langchain_community.retrievers import WikipediaRetriever

retriever = WikipediaRetriever(top_k_results=2, lang='en')

# FIX: Changed from a conversational question to a direct Wikipedia page topic
query = "India–Pakistan relations"

docs = retriever.invoke(query)

print(f"Successfully retrieved {len(docs)} documents!")
print("\n--- Content Snippet ---")
print(docs[0].page_content[:400] + "...")