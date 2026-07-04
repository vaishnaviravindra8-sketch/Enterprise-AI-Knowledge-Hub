# 📚 Enterprise AI Knowledge Hub

## Overview
Enterprise AI Knowledge Hub is an AI-powered document question-answering system built using Retrieval-Augmented Generation (RAG). Users can upload enterprise documents such as PDF, DOCX, TXT, Markdown, and HTML files, and ask questions in natural language. The system retrieves the most relevant information from the uploaded documents and generates accurate responses using Google's Gemini AI model.

## Features
- Upload multiple documents
- Supports PDF, DOCX, TXT, Markdown, and HTML
- Automatic document processing
- Intelligent text chunking
- Semantic search using vector embeddings
- ChromaDB vector database
- AI-powered answers using Gemini
- Displays source documents and page numbers
- Chat history
- Delete knowledge base
- Clean and interactive Streamlit interface

## Technologies Used
- Python
- Streamlit
- LangChain
- ChromaDB
- HuggingFace Embeddings
- Google Gemini API
- Sentence Transformers

## Project Structure

Enterprise-AI-Knowledge-Hub/
│
├── app.py
├── requirements.txt
├── README.md
├── .env.example
│
├── assets/
├── uploads/
├── chroma_db/
│
└── utils/
    ├── loader.py
    ├── splitter.py
    ├── embeddings.py
    ├── vector_store.py
    ├── retriever.py
    ├── llm.py
    ├── rag.py
    └── helper.py


## Installation
Clone the repository

```bash
git clone <repository-link>
```

Go to the project folder

```bash
cd Enterprise-AI-Knowledge-Hub
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate it

Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file using `.env.example`

```env
GOOGLE_API_KEY=YOUR_API_KEY
Run the application

```bash
streamlit run app.py
```

## Future Enhancements
- Support more document formats
- Conversation memory
- User authentication
- Cloud deployment
- Document summarization


## Author

**Vaishnavi_R**
Major Internship Project