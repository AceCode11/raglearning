from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel, RunnablePassthrough, RunnableLambda
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

def build_rag(video_id):

    ytt_api = YouTubeTranscriptApi()

    transcript_list = ytt_api.fetch(
        video_id,
        languages=['en']
    )

    transcript = " ".join(
        chunk.text for chunk in transcript_list
    )

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    docs = splitter.create_documents([transcript])

    embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")
    vector_store = FAISS.from_documents(docs,embeddings)

    retriever = vector_store.as_retriever()

    def format_docs(docs):
        return "\n\n".join(
            doc.page_content for doc in docs
        )

    parallel_chain = RunnableParallel({
        "context":retriever | RunnableLambda(format_docs),

        "question":
            RunnablePassthrough()
    })

    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

    prompt = PromptTemplate(
        template="""
You are a helpful assistant.

Answer only from the provided transcript.

If the answer is not available,
say "I don't know".

Context:
{context}

Question:
{question}
""",

        input_variables=["context","question"])

    parser = StrOutputParser()

    chain = (parallel_chain | prompt | llm | parser
    )

    return chain