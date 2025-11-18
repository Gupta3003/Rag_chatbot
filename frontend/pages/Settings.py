# src/pages/settings.py
import streamlit as st
import os

def page_settings():
    st.title("Settings")
    st.write("Set backend URL and other local options.")
    backend_url = st.text_input("Backend URL", value=os.environ.get("RAG_BACKEND_URL", "http://localhost:8000"))
    if st.button("Save (session only)"):
        st.session_state.backend_url = backend_url
        st.success("Saved to session.")
    st.write("Session backend URL:", st.session_state.get("backend_url", backend_url))
    st.markdown("Note: To set permanently, set environment variable `RAG_BACKEND_URL`.")
