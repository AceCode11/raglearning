'''used when the text is in form of code,markdown etc'''


from langchain_text_splitters import RecursiveCharacterTextSplitter , Language

text = '''
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('sample.pdf')

docs = loader.load()

print(len(docs))

print(docs[0].page_content)

print(docs[0].metadata)

'''

splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON , 
    chunk_size = 100 , 
    chunk_overlap = 0
)

chubnks = splitter.split_text(text)
print(len(chubnks))
print(chubnks[1])