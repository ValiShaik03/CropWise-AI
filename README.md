# 🌱 CropWise-AI — Intelligent Crop Recommendation System

An **AI-powered full-stack application** that recommends the most suitable crops based on soil and environmental conditions.  
Built using **Machine Learning + FastAPI + Streamlit**, and deployed as a **cloud-based system**.

---

## 🧠 Project Overview

CropWise-AI helps farmers and agricultural analysts make **data-driven decisions** by analyzing:

- Soil nutrients (N, P, K)
- pH level
- Temperature & humidity
- Rainfall conditions  

👉 The system uses a trained ML model exposed via an API to provide **real-time crop recommendations**.

---

## 🚀 Key Features

- ✅ AI-based crop prediction using **Random Forest**
- ✅ **FastAPI backend** for real-time inference
- ✅ **Streamlit frontend** for interactive UI
- ✅ Structured JSON input using **Pydantic validation**
- ✅ Fully deployed on cloud (Render + Streamlit Cloud)
- ✅ Clean **client-server architecture**
- ✅ Fast and scalable prediction system

---

## 🏗️ System Architecture
```
User (Browser)
↓
Streamlit (Frontend UI)
↓
FastAPI (Backend API)
↓
ML Model (Random Forest)
↓
Prediction (Recommended Crop)
```

---

## 🧩 Tech Stack

| Category        | Technologies                         |
|----------------|-------------------------------------|
| **Language**   | Python                              |
| **Frontend**  | Streamlit                           |
| **Backend**   | FastAPI                             |
| **ML Model**  | RandomForestClassifier              |
| **Validation**| Pydantic                            |
| **Deployment**| Render, Streamlit Cloud             |
| **Libraries** | Pandas, NumPy, Scikit-learn         |

---

## 📂 Project Structure
```
cropwise-ai/
│
├── app.py # Streamlit frontend (UI)
├── main.py # FastAPI backend (API)
│
├── models/
│ ├── soil_model.pkl
│ ├── scaler.pkl
│ └── label_encoder.pkl
│
├── data/
│ └── Crop_recommendation.csv
│
├── requirements.txt
└── README.md
```

---

## ⚙️ How It Works

1. User enters soil parameters in Streamlit UI  
2. Streamlit sends request → FastAPI API  
3. FastAPI processes data using trained ML model  
4. API returns predicted crop  
5. Result is displayed instantly on UI  

---

## 🌐 Live Demo

- 🔗 **Frontend (Streamlit):** https://cropwiseai.streamlit.app/
- 🔗 **API Docs:**  https://cropwiseai-api.onrender.com/docs

---

## 🧪 Example Input

```json
{
"N": 90,
"P": 42,
"K": 43,
"temperature": 20.8,
"humidity": 82,
"ph": 6.5,
"rainfall": 202
}
```

## 🧮 Model Performance
- Accuracy: ~90%
- Algorithm: Random Forest
- Optimized using feature scaling and encoding

## 🧑‍🌾 Future Enhancements
- 🌍 Location-based recommendations (GPS integration)
- 🌐 Multi-language support
- 📊 Confidence score & top-3 crop suggestions
- 📱 Mobile app integration
- 🗄️ Database logging for predictions

## 🤝 Contributing
- Fork the repository
- Create a new branch
- Make your changes
- Submit a pull request

## 🏆 Credits 
- Author: [Vali Shaik](https://www.linkedin.com/in/mahaboobvalishaik/) 
- Dataset: Crop Recommendation Dataset on Kaggle 
- Frameworks: Streamlit, Scikit-learn, Pandas, NumPy

⭐ Support

If you found this project useful, please ⭐ star the repository!
