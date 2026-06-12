# PDF Chatbot using RAG

## Overview

This project is a Retrieval-Augmented Generation (RAG) based PDF Chatbot built using LangChain, ChromaDB, Gemini, and Streamlit.

The application allows users to upload a PDF document and ask questions related to its content. Instead of relying solely on the language model's pretrained knowledge, the system retrieves relevant information from the uploaded document and uses it to generate context-aware responses.

## Features

* Dynamic PDF upload
* PDF text extraction
* Document chunking
* Semantic search using embeddings
* Vector storage with ChromaDB
* Question answering using Gemini
* Streamlit-based interface

## Technologies Used
Python
Streamlit
LangChain
ChromaDB
Google Gemini
PyPDF

## Running the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

## How It Works

1. The user uploads a PDF document.
2. The PDF content is extracted and converted into documents.
3. Documents are split into smaller chunks.
4. Embeddings are generated for each chunk.
5. The embeddings are stored in ChromaDB.
6. When a question is asked, relevant chunks are retrieved using semantic search.
7. The retrieved context is passed to Gemini.
8. Gemini generates an answer based on the retrieved information.


## Learning Outcomes

This project demonstrates the implementation of:

* Retrieval-Augmented Generation (RAG)
* Document Processing
* Text Chunking
* Embeddings
* Vector Databases
* Semantic Search
* Large Language Model Integration
* LangChain Workflows


