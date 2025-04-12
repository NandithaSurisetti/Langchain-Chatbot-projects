import streamlit as st
from main import agentgen


st.title("Chatbot with AI Agents")
query=st.text_input('Type your query here')


if 'chat_history' not in st.session_state:
    st.session_state['chat_history']=[]


if query :
    response=agentgen(query)
    st.subheader("Response")
    bot_answer=response['output']
    st.write(bot_answer)
    st.session_state['chat_history'].append(("You", query))
    st.session_state['chat_history'].append(("Bot", bot_answer))
    
    
st.subheader("Chat history")
for role,texts in st.session_state['chat_history']:
    st.write(f"{role}: {texts}")




    

    