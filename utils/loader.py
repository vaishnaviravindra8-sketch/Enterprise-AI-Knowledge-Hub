import os

from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader,
    Docx2txtLoader,
    UnstructuredHTMLLoader
)

UPLOAD_FOLDER = "uploads"


def save_uploaded_files(uploaded_files):
    """
    Save uploaded files to uploads folder.
    """

    os.makedirs(UPLOAD_FOLDER, exist_ok=True)

    saved_paths = []

    for uploaded_file in uploaded_files:

        file_path = os.path.join(
            UPLOAD_FOLDER,
            uploaded_file.name
        )

        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        saved_paths.append(file_path)

    return saved_paths


def load_documents(file_paths):
    """
    Read uploaded documents.
    """

    documents = []

    for file_path in file_paths:

        extension = file_path.split(".")[-1].lower()

        if extension == "pdf":
            loader = PyPDFLoader(file_path)

        elif extension == "docx":
            loader = Docx2txtLoader(file_path)

        elif extension in ["txt", "md"]:
            loader = TextLoader(file_path)

        elif extension == "html":
            loader = UnstructuredHTMLLoader(file_path)

        else:
            continue

        documents.extend(loader.load())

    return documents