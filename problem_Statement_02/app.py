import streamlit as st
from rag import PDFRAG

st.set_page_config(
    page_title="PDF Chatbot",
    page_icon="📄"
)

st.title("📄 PDF Chatbot")

# Initialize RAG object
if "rag" not in st.session_state:
    st.session_state.rag = PDFRAG()

# Track PDF processing
if "pdf_processed" not in st.session_state:
    st.session_state.pdf_processed = False

# Upload PDF
uploaded_pdf = st.file_uploader(
    "Upload a PDF",
    type=["pdf"]
)

# Process PDF
if uploaded_pdf is not None and not st.session_state.pdf_processed:

    with st.spinner("Processing PDF..."):

        st.session_state.rag.process_pdf(uploaded_pdf)
        st.session_state.pdf_processed = True

    st.success("PDF processed successfully!")

# Ask Questions
if st.session_state.pdf_processed:

    question = st.text_input(
        "Ask a question from the PDF"
    )

    if st.button("Get Answer"):

        if question:

            with st.spinner("Thinking..."):

                answer = st.session_state.rag.ask(question)

            st.subheader("Answer")
            st.write(answer)