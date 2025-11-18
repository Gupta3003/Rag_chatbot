# src/components/sidebar.py
import streamlit as st
from PIL import Image
import os

def render_sidebar():
    st.sidebar.image(Image.open(os.path.join("assets", "logo.png")) if os.path.exists("src/assets/logo.png") else None, width=120)
    st.sidebar.markdown("## RAG Chatbot")
    pages = [
        "Chatbot (RAG)",
        "Text Generation",
        "Image Analysis",
        "Documentation",
        "Settings"
    ]
    choice = st.sidebar.radio("Go to", pages, index=0, key="selected_page")
    # footer
    st.sidebar.markdown("---")
    st.sidebar.markdown("Built for AI Intern Assignment")
