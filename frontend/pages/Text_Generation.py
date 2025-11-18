# src/pages/text_generation.py
import streamlit as st
from utils.api_client import text_generation

def page_text_generation():
    st.title("Text Generation (Hugging Face)")
    st.write("Use a text-generation model (Hugging Face) via backend. Model selection is optional here; leave blank to use backend default.")
    if "text_out" not in st.session_state:
        st.session_state.text_out = ""

    with st.form("tg_form"):
        model = st.text_input("Model (optional)", value="")
        prompt = st.text_area("Prompt", value="Write a short summary of earthing in electrical systems.", height=200)
        col1, col2 = st.columns(2)
        with col1:
            max_new_tokens = st.number_input("Max new tokens", value=150, min_value=1)
            temperature = st.slider("Temperature", 0.0, 1.5, 0.7)
        with col2:
            top_k = st.number_input("Top K", value=50, min_value=0)
            top_p = st.slider("Top P", 0.0, 1.0, 0.95)
        submitted = st.form_submit_button("Generate")

    if submitted:
        with st.spinner("Generating text..."):
            try:
                resp = text_generation(
                    prompt=prompt,
                    model=model or None,
                    max_new_tokens=int(max_new_tokens),
                    temperature=float(temperature),
                    top_k=int(top_k),
                    top_p=float(top_p),
                )
                out = resp.get("generated_text") or str(resp.get("raw", resp))
                st.session_state.text_out = out
            except Exception as e:
                st.error("Generation error: " + str(e))

    if st.session_state.text_out:
        st.subheader("Output")
        st.write(st.session_state.text_out)
        st.download_button("Download output", st.session_state.text_out, file_name="generated_text.txt")
