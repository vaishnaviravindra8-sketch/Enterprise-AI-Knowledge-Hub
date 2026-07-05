import os
import shutil
from langchain_chroma import Chroma

CHROMA_DB_PATH = "chroma_db"


def create_vector_store(chunks, embedding_model):
    """
    Create a fresh Chroma vector database.
    """

    # Remove old database completely
    if os.path.exists(CHROMA_DB_PATH):
        shutil.rmtree(CHROMA_DB_PATH, ignore_errors=True)

    # Create a new database folder
    os.makedirs(CHROMA_DB_PATH, exist_ok=True)

    # Create Chroma database
    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory=CHROMA_DB_PATH
    )

    return vector_store