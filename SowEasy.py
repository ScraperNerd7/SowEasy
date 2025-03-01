import streamlit as st
from PIL import Image
st.set_page_config(
    page_title="SowEasy - AI Crop Advisor",
    page_icon="🌾",
    layout="centered"
)

st.title("🌾 SowEasy - AI Crop Recommender")
image = Image.open('cc.jpg')
st.image(image, use_column_width=True)
st.write("Welcome to SowEasy! Navigate through the sidebar to:")
st.markdown("""
- **🌱 Predict Crop:** Get recommendations based on soil and climate conditions.
- **📜 Crop Information:** Learn about ideal soil, seasons, and farming methods for any crop.
- **💬 General Queries:** Ask anything related to agriculture and farming.
- **📍 Location-Based Crop Suggestions:** Get crop recommendations based on your region’s climate and soil conditions.
""")

st.sidebar.success("Select a page above 👆")
