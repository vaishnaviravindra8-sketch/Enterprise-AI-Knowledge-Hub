from utils.retriever import get_retriever
from utils.embeddings import get_embedding_model
from utils.llm import get_llm


def ask_question(question):

    embedding_model = get_embedding_model()
    
    retriever = get_retriever(embedding_model)

    docs = retriever.invoke(question)

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    prompt = f"""
You are an Enterprise AI Knowledge Assistant.

Answer ONLY using the context below.

If the answer is not found, say:
"I couldn't find this information in the uploaded documents."

Context:
{context}

Question:
{question}

Answer:
"""

    llm = get_llm()

    response = llm.invoke(prompt)

    return response.content, docs