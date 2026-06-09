from langchain_community.document_loaders import PyPDFLoader , DirectoryLoader


loader = DirectoryLoader(
    path = "//path of the directory" , 
    glob = ".pdf" , 
    loader_cls=PyPDFLoader
)

docs = loader.lazy_load()

print(len(docs[0]))

print(docs[0].metadata)

print(docs[0].page_content)

for document in docs:
    print(document.metadeta)


