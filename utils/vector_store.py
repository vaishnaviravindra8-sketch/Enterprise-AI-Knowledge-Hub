from langchain_community.vectorstores import FAISS


def create_vector_store(chunks, embedding_model):
    """
    Create the FAISS vector database.
    """

    vector_store = FAISS.from_documents(
        documents=chunks,
        embedding=embedding_model
    )

    vector_store.save_local("faiss_index")

    return vector_store