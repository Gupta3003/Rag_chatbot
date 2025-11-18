# src/components/visual_components.py
import streamlit as st

def show_sources(sources):
    if not sources:
        st.write("No sources returned.")
        return
    st.write("Sources:")
    for i, s in enumerate(sources, start=1):
        st.write(f"{i}. {s}")
