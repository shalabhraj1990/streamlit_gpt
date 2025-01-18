from langchain_openai import ChatOpenAI
import streamlit as st
from langchain.globals import set_debug

set_debug(True)

st.title("Ask Anything with OpenAI")

# OPENAI_API_KEY = "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"
with st.sidebar:
    st.title("provide youy api key")
    OPENAI_API_KEY = st.text_input("Enter your OpenAI API Key:", type="password")
if not OPENAI_API_KEY:
    st.info("Please provide your OpenAI API Key in the sidebar")
    st.stop()
llm = ChatOpenAI(model_name="gpt-4o-mini", api_key=OPENAI_API_KEY)

question = st.text_input("Enter your question: ")

if question:
    response = llm.invoke(question)
    st.write(response.content)
