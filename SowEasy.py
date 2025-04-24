import streamlit as st
from PIL import Image
import base64
import os

# Configure the page
st.set_page_config(
    page_title="SowEasy - AI Crop Advisor",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load and apply custom CSS
def load_css():
    with open('styles/main.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

load_css()

# Custom background and header
def add_bg_from_local(image_file):
    with open(image_file, "rb") as file:
        encoded_string = base64.b64encode(file.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(data:image/jpg;base64,{encoded_string});
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Add background image
add_bg_from_local('cc.jpg')

# Custom header with gradient
st.markdown("""
    <div class="custom-header">
        <h1>🌾 SowEasy - AI Crop Recommender</h1>
        <p style='font-size: 1.2em;'>Your Smart Farming Assistant</p>
    </div>
""", unsafe_allow_html=True)

# Main content in a container with custom styling
with st.container():
    st.markdown('<div class="custom-container fade-in">', unsafe_allow_html=True)
    
    # Two-column layout for features
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="custom-card">
            <h2>🎯 Key Features</h2>
            <ul>
                <li>AI-Powered Crop Recommendations</li>
                <li>Disease Detection & Analysis</li>
                <li>Yield & ROI Calculator</li>
                <li>Smart Irrigation Planning</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("""
        <div class="custom-card">
            <h2>🌟 Benefits</h2>
            <ul>
                <li>Increase Agricultural Production</li>
                <li>Optimize Resource Usage</li>
                <li>Make Data-Driven Decisions</li>
                <li>Connect with Farming Community</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    # Getting Started Section
    st.markdown("""
    <div class="custom-card">
        <h2>🚀 Getting Started</h2>
        <p>Navigate through the sidebar to access different features:</p>
        <div class="metric-container">
            <p><strong>🌱 Predict Crop:</strong> Get recommendations based on soil and climate conditions.</p>
            <p><strong>🔍 Disease Detection:</strong> Upload plant images for disease analysis.</p>
            <p><strong>💰 ROI Calculator:</strong> Calculate potential returns on your farming investment.</p>
            <p><strong>💧 Smart Irrigation:</strong> Plan efficient water usage for your crops.</p>
            <p><strong>👥 Community:</strong> Connect with other farmers and share experiences.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

# Sidebar enhancement
with st.sidebar:
    st.markdown("""
    <div style='text-align: center; padding: 1rem;'>
        <h2>🌾 Navigation</h2>
    </div>
    """, unsafe_allow_html=True)
    
# Footer
st.markdown("""
<div style='text-align: center; padding: 2rem; opacity: 0.7;'>
    <p>Made with ❤️ for Farmers</p>
</div>
""", unsafe_allow_html=True) 