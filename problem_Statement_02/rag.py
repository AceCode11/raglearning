from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_classic.chains import RetrievalQA
import tempfile
from dotenv import load_dotenv

load_dotenv()

class PDFRAG:

    def __init__(self):
        self.vectorstore = None
        self.qa_chain = None

    def process_pdf(self , uploaded_pdf):
        with tempfile.NamedTemporaryFile(
            delete = False , 
            suffix = ".pdf"
        ) as temp_file:
            

            temp_file.write(uploaded_pdf.getvalue())
            temp_pdf_path = temp_file.name

        loader = PyPDFLoader(temp_pdf_path)

        documents = loader.load()


        splitter = RecursiveCharacterTextSplitter(
            chunk_size = 1000 , 
            chunk_overlap = 200
        )


        chunks = splitter.split_documents(documents)

        embeddings = GoogleGenerativeAIEmbeddings(
            model="models/gemini-embedding-001"
        )

        self.vectorstore = Chroma.from_documents(
            documents = chunks , 
            embedding = embeddings,
            collection_name="pdf_chatbot"

        )


        retriever = self.vectorstore.as_retriever(
            search_kwargs = {"k" : 4}
        )

        llm = ChatGoogleGenerativeAI(
                model="gemini-2.5-flash",

        )

        self.qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff"
         ) 
    
    
    def ask(self, question):
        if self.qa_chain is None:
            return "Please upload a PDF first."

        response = self.qa_chain.invoke(
        {"query": question}
    )

        return response["result"]

        