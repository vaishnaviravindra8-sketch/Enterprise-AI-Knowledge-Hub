import streamlit as st

from utils.loader import save_uploaded_files, load_documents
from utils.splitter import split_documents
from utils.embeddings import get_embedding_model
from utils.vector_store import create_vector_store
from utils.rag import ask_question
from utils.helper import delete_knowledge_base

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Enterprise AI Knowledge Hub",
    page_icon="📚",
    layout="wide"
)

# =====================================================
# SESSION STATE
# =====================================================

if "knowledge_base_ready" not in st.session_state:
    st.session_state.knowledge_base_ready = False

if "uploaded_once" not in st.session_state:
    st.session_state.uploaded_once = False

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "saved_files" not in st.session_state:
    st.session_state.saved_files = []

if "documents" not in st.session_state:
    st.session_state.documents = []

if "chunks" not in st.session_state:
    st.session_state.chunks = []

# =====================================================
# HEADER
# =====================================================

st.title("📚 Enterprise AI Knowledge Hub")
st.markdown("### AI-Powered Enterprise Document Assistant")
st.markdown("---")

# =====================================================
# SIDEBAR
# =====================================================

st.sidebar.title("📚 Enterprise AI Knowledge Hub")

st.sidebar.markdown("---")

st.sidebar.subheader("📂 Upload Documents")

uploaded_files = st.sidebar.file_uploader(
    "Choose Files",
    type=["pdf", "docx", "txt", "md", "html"],
    accept_multiple_files=True
)

st.sidebar.markdown("---")

if st.session_state.knowledge_base_ready:
    st.sidebar.success("🟢 Knowledge Base Ready")
else:
    st.sidebar.warning("🟡 Waiting for documents...")

# =====================================================
# BUILD KNOWLEDGE BASE
# =====================================================

if uploaded_files and not st.session_state.uploaded_once:

    with st.spinner("Building Knowledge Base..."):

        saved_files = save_uploaded_files(uploaded_files)

        documents = load_documents(saved_files)

        chunks = split_documents(documents)
        if len(chunks) == 0:

           st.error(
            "No readable text was found in the uploaded PDF. "
            "It may be a scanned document or image-based PDF."
           )
           st.stop()

        embedding_model = get_embedding_model()

        create_vector_store(
            chunks,
            embedding_model
        )

        st.session_state.saved_files = saved_files
        st.session_state.documents = documents
        st.session_state.chunks = chunks

        st.session_state.uploaded_once = True
        st.session_state.knowledge_base_ready = True

    st.rerun()

# =====================================================
# DASHBOARD
# =====================================================

if st.session_state.knowledge_base_ready:

    st.success("✅ Knowledge Base Ready!")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Documents",
            len(st.session_state.saved_files)
        )

    with col2:
        st.metric(
            "Pages",
            len(st.session_state.documents)
        )

    with col3:
        st.metric(
            "Chunks",
            len(st.session_state.chunks)
        )

    st.markdown("---")

    st.subheader("📄 Uploaded Documents")

    for file in st.session_state.saved_files:
        st.write(f"📄 {file}")
        # =====================================================
# ASK QUESTIONS
# =====================================================

st.markdown("---")
st.header("💬 Ask Questions")

with st.form("question_form"):

    question = st.text_input(
        "Ask anything about your uploaded documents..."
    )

    submitted = st.form_submit_button("Ask")

if submitted:

    if not st.session_state.knowledge_base_ready:

        st.warning("Please upload documents first.")

    elif question.strip() == "":

        st.warning("Please enter a question.")

    else:

        with st.spinner("Searching documents and generating answer..."):

            answer, docs = ask_question(question)

        st.session_state.chat_history.append(
            {
                "question": question,
                "answer": answer,
                "sources": docs
            }
        )

        st.rerun()

# =====================================================
# CHAT HISTORY
# =====================================================

if st.session_state.chat_history:

    st.markdown("---")
    st.header("💬 Conversation")

    for chat in reversed(st.session_state.chat_history):

        with st.chat_message("user"):
            st.write(chat["question"])

        with st.chat_message("assistant"):

            st.write(chat["answer"])

            st.markdown("#### 📄 Sources")

            shown = set()

            for doc in chat["sources"]:

                source = doc.metadata.get("source", "Unknown")
                page = doc.metadata.get("page", None)

                key = (source, page)

                if key in shown:
                    continue

                shown.add(key)

                if page is not None:
                    st.caption(f"📄 {source} | Page {page + 1}")
                else:
                    st.caption(f"📄 {source}")

                with st.expander("View Retrieved Text"):

                    st.write(doc.page_content)

        st.markdown("---")

# =====================================================
# SIDEBAR ACTIONS
# =====================================================

st.sidebar.markdown("---")

if st.sidebar.button("🗑 Clear Chat"):

    st.session_state.chat_history = []

    st.rerun()

if st.sidebar.button("🗑 Delete Knowledge Base"):

    delete_knowledge_base()

    st.session_state.chat_history = []
    st.session_state.saved_files = []
    st.session_state.documents = []
    st.session_state.chunks = []

    st.session_state.uploaded_once = False
    st.session_state.knowledge_base_ready = False

    st.rerun()

# =====================================================
# FOOTER
# =====================================================

st.sidebar.markdown("---")

st.sidebar.caption("Enterprise AI Knowledge Hub")

st.sidebar.caption("Built with")

st.sidebar.write("✅ Streamlit")
st.sidebar.write("✅ LangChain")
st.sidebar.write("✅ ChromaDB")
st.sidebar.write("✅ Gemini")
st.sidebar.write("✅ HuggingFace Embeddings")