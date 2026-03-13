from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import Chroma


def create_vectorstore(chunks, persist_directory="vectorstore"):
    # embeddings = OllamaEmbeddings(model="nomic-embed-text") for local running
    embeddings = OllamaEmbeddings(
    model="nomic-embed-text",
    base_url="http://host.docker.internal:11434"
) # for docker

    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=persist_directory
    )

    return vectorstore