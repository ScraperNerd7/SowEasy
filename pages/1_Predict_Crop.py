import streamlit as st
import pickle
from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage
import os
from dotenv import load_dotenv

# Load ML Models
LogReg_model = pickle.load(open('LogReg_model.pkl', 'rb'))
DecisionTree_model = pickle.load(open('DecisionTree_model.pkl', 'rb'))
NaiveBayes_model = pickle.load(open('NaiveBayes_model.pkl', 'rb'))
RF_model = pickle.load(open('RF_model.pkl', 'rb'))
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
llm = ChatOpenAI(model_name="gpt-4", openai_api_key=openai_api_key)

st.title("🌱 Predict the Best Crop")

# Sidebar Model Selection
activities = ['Naive Bayes (The Best Model)', 'Logistic Regression', 'Decision Tree', 'Random Forest']
option = st.sidebar.selectbox("Select Model for Prediction:", activities)

# User Input Sliders
sn = st.slider('NITROGEN (N)', 0.0, 150.0)
sp = st.slider('PHOSPHOROUS (P)', 0.0, 150.0)
pk = st.slider('POTASSIUM (K)', 0.0, 210.0)
pt = st.slider('TEMPERATURE (°C)', 0.0, 50.0)
phu = st.slider('HUMIDITY (%)', 0.0, 100.0)
pPh = st.slider('Soil pH', 0.0, 14.0)
pr = st.slider('RAINFALL (mm)', 0.0, 300.0)

inputs = [[sn, sp, pk, pt, phu, pPh, pr]]

if st.button('Classify'):
    models = {
        'Logistic Regression': LogReg_model,
        'Decision Tree': DecisionTree_model,
        'Naive Bayes (The Best Model)': NaiveBayes_model,
        'Random Forest': RF_model
    }
    model = models[option]
    prediction = model.predict(inputs)[0]

    explanation_prompt = f"""
    The recommended crop is {prediction}. Given the soil nitrogen ({sn}), phosphorus ({sp}), potassium ({pk}), temperature ({pt}°C), humidity ({phu}%), pH ({pPh}), and rainfall ({pr} mm), 
    explain why {prediction} is suitable and how it thrives in these conditions.
    """
    
    response = llm([SystemMessage(content="You are an expert agronomist."), HumanMessage(content=explanation_prompt)])
    
    st.success(f"✅ **{prediction}** is the best crop for cultivation here.")
    st.info(f"💡 **Why {prediction}?**\n{response.content}")
