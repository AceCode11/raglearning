import streamlit as st
from retriever import create_hybrid_retriever

st.set_page_config(
    page_title="Azure Bicep Assistant",
    page_icon="📘",
    layout="wide"
)

st.title("Azure Bicep Documentation Assistant")

st.write(
    "Ask questions about Azure Bicep documentation."
)

# Load retriever once
@st.cache_resource
def load_retriever():
    return create_hybrid_retriever()

hybrid_retriever = load_retriever()

query = st.text_input(
    "Ask a question",
    placeholder="What is BCP187?"
)

if st.button("Search"):

    if query:

        with st.spinner("Searching documentation..."):

            results = hybrid_retriever.invoke(query)

        st.subheader("Retrieved Results")

        for i, doc in enumerate(results):

            with st.expander(f"Result {i+1}"):

                st.write(doc.page_content)

                if "source" in doc.metadata:

                    st.caption(
                        f"Source: {doc.metadata['source']}"
                    )