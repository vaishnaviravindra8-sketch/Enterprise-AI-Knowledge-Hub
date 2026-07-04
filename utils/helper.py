import os
import shutil


def delete_knowledge_base():

    folders = ["uploads", "chroma_db"]

    for folder in folders:

        if os.path.exists(folder):

            shutil.rmtree(folder, ignore_errors=True)

            os.makedirs(folder, exist_ok=True)