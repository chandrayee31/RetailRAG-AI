from fastapi import FastAPI, UploadFile, File, HTTPException
import os

from app.services.loader_service import load_documents
from app.services.chunk_service import split_documents
from app.services.embedding_service import create_vectorstore
from app.services.retrieval_service import get_retriever
from app.services.prompt_service import build_rag_prompt
from app.services.llm_service import generate_rag_answer

from app.utils.logger import logger

from app.models.request_model import QuestionRequest
from app.models.response_model import AskResponse, IngestResponse


app = FastAPI(title="RetailRAG AI")


@app.on_event("startup")
def startup_event():
    logger.info("Starting RetailRAG AI...")

    docs = load_documents()
    logger.info(f"Loaded {len(docs)} documents")

    chunks = split_documents(docs)
    logger.info(f"Created {len(chunks)} chunks")

    create_vectorstore(chunks)
    logger.info("Vector store created successfully")


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/ask", response_model=AskResponse)
def ask_question(request: QuestionRequest):
    logger.info(f"Received question: {request.question}")

    retriever = get_retriever()
    docs = retriever.get_relevant_documents(request.question)
    logger.info(f"Retrieved {len(docs)} relevant documents")

    prompt = build_rag_prompt(request.question, docs)
    answer = generate_rag_answer(prompt)

    sources = [doc.page_content[:200] for doc in docs]

    return AskResponse(
        question=request.question,
        answer=answer,
        sources=sources
    )


@app.post("/ingest", response_model=IngestResponse)
async def ingest_document(file: UploadFile = File(...)):
    if not file.filename.endswith(".txt"):
        raise HTTPException(status_code=400, detail="Only .txt files are supported.")

    file_path = os.path.join("data/docs", file.filename)

    try:
        content = await file.read()

        with open(file_path, "wb") as f:
            f.write(content)

        logger.info(f"Uploaded file saved: {file.filename}")

        docs = load_documents()
        chunks = split_documents(docs)
        create_vectorstore(chunks)

        logger.info("Vector store refreshed after ingestion")

        return IngestResponse(
            message="Document ingested successfully",
            filename=file.filename
        )

    except Exception as e:
        logger.exception("Error during document ingestion")
        raise HTTPException(status_code=500, detail=str(e))