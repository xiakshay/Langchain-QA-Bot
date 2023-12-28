## Q/A chatbot

from langchain.llms import OpenAI
from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os

## functio to load openai model and get responses
def get_openai_response(question):
    llm = OpenAI(openai_api_key = os.getenv("OPEN_API_KEY"), model_name="text-davinci-003", temperature=0.5)
    response = llm(question)
    return response

## initialize streamlit app

st.set_page_config(page_title="Q&A Demo")
st.header("Langchain Application")
input=st.text_input("Input: ", key="input")
response = get_openai_response(input)
submit = st.button("Generate")


## if ask button clicked
if submit:
    st.subheader("The response is ")
    st.write(response)