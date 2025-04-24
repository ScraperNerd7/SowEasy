import streamlit as st
import os
from PIL import Image
import io
import base64
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Crop Disease Detection", page_icon="🔍")
st.title("🔍 Crop Disease Detection")

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

st.markdown("""
Upload an image of your plant/crop leaf to detect diseases and get treatment recommendations.
Our AI will analyze the image and provide:
- Disease identification
- Severity assessment
- Treatment recommendations
- Preventive measures
""")

uploaded_file = st.file_uploader("Choose an image of the plant/leaf...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)
    
    if st.button('Analyze Image'):
        with st.spinner('Analyzing image...'):
            # Convert the image to base64
            buffered = io.BytesIO()
            image.save(buffered, format=image.format if image.format else 'JPEG')
            img_str = base64.b64encode(buffered.getvalue()).decode()
            
            try:
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",  # Using GPT-3.5-turbo for wider availability
                    messages=[
                        {
                            "role": "system",
                            "content": """You are an expert in agricultural plant pathology. When presented with a plant/leaf image, analyze it for:
                            1. Visual symptoms and potential diseases
                            2. Severity level of any issues found
                            3. Specific treatment recommendations
                            4. Preventive measures for future protection
                            
                            Format your response in clear sections with markdown headings."""
                        },
                        {
                            "role": "user",
                            "content": f"""I have a plant/leaf image showing potential disease symptoms. The image is encoded in base64: {img_str}

Please provide a detailed analysis with the following sections:

### Disease Identification
[Identify any visible diseases or issues based on the image]

### Severity Assessment
[Assess the severity level of the identified issues]

### Treatment Recommendations
[Provide specific treatment recommendations]

### Preventive Measures
[Suggest preventive measures to avoid future occurrences]"""
                        }
                    ],
                    max_tokens=1000
                )
                
                st.markdown("### Analysis Results")
                st.markdown(response.choices[0].message.content)
                
            except Exception as e:
                st.error(f"Error analyzing image: {str(e)}")
                st.info("""Please ensure:
                1. Your OpenAI API key is set correctly in the .env file
                2. The image is in a supported format (JPG, JPEG, PNG)
                3. The image file size is not too large""")
                
                # Additional error handling suggestions
                if "invalid_api_key" in str(e):
                    st.warning("Invalid API key. Please check your OpenAI API key in the .env file.")
                elif "insufficient_quota" in str(e):
                    st.warning("Your OpenAI API quota has been exceeded. Please check your usage limits.") 