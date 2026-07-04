import os

import streamlit as st
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv()


def get_embedding_model():

    api_key = os.getenv("GOOGLE_API_KEY")

    if not api_key:
        api_key = st.secrets["GOOGLE_API_KEY"]

    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/embedding-001",
        google_api_key=api_key
    )

    return embeddings