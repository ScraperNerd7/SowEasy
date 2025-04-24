# 🌾 SowEasy - AI Crop Recommender

## 🚀 About the Project
SowEasy is an AI-powered crop recommendation system designed to assist farmers in making data-driven decisions about what to plant. By analyzing key environmental factors such as **soil composition, pH level, rainfall, humidity, and temperature**, the system predicts the most suitable crop to cultivate, enhancing productivity and sustainability in agriculture.

## 🎯 Objectives
SowEasy aims to:
- 🌱 **Increase Agricultural Production** – By recommending the most suitable crops for specific conditions, farmers can maximize yield.
- 🛑 **Reduce Chemical Usage** – Precision farming helps minimize the need for excessive fertilizers and pesticides.
- 💧 **Optimize Water Resources** – Ensures efficient use of water based on the crop's requirements.
- 🌍 **Prevent Soil Degradation** – Encourages sustainable farming practices by selecting crops that suit the soil type.

## 🛠 Features
✅ **AI-Powered Crop Prediction** – Recommends the best crop based on soil and climatic conditions.  
✅ **Conversational AI** – Uses NLP (ChatGPT) to provide insights and answer farming-related queries.  
✅ **Automated Crop Insights** – Explains why a crop is recommended based on input data.  
✅ **Multi-Page Navigation** –  
  - **🌱 Predict Crop:** Get crop recommendations based on input parameters.  
  - **📜 Crop Information:** Enter a crop name and get details about soil, season, farming methods, and pest control.  
  - **💬 General Queries:** Ask any agriculture-related questions.  
  - **📍 Location-Based Suggestions:** Predict the best crops based on your region's climate and soil conditions.  
  - **🔍 Disease Detection:** Upload plant/leaf images for AI-powered disease diagnosis and treatment recommendations.
  - **💰 Yield & ROI Calculator:** Calculate expected yields, costs, and return on investment for your crops.
  - **👥 Community Forum:** Connect with other farmers, share experiences, and get expert advice.
  - **💧 Smart Irrigation:** Plan efficient irrigation schedules and optimize water usage.

## 🌟 Key Features in Detail

### 🔍 Disease Detection
- Upload images of plant leaves or crops
- AI-powered disease identification
- Severity assessment
- Treatment recommendations
- Preventive measures
- Supports multiple image formats (JPG, JPEG, PNG)

### 💰 Yield & ROI Calculator
- Predict crop yields based on environmental factors
- Detailed cost breakdown analysis
- Calculate return on investment
- Input customization for:
  - Land area
  - Seed costs
  - Fertilizer costs
  - Labor costs
  - Irrigation costs
  - Market prices

### 👥 Community Forum
- Interactive discussion forum for farmers
- Create and respond to posts by category
- Expert consultation using AI
- Share success stories and experiences
- Categories include:
  - General Discussion
  - Crop Issues
  - Market Prices
  - Equipment
  - Weather
  - Best Practices

### 💧 Smart Irrigation Planning
- Calculate daily water requirements
- Generate custom irrigation schedules
- Factors considered:
  - Crop type and growth stage
  - Soil type and water capacity
  - Environmental conditions
  - Irrigation system efficiency
- Features include:
  - Water requirement visualization
  - Cost estimation
  - Conservation recommendations
  - System efficiency analysis
- Support for multiple irrigation systems:
  - Drip Irrigation
  - Sprinkler System
  - Surface Irrigation
  - Center Pivot

## 📊 Dataset
This application is trained using a dataset from **Kaggle**, which contains details about various crops and their ideal growing conditions.
- 📂 **Dataset Link:** [Crop Recommendation Dataset](https://www.kaggle.com/datasets/atharvaingle/crop-recommendation-dataset)

## 🏗 Tech Stack
- **Python** – Core programming language  
- **Streamlit** – Interactive UI for the web app  
- **OpenAI GPT-3.5** – AI-powered disease detection and insights  
- **Machine Learning Models** – Logistic Regression, Decision Tree, Naïve Bayes, Random Forest  
- **Pandas & NumPy** – Data processing  
- **Scikit-learn** – Model training and evaluation  
- **Plotly** – Interactive data visualization
- **PIL (Python Imaging Library)** – Image processing

## ⚙️ Installation & Setup
To run the project locally, follow these steps:
```bash
# Clone the repository
git clone https://github.com/yourusername/soweasy.git
cd soweasy

# Install dependencies
pip install -r requirements.txt

# Create a .env file and add your OpenAI API key
echo "OPENAI_API_KEY=your_api_key_here" > .env

# Run the application
streamlit run SowEasy.py
```

## 🔑 API Key Setup
The application requires an OpenAI API key for disease detection and expert consultation features:
1. Get your API key from [OpenAI Platform](https://platform.openai.com)
2. Create a `.env` file in the project root
3. Add your API key: `OPENAI_API_KEY=your_api_key_here`

## 📝 Usage Notes
- For disease detection, ensure images are clear and well-lit
- Supported image formats: JPG, JPEG, PNG
- Keep image sizes reasonable for optimal processing
- API usage is subject to OpenAI's pricing and rate limits
- Community forum data is session-based (resets on app restart)
- Irrigation calculations are estimates and should be validated with local conditions

### 📧 Contact

This README follows best practices and provides **clear** and **useful** information about your project. 🚀 Let me know if you want any modifications!

