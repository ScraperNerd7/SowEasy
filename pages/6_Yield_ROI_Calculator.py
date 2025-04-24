import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

st.set_page_config(page_title="Yield & ROI Calculator", page_icon="💰")
st.title("💰 Yield Prediction & ROI Calculator")

# Load the crop dataset
df = pd.read_csv('Crop_recommendation.csv')
unique_crops = sorted(df['label'].unique())

st.markdown("""
Calculate expected yield and return on investment for your crop based on various factors.
""")

# Input sections
col1, col2 = st.columns(2)

with col1:
    st.subheader("Crop Details")
    selected_crop = st.selectbox("Select Crop", unique_crops)
    area = st.number_input("Land Area (acres)", min_value=0.1, value=1.0, step=0.1)
    
    st.subheader("Cost Inputs")
    seed_cost = st.number_input("Seed Cost (per acre)", min_value=0, value=100)
    fertilizer_cost = st.number_input("Fertilizer Cost (per acre)", min_value=0, value=150)
    labor_cost = st.number_input("Labor Cost (per acre)", min_value=0, value=200)
    irrigation_cost = st.number_input("Irrigation Cost (per acre)", min_value=0, value=100)
    other_costs = st.number_input("Other Costs (per acre)", min_value=0, value=50)

with col2:
    st.subheader("Market Information")
    market_price = st.number_input("Current Market Price (per kg)", min_value=0.0, value=20.0)
    
    st.subheader("Environmental Factors")
    rainfall = st.slider("Average Rainfall (mm)", 0, 300, 100)
    temperature = st.slider("Average Temperature (°C)", 0, 45, 25)
    humidity = st.slider("Humidity (%)", 0, 100, 50)

if st.button("Calculate Yield and ROI"):
    # Simple yield prediction based on environmental factors
    # This is a simplified model - you can replace it with your trained ML model
    base_yield = np.random.normal(2000, 200)  # Base yield in kg per acre
    rainfall_factor = 1 + (rainfall - 100) / 200
    temp_factor = 1 - abs(temperature - 25) / 25
    humidity_factor = 1 + (humidity - 50) / 100
    
    predicted_yield = base_yield * rainfall_factor * temp_factor * humidity_factor
    predicted_yield = max(predicted_yield, 1000)  # Set minimum yield
    
    # Calculate costs
    total_cost_per_acre = seed_cost + fertilizer_cost + labor_cost + irrigation_cost + other_costs
    total_cost = total_cost_per_acre * area
    
    # Calculate revenue and profit
    total_yield = predicted_yield * area
    total_revenue = total_yield * market_price
    total_profit = total_revenue - total_cost
    roi = (total_profit / total_cost) * 100

    # Display results
    st.subheader("Results")
    col3, col4, col5 = st.columns(3)
    
    with col3:
        st.metric("Predicted Yield", f"{total_yield:.0f} kg")
    with col4:
        st.metric("Total Revenue", f"₹{total_revenue:.2f}")
    with col5:
        st.metric("ROI", f"{roi:.1f}%")

    # Detailed breakdown
    st.subheader("Detailed Breakdown")
    st.markdown(f"""
    **Costs Breakdown (Total: ₹{total_cost:.2f})**
    - Seeds: ₹{seed_cost * area:.2f}
    - Fertilizer: ₹{fertilizer_cost * area:.2f}
    - Labor: ₹{labor_cost * area:.2f}
    - Irrigation: ₹{irrigation_cost * area:.2f}
    - Other: ₹{other_costs * area:.2f}

    **Profit Analysis**
    - Total Cost: ₹{total_cost:.2f}
    - Total Revenue: ₹{total_revenue:.2f}
    - Net Profit: ₹{total_profit:.2f}
    - Return on Investment: {roi:.1f}%
    """)

    # Recommendations
    st.subheader("Recommendations")
    if roi > 50:
        st.success("This appears to be a highly profitable crop choice! Consider increasing your cultivation area.")
    elif roi > 20:
        st.info("This crop shows good profit potential. Focus on optimizing costs to increase ROI.")
    else:
        st.warning("Consider ways to reduce costs or explore alternative crops for better returns.") 