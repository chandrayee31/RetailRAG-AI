# RetailRAG AI

RetailRAG AI is a Retrieval-Augmented Generation (RAG) knowledge assistant built with FastAPI, ChromaDB, Ollama, and LangChain.

The system ingests text documents, splits them into chunks, generates embeddings, stores them in a vector database, retrieves relevant context for user questions, and produces grounded answers using a locally hosted LLM.

## Features

- Document ingestion using `.txt` files
- Text chunking for retrieval
- Embedding generation with Ollama
- Vector storage using ChromaDB
- Retrieval pipeline for relevant context
- LLM-based answer generation
- FastAPI endpoints for asking questions and ingesting documents
- Logging for observability
- Docker support for deployment

## Architecture

```text
Documents
   ↓
Loader
   ↓
Chunking
   ↓
Embeddings
   ↓
Chroma Vector Store
   ↓
Retriever
   ↓
Prompt Builder
   ↓
Ollama
   ↓
Answer with Sources
Tech Stack

Python

FastAPI

LangChain

ChromaDB

Ollama

Pydantic

Docker

Project Structure
retailrag-ai/
│
├── app/
│   ├── main.py
│   ├── services/
│   ├── models/
│   └── utils/
├── data/
│   └── docs/
├── vectorstore/
├── tests/
├── requirements.txt
├── Dockerfile
└── README.md
API Endpoints
GET /health

Returns API health status.

POST /ask

Accepts a user question and returns a RAG-based answer with retrieved source snippets.

Example request:

{
  "question": "What is the refund policy?"
}
POST /ingest

Uploads a .txt file, stores it in data/docs, and refreshes the vector store.

How It Works

Load documents from data/docs

Split documents into chunks

Generate embeddings for chunks

Store embeddings in ChromaDB

Retrieve relevant chunks for a user question

Build a grounded prompt

Generate the final answer using Ollama

Run Locally

Install dependencies:

pip install -r requirements.txt

Start the API:

uvicorn app.main:app --reload

Open Swagger UI:

http://127.0.0.1:8000/docs
Run with Docker

Build:

docker build -t retailrag-ai .

Run:

docker run -p 8000:8000 retailrag-ai
Future Improvements

PDF and Markdown ingestion

Source metadata in responses

Hybrid retrieval

Reranking

Chat memory

Evaluation pipeline

Multi-document support with filters

Author

Chandrayee Kumar