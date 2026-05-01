from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np

app = FastAPI()

# Loading models
model = pickle.load(open("models/soil_model.pkl", "rb"))
scaler = pickle.load(open("models/scaler.pkl", "rb"))
label_encoder = pickle.load(open("models/label_encoder.pkl", "rb"))

# Define input schema
class SoilInput(BaseModel):
    N: float
    P: float
    K: float
    temperature: float
    humidity: float
    ph: float
    rainfall: float

@app.get("/")
def home():
    return {"message": "API is working"}

@app.post("/predict")
def predict(data: SoilInput):
    input_list = [
        data.N,
        data.P,
        data.K,
        data.temperature,
        data.humidity,
        data.ph,
        data.rainfall
    ]

    input_array = np.array(input_list).reshape(1, -1)
    input_scaled = scaler.transform(input_array)
    prediction = model.predict(input_scaled)[0]
    crop = label_encoder.inverse_transform([prediction])[0]

    return {"recommended_crop": crop}
