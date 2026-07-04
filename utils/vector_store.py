import os
from langchain_chroma import Chroma

CHROMA_DB_PATH = "chroma_db"


def create_vector_store(chunks, embedding_model):
    """
    Create or load the Chroma vector database.
    """

    if not os.path.exists(CHROMA_DB_PATH):
        os.makedirs(CHROMA_DB_PATH)

    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory=CHROMA_DB_PATH
    )

    return vector_store