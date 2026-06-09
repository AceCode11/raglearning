import streamlit as st

from rag import build_rag
from utils import extract_video_id


st.set_page_config(
    page_title="YouTube RAG Chatbot",
    page_icon="🎥",
    layout="wide"
)

st.title("🎥 YouTube RAG Chatbot")

st.write(
    "Paste a YouTube URL and ask questions about the video."
)


# Session State
if "chain" not in st.session_state:
    st.session_state.chain = None

if "video_loaded" not in st.session_state:
    st.session_state.video_loaded = False


# URL Input
video_url = st.text_input(
    "Paste YouTube URL"
)


# Load Video Button
if st.button("Load Video"):

    if not video_url:

        st.error("Please enter a YouTube URL")

    else:

        video_id = extract_video_id(video_url)

        if not video_id:

            st.error("Invalid YouTube URL")

        else:

            try:

                with st.spinner(
                    "Fetching transcript and creating vector database..."
                ):

                    st.session_state.chain = build_rag(
                        video_id
                    )

                    st.session_state.video_loaded = True

                st.success(
                    "Video loaded successfully!"
                )

            except Exception as e:

                st.error(
                    f"Error: {str(e)}"
                )


# Question Section
if st.session_state.video_loaded:

    st.divider()

    question = st.text_input(
        "Ask a question about the video"
    )

    if st.button("Ask"):

        if question:

            with st.spinner(
                "Thinking..."
            ):

                try:

                    answer = (
                        st.session_state.chain
                        .invoke(question)
                    )

                    st.subheader("Answer")

                    st.write(answer)

                except Exception as e:

                    st.error(
                        f"Error: {str(e)}"
                    )