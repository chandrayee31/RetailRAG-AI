from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import Chroma


def get_retriever(persist_directory="vectorstore", k=3):
    embeddings = OllamaEmbeddings(model="nomic-embed-text")

    vectorstore = Chroma(
        persist_directory=persist_directory,
        embedding_function=embeddings
    )

    retriever = vectorstore.as_retriever(search_kwargs={"k": k})
    return retriever