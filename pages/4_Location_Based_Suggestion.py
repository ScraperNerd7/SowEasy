import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage
import requests
import geocoder
import os
from dotenv import load_dotenv

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI LLM
llm = ChatOpenAI(model_name="gpt-4", openai_api_key=openai_api_key)

st.title("📍 Location-Based Crop Recommendation")

# Option to get location automatically
st.subheader("🌎 Enter Your Location")
auto_location = st.checkbox("Use my current location")

if auto_location:
    # Get location using geocoder
    g = geocoder.ip("me")
    if g.city and g.country:
        location = f"{g.city}, {g.country}"
    else:
        location = None
else:
    location = st.text_input("Enter City & Country (e.g., New Delhi, India)")

if st.button("Get Crop Suggestions"):
    if location:
        st.success(f"📍 Location Detected: {location}")

        # Generate crop recommendations using LangChain LLM
        crop_prompt = f"""
        Based on the following conditions:
        - Location: {location}
        
        Suggest the **best crops** that can be cultivated in this region. 
        Provide detailed insights, including:
        - Ideal soil type
        - Best season for cultivation
        - Required nutrients
        - Farming techniques
        - Common pests & control methods
        """
        
        ai_response = llm([SystemMessage(content="You are an expert agronomist."), HumanMessage(content=crop_prompt)])
        
        st.subheader("🌾 Recommended Crops")
        st.write(ai_response.content)
    
    else:
        st.warning("Please enter a valid location.")
