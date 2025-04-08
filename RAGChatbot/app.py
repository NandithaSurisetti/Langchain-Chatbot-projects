import streamlit as st
from main import generator


st.title("RAG powered Chatbot")
query=st.text_input('Type your query here')


if query :
    response=generator(query)
    st.write(response['answer'])