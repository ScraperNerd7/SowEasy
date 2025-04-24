import streamlit as st
from PIL import Image
st.set_page_config(
    page_title="BioBloom - AI Crop Advisor",
    page_icon="🌾",
    layout="centered"
)

st.title("🌾 BioBloom - AI Crop Recommender")
image = Image.open('cc.jpg')
st.image(image, use_column_width=True)
st.write("Welcome to BioBloom! Navigate through the sidebar to:")
st.markdown("""
- **🌱 Predict Crop:** Get recommendations based on soil and climate conditions.
- **📜 Crop Information:** Learn about ideal soil, seasons, and farming methods for any crop.
- **💬 General Queries:** Ask anything related to agriculture and farming.
- **📍 Location-Based Crop Suggestions:** Get crop recommendations based on your region’s climate and soil conditions.
- **🔍 Disease Detection:** Upload plant/leaf images for AI-powered disease diagnosis and treatment recommendations.
- **💰 Yield & ROI Calculator:** Calculate expected yields, costs, and return on investment for your crops.
- **👥 Community Forum:** Connect with other farmers, share experiences, and get expert advice.
- **💧 Smart Irrigation:** Plan efficient irrigation schedules and optimize water usage.
""")

st.sidebar.success("Select a page above 👆")
