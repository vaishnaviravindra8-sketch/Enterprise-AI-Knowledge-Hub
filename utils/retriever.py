from langchain_community.vectorstores import FAISS
from utils.embeddings import get_embedding_model


def get_retriever(embedding_model=None):
    """
    Load the FAISS vector database and return a retriever.
    """

    if embedding_model is None:
        embedding_model = get_embedding_model()

    vector_store = FAISS.load_local(
        "faiss_index",
        embedding_model,
        allow_dangerous_deserialization=True
    )

    return vector_store.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 4}
    )