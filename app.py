import streamlit as st
from text_summarizer.functions import summarize
import os
import openai


try:
    openai.api_key = os.getenv('OPENAI_KEY')

    if "summary" not in st.session_state:
        st.session_state["summary"] = ""

    st.title("Text Summarizer")

    input_text = st.text_area(label='Enter full text:', value="", height=250)
    st.button(
            "submit",
            on_click=summarize,
            kwargs={"prompt": input_text},
            )
    # configure text area to populate with current state of summary
    output_text = st.text_area(label='Summarized text:', value=st.session_state["summary"], height=250)
except:
    st.write('There was an error = (')

