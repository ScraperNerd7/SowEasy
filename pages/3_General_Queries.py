import streamlit as st
from streamlit_chat import message
from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage
import os
from dotenv import load_dotenv

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
llm = ChatOpenAI(model_name="gpt-4", openai_api_key=openai_api_key)

st.title("💬 Ask an AI Agricultural Expert")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display Chat History
for message_data in st.session_state.messages:
    message(message_data["content"], is_user=message_data["is_user"])

# User Input for Chatbot
user_input = st.text_input("Ask any farming-related question!")

if st.button("Send"):
    if user_input:
        # Add User Message
        st.session_state.messages.append({"content": user_input, "is_user": True})
        
        # Get AI Response
        response = llm([SystemMessage(content="You are an AI expert in agriculture."), HumanMessage(content=user_input)])
        bot_response = response.content
        
        # Store and Display Messages
        st.session_state.messages.append({"content": bot_response, "is_user": False})
        message(user_input, is_user=True)
        message(bot_response, is_user=False)
