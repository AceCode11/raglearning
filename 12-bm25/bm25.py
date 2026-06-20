from rank_bm25 import BM25Okapi

docs = [
    "AWS EC2 is a cloud computing service",
    "Random Forest is an ensemble learning algorithm",
    "BCP187 is an Azure Bicep deployment error"

]


tokenised_docs = [doc.split() for doc in docs]

bm25 = BM25Okapi(tokenised_docs)


query = "What is BCP187".split()

scores = bm25.get_scores(query)

print(scores)