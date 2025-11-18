# src/app.py
import streamlit as st
from components.sidebar import render_sidebar
from pages.chatbot_interface import page_chatbot
from pages.text_generation import page_text_generation
from pages.image_analysis import page_image_analysis
from pages.documentation import page_documentation
from pages.settings import page_settings

PAGES = {
    "Chatbot (RAG)": page_chatbot,
    "Text Generation": page_text_generation,
    "Image Analysis": page_image_analysis,
    "Documentation": page_documentation,
    "Settings": page_settings,
}

def main():
    st.set_page_config(page_title="RAG Chatbot", layout="wide", page_icon="🤖")
    render_sidebar()
    selection = st.session_state.get("selected_page", "Chatbot (RAG)")
    page = PAGES.get(selection)
    if page:
        page()
    else:
        st.error("Page not found.")

if __name__ == "__main__":
    main()
