# src/components/chat_ui.py
import streamlit as st
from datetime import datetime

def render_messages(history):
    """
    history: list of dicts {"user": "...", "bot": "...", "ts": float}
    """
    for turn in history:
        user = turn.get("user")
        bot = turn.get("bot")
        ts = turn.get("ts")
        if ts:
            ts_str = datetime.fromtimestamp(ts).strftime("%Y-%m-%d %H:%M:%S")
        else:
            ts_str = ""
        st.markdown(f"**You** • _{ts_str}_")
        st.info(user)
        st.markdown("**Bot**")
        st.success(bot)

def chat_input_area(default_prompt=""):
    st.subheader("Ask something")
    with st.form("chat_form", clear_on_submit=False):
        prompt = st.text_area("You:", value=default_prompt, height=120, key="chat_prompt")
        submitted = st.form_submit_button("Send")
    return submitted, prompt
