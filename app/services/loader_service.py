from langchain_community.document_loaders import TextLoader


from pathlib import Path

def load_documents(doc_path="data/docs"):
    documents = []

    for file in Path(doc_path).glob("*.txt"):
        loader = TextLoader(file)
        documents.extend(loader.load())

    return documents

