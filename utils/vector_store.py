import os
import shutil
import tempfile
from langchain_chroma import Chroma

CHROMA_DB_PATH = os.path.join(tempfile.gettempdir(), "enterprise_ai_chroma")


def create_vector_store(chunks, embedding_model):
    """
    Create a fresh Chroma vector database in a writable temp directory.
    """

    if os.path.exists(CHROMA_DB_PATH):
        shutil.rmtree(CHROMA_DB_PATH, ignore_errors=True)

    os.makedirs(CHROMA_DB_PATH, exist_ok=True)

    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory=CHROMA_DB_PATH
    )

    return vector_store