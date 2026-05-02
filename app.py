import streamlit as st
import requests

# --------------------------------------
# App Config
# --------------------------------------
st.set_page_config(
    page_title="CropWise AI",
    page_icon="🌾",
    layout="centered"
)

st.title("🌱 CropWise AI - Crop Recommendation System")

st.markdown("""
Enter your soil parameters below to get the best crop recommendation using AI.
""")

# --------------------------------------
# Input Fields
# --------------------------------------
st.subheader("🌾 Enter Soil Details")

N = st.number_input("Nitrogen (N)", min_value=0.0, value=90.0)
P = st.number_input("Phosphorus (P)", min_value=0.0, value=42.0)
K = st.number_input("Potassium (K)", min_value=0.0, value=43.0)
temperature = st.number_input("Temperature (°C)", value=20.8)
humidity = st.number_input("Humidity (%)", value=82.0)
ph = st.number_input("pH", min_value=0.0, max_value=14.0, value=6.5)
rainfall = st.number_input("Rainfall (mm)", value=202.0)

# --------------------------------------
# Prediction Button
# --------------------------------------
if st.button("🌿 Predict Best Crop"):

    api_url = "https://cropwiseai-api.onrender.com/predict"

    api_data = {
        "N": N,
        "P": P,
        "K": K,
        "temperature": temperature,
        "humidity": humidity,
        "ph": ph,
        "rainfall": rainfall
    }

    try:
        with st.spinner("🔄 Getting recommendation..."):
            response = requests.post(api_url, json=api_data)

        if response.status_code == 200:
            result = response.json()
            crop = result["recommended_crop"]

            st.success(f"🌾 Recommended Crop: **{crop.upper()}**")

        else:
            st.error("❌ API Error: Failed to get response")

    except Exception as e:
        st.error(f"❌ Connection Error: {e}")
