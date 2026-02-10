from dotenv import load_dotenv
import streamlit as st
from langchain_groq import ChatGroq
from streamlit import user
#  streamlit run .\chatbot.py
#user query -> display user query -> save query to chat history -> send chat history to llm -> get response from llm and save to chat history -> display response od assistant->
#for next question display from beginning by running thru the chat history( you might not see as it happens fast)

#load the environmental variables
load_dotenv() #otherwise load the location if not in same folder

#streamlit page setup
st.set_page_config(
    page_title="Chatbot",
    page_icon="💬",
    layout="centered"
)
st.title("💬 Generative AI Chatbot - Pramod Reddy Lankala")

#initiate chat history
# chat_history = []

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

#show chat history
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# llm_initiate
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.0,
    )

#input box
user_prompt = st.chat_input("Ask  Chatbot ...")

if user_prompt:
    st.chat_message("user").markdown(user_prompt)
    st.session_state.chat_history.append({"role":"user","content": user_prompt})

    response = llm.invoke(
        input = [{"role":"system","content": "You are a helpful assistant"}, *st.session_state.chat_history]
                         )
    assistant_response = response.content
    st.session_state.chat_history.append({"role":"assistant","content":assistant_response})

    if assistant_response:
        st.chat_message("assistant").markdown(assistant_response)

    # print(st.session_state.chat_history)

    # with st.chat_message("assistant"):

    #     st.markdown(assistant_response)
