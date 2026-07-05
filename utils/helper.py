import os
import shutil
import tempfile

CHROMA_DB_PATH = os.path.join(tempfile.gettempdir(), "enterprise_ai_chroma")


def delete_knowledge_base():

    folders = [
        "uploads",
        CHROMA_DB_PATH
    ]

    for folder in folders:

        if os.path.exists(folder):

            shutil.rmtree(folder, ignore_errors=True)

            os.makedirs(folder, exist_ok=True)