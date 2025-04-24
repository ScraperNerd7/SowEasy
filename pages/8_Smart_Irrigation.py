import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import plotly.graph_objects as go
import plotly.express as px

st.set_page_config(page_title="Smart Irrigation", page_icon="💧")
st.title("💧 Smart Irrigation Planning")

# Load crop dataset
df = pd.read_csv('Crop_recommendation.csv')
unique_crops = sorted(df['label'].unique())

# Crop water requirements (mm/day) - example data
crop_water_req = {
    "rice": {"initial": 4.5, "development": 6.5, "mid": 7.5, "late": 4.0},
    "wheat": {"initial": 3.0, "development": 4.5, "mid": 6.0, "late": 3.5},
    "maize": {"initial": 3.5, "development": 5.0, "mid": 6.5, "late": 4.0}
}

# Add default values for other crops
for crop in unique_crops:
    if crop.lower() not in crop_water_req:
        crop_water_req[crop.lower()] = {
            "initial": 3.5,
            "development": 5.0,
            "mid": 6.0,
            "late": 3.5
        }

st.markdown("""
Plan your irrigation schedule efficiently with our smart irrigation calculator.
Get recommendations for:
- Daily water requirements
- Irrigation scheduling
- Water conservation tips
- Cost optimization
""")

# Input Section
col1, col2 = st.columns(2)

with col1:
    st.subheader("Crop Details")
    selected_crop = st.selectbox("Select Crop", unique_crops)
    area = st.number_input("Field Area (hectares)", min_value=0.1, value=1.0, step=0.1)
    soil_type = st.selectbox("Soil Type", ["Sandy", "Loamy", "Clay", "Silt"])
    
    # Soil water holding capacity (mm/m)
    soil_water_capacity = {
        "Sandy": 100,
        "Loamy": 170,
        "Clay": 200,
        "Silt": 150
    }

with col2:
    st.subheader("Environmental Factors")
    rainfall_prob = st.slider("Expected Rainfall Probability (%)", 0, 100, 30)
    temperature = st.slider("Average Temperature (°C)", 0, 45, 25)
    humidity = st.slider("Relative Humidity (%)", 0, 100, 50)
    wind_speed = st.slider("Wind Speed (km/h)", 0, 50, 10)

# Irrigation System
st.subheader("Irrigation System")
irrigation_system = st.selectbox("Select Irrigation System", [
    "Drip Irrigation",
    "Sprinkler System",
    "Surface Irrigation",
    "Center Pivot"
])

irrigation_efficiency = {
    "Drip Irrigation": 0.90,
    "Sprinkler System": 0.75,
    "Surface Irrigation": 0.60,
    "Center Pivot": 0.80
}

if st.button("Calculate Irrigation Schedule"):
    # Calculate daily water requirements
    crop_req = crop_water_req[selected_crop.lower()]
    
    # Generate 30-day schedule
    days = 30
    dates = [datetime.now() + timedelta(days=x) for x in range(days)]
    
    # Calculate water requirements considering all factors
    daily_req = []
    cumulative_req = 0
    
    for i in range(days):
        # Base requirement
        if i < days * 0.2:  # Initial stage
            base_req = crop_req["initial"]
        elif i < days * 0.4:  # Development stage
            base_req = crop_req["development"]
        elif i < days * 0.7:  # Mid stage
            base_req = crop_req["mid"]
        else:  # Late stage
            base_req = crop_req["late"]
        
        # Adjust for environmental factors
        temp_factor = 1 + (temperature - 25) * 0.05
        humidity_factor = 1 - (humidity - 50) * 0.005
        wind_factor = 1 + (wind_speed - 10) * 0.02
        
        # Calculate adjusted requirement
        adj_req = base_req * temp_factor * humidity_factor * wind_factor
        
        # Account for rainfall probability
        rainfall_adj = 1 - (rainfall_prob * 0.01 * 0.5)
        
        # Final daily requirement in cubic meters
        final_req = (adj_req * area * 10 * rainfall_adj) / irrigation_efficiency[irrigation_system]
        daily_req.append(final_req)
        cumulative_req += final_req
    
    # Create visualization
    fig = go.Figure()
    
    # Daily requirements
    fig.add_trace(go.Scatter(
        x=dates,
        y=daily_req,
        name='Daily Requirement',
        line=dict(color='blue')
    ))
    
    # Cumulative requirement
    cumulative = np.cumsum(daily_req)
    fig.add_trace(go.Scatter(
        x=dates,
        y=cumulative,
        name='Cumulative Requirement',
        line=dict(color='red', dash='dash')
    ))
    
    fig.update_layout(
        title='Water Requirements Over Time',
        xaxis_title='Date',
        yaxis_title='Water Requirement (cubic meters)',
        hovermode='x unified'
    )
    
    st.plotly_chart(fig)
    
    # Summary statistics
    st.subheader("Irrigation Summary")
    col3, col4, col5 = st.columns(3)
    
    with col3:
        st.metric("Average Daily Requirement", f"{np.mean(daily_req):.1f} m³")
    with col4:
        st.metric("Total Monthly Requirement", f"{cumulative_req:.1f} m³")
    with col5:
        st.metric("System Efficiency", f"{irrigation_efficiency[irrigation_system]*100:.0f}%")
    
    # Irrigation schedule
    st.subheader("Recommended Irrigation Schedule")
    
    # Calculate irrigation intervals based on soil type and system
    soil_factor = soil_water_capacity[soil_type] / 150  # Normalize to medium soil
    if irrigation_system == "Drip Irrigation":
        interval = 1
    else:
        interval = max(1, int(soil_factor * 3))  # Base interval on soil type
    
    schedule_data = []
    for i in range(0, days, interval):
        water_amount = sum(daily_req[i:i+interval])
        schedule_data.append({
            "Date": dates[i].strftime('%Y-%m-%d'),
            "Water Amount (m³)": f"{water_amount:.1f}",
            "Duration (hours)": f"{water_amount/5:.1f}"  # Assuming 5 m³/hour flow rate
        })
    
    schedule_df = pd.DataFrame(schedule_data)
    st.table(schedule_df)
    
    # Water conservation tips
    st.subheader("Water Conservation Recommendations")
    st.markdown(f"""
    Based on your setup, here are some recommendations:
    
    1. **Timing**: Water early in the morning or late in the evening to reduce evaporation
    2. **Mulching**: Apply organic mulch to reduce water evaporation
    3. **Maintenance**: Regularly check for leaks in the {irrigation_system.lower()}
    4. **Monitoring**: Install soil moisture sensors to optimize irrigation timing
    5. **Weather**: Skip irrigation if rainfall is expected (current probability: {rainfall_prob}%)
    """)
    
    # Cost estimation
    st.subheader("Cost Estimation")
    water_cost_per_m3 = 0.5  # Example cost per cubic meter
    electricity_cost_per_hour = 1.0  # Example electricity cost per hour
    
    total_water_cost = cumulative_req * water_cost_per_m3
    total_electricity_cost = (cumulative_req/5) * electricity_cost_per_hour  # Assuming 5 m³/hour
    
    cost_data = {
        "Category": ["Water Cost", "Electricity Cost", "Total Cost"],
        "Amount (₹)": [
            f"₹{total_water_cost:.2f}",
            f"₹{total_electricity_cost:.2f}",
            f"₹{total_water_cost + total_electricity_cost:.2f}"
        ]
    }
    cost_df = pd.DataFrame(cost_data)
    st.table(cost_df) 