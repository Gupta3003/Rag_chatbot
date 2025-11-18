# src/pages/documentation.py
import streamlit as st
import os

def page_documentation():
    st.title("Project Documentation")
    st.write("This page contains notes, architecture, and links.")
    st.markdown("### Assignment Text")
    if os.path.exists("../docs/Assignment_Full_Text.pdf"):
        st.markdown("Assignment PDF present in `docs/` folder.")
        with open("../docs/Assignment_Full_Text.pdf","rb") as f:
            st.download_button("Download Assignment PDF", f, "Assignment_Full_Text.pdf")
    else:
        st.write("Assignment PDF not found in `docs/` (place `Assignment_Full_Text.pdf` in project root `docs/`).")

    st.markdown("### How to use")
    st.markdown("- Start backend (`uvicorn backend.main:app --reload`) on port 8000")
    st.markdown("- Start this Streamlit app: `streamlit run src/app.py`")
