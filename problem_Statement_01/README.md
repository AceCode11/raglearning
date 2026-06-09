# Problem Statement 01 - YouTube RAG Chatbot

A RAG (Retrieval-Augmented Generation) based chatbot that takes a YouTube video URL, fetches its transcript, and lets you ask questions about the video content using LangChain and Google Gemini.

## Problem Statement

Build a chatbot that can answer questions based on the transcript of any YouTube video. The system should retrieve the most relevant parts of the transcript before generating a response so that answers are accurate and context-aware.

## Project Structure

`app.py` - Streamlit frontend that handles the UI, session state, and user interaction
`rag.py` - Core RAG pipeline that fetches the transcript, chunks it, creates FAISS vector store, and builds the LLM chain
`utils.py` - Helper function to extract video ID from YouTube URLs (supports both youtube.com and youtu.be formats)

## How It Works

1. User pastes a YouTube URL in the Streamlit app
2. The video ID is extracted from the URL
3. The transcript is fetched using 'youtube-transcript-api'
4. The transcript text is split into chunks using 'RecursiveCharacterTextSplitter' (chunk size 1000, overlap 200)
5. Chunks are embedded using Google Generative AI Embeddings and stored in a FAISS vector store
6. When the user asks a question, the retriever finds the most relevant chunks
7. The chunks and question are passed to Gemini 2.5 Flash via a prompt template
8. The LLM generates an answer based only on the provided context

## Tech Stack

Streamlit (frontend)
LangChain (framework)
Google Gemini 2.5 Flash (LLM)
Google Generative AI Embeddings (embedding model)
FAISS (vector store)
youtube-transcript-api (transcript fetching)



Install the required packages:

```
pip install streamlit langchain langchain-google-genai langchain-community faiss-cpu youtube-transcript-api python-dotenv
```

Make sure you have a `.env` file in the project root with your Google API key:
