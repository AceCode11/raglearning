# RAG Learning

A collection of hands-on lessons covering the core building blocks of Retrieval-Augmented Generation (RAG) using LangChain and Google Gemini. Each folder is a self-contained lesson that focuses on one specific concept.

## Lessons

### 01 - Document Loader
Introduction to LangChain's `TextLoader`. Loads a text file and passes its content through a Gemini LLM chain to generate a summary.

### 02 - PyPDF Loader
Loading PDF documents using `PyPDFLoader`. Demonstrates how to access page content and metadata from a PDF file.

### 03 - Directory Loader
Using `DirectoryLoader` to load multiple PDF files from a directory at once, with `PyPDFLoader` as the file-level loader.

### 04 - Lazy Loading
Same as the directory loader but uses `lazy_load()` instead of `load()`. Useful for large datasets where you don't want to load everything into memory at once.

### 05 - Web Based Loader
Loading content directly from a webpage using `WebBaseLoader`. The loaded web content is then used as context to answer a question via an LLM chain.

### 06 - Text Splitter
Using `CharacterTextSplitter` to break a block of text into smaller chunks based on a specified chunk size and separator.

### 07 - Document Text Splitter (Practice)
Combining `PyPDFLoader` with `CharacterTextSplitter` to load a PDF and then split its content into chunks. Uses `split_documents()` instead of `split_text()`.

### 08 - Recursive Character Text Splitter
Using `RecursiveCharacterTextSplitter` which tries multiple separators (newlines, spaces, etc.) to create more meaningful chunks compared to the basic character splitter.

### 09 - Document Structured Splitter
Splitting structured text like code using `RecursiveCharacterTextSplitter.from_language()`. Demonstrates language-aware splitting with Python as the target language.

### 10 - Vector Store
Creating and querying a Chroma vector store. Covers adding documents with metadata, similarity search, similarity search with scores, and metadata-based filtering.

### 11 - Wikipedia Retriever
Using LangChain's `WikipediaRetriever` to fetch documents directly from Wikipedia based on a search query.

## Other Folders

### langchain_concepts
Additional lessons on LangChain fundamentals including Chat Models, Runnables, Structured Outputs, and Chains.Some of it are in the collab book so I didnt put it here will upload once I arranged everything properly

### problem_Statement_01
A complete RAG project — a YouTube video chatbot built with Streamlit, FAISS, and Gemini. Takes a YouTube URL, fetches the transcript, and answers questions about the video.

## Setup

Create a `.env` file in the root directory with your API keys:

```
GOOGLE_API_KEY=your_google_api_key
GROQ_API_KEY=your_groq_api_key
```

Install the common dependencies:


pip install langchain langchain-google-genai langchain-community python-dotenv

may require additional packages like 'faiss-cpu', 'chromadb', 'streamlit', 'youtube-transcript-api', etc.
