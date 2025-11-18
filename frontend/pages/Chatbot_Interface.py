# src/pages/chatbot_interface.py
import streamlit as st
from components.chat_ui import render_messages, chat_input_area
from components.visual_components import show_sources
from utils.api_client import chat_query

def page_chatbot():
    st.title("RAG Chatbot")
    st.write("Ask NEC, Wattmonk or general questions. The bot uses retrieval-augmented generation (RAG).")
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    submitted, prompt = chat_input_area()
    col1, col2 = st.columns([3,1])
    with col2:
        top_k = st.number_input("Top K", min_value=1, max_value=20, value=5)

    if submitted and prompt.strip():
        with st.spinner("Getting answer..."):
            try:
                resp = chat_query(prompt, user_id="streamlit_user", top_k=int(top_k))
                answer = resp.get("answer", "")
                sources = resp.get("sources", [])
                confidence = resp.get("confidence", 0.0)
                # Append to history
                st.session_state.chat_history.append({"user": prompt, "bot": answer, "ts": None})
                st.success(f"Confidence: {confidence:.2f}")
                show_sources(sources)
            except Exception as e:
                st.error("Error calling backend: " + str(e))

    # show past messages
    render_messages(st.session_state.chat_history)
