import streamlit as st
from main import agentgen


st.title("Chatbot with AI Agents")
query=st.text_input('Type your query here')


if query :
    response=agentgen(query)
    st.write(response['output'])

