import os
import shutil


def delete_knowledge_base():
    """
    Delete uploads folder and FAISS index.
    """

    folders = [
        "uploads",
        "faiss_index"
    ]

    for folder in folders:

        if os.path.exists(folder):

            shutil.rmtree(folder, ignore_errors=True)

            os.makedirs(folder, exist_ok=True)