# src/pages/image_analysis.py
import streamlit as st
from utils.api_client import image_analysis
from PIL import Image
import io

def page_image_analysis():
    st.title("Image Analysis")
    st.write("Upload an image to analyze (OCR / captioning / classification depending on your model).")
    uploaded = st.file_uploader("Choose an image", type=["png", "jpg", "jpeg"])
    if uploaded:
        img = Image.open(uploaded)
        st.image(img, caption="Uploaded", use_column_width=True)
        if st.button("Analyze"):
            with st.spinner("Analyzing..."):
                try:
                    content = uploaded.getvalue()
                    resp = image_analysis(content, filename=uploaded.name)
                    text = resp.get("text") or str(resp.get("raw", resp))
                    st.subheader("Analysis Result")
                    st.write(text)
                except Exception as e:
                    st.error("Image analysis error: " + str(e))
