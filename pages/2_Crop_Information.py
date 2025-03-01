import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

import os
from dotenv import load_dotenv
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(model_name="gpt-4", openai_api_key=openai_api_key)

st.title("📜 Crop Information")

crop_name = st.text_input("Enter the crop name (e.g., Wheat, Rice, Maize)")

if st.button("Get Information"):
    if crop_name:
        info_prompt = f"""
        Provide detailed information about {crop_name} including:
        - Ideal soil type
        - Best temperature range
        - Required nutrients
        - Ideal season for cultivation
        - Step-by-step farming methods
        - Common diseases and pest control
        - Average Cost Per Acre of Land
        """
        
        response = llm([SystemMessage(content="You are an expert agronomist."), HumanMessage(content=info_prompt)])
        
        st.subheader(f"🌱 {crop_name} - Detailed Information")
        st.write(response.content)
    else:
        st.warning("Please enter a crop name.")
