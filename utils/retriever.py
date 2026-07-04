from langchain_chroma import Chroma

CHROMA_DB_PATH = "chroma_db"


def get_retriever(embedding_model):

    vector_store = Chroma(
        persist_directory=CHROMA_DB_PATH,
        embedding_function=embedding_model
    )

    return vector_store.as_retriever(
        search_type="similarity",
        search_kwargs={"k":4}
    )
