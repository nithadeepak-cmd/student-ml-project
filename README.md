Student ML Project

A simple Machine Learning mini-project that predicts a student's performance level (Low, Medium, High) based on Age and Marks.

This repository contains two parts:

student-ml-project
│
├── api → Flask-based Machine Learning API
└── ui → React-based Frontend UI

This is one of my early ML learning projects, built using a very small sample dataset (5 records) just to understand the end-to-end workflow of ML + API + UI + Hosting.

LIVE DEMO

Backend API (Render):
https://student-ml-api.onrender.com/predict?age=35&marks=89

Frontend UI (Render):
https://student-ml-ui.onrender.com/

(Note: Render free tier sleeps when idle.)

PROJECT STRUCTURE

student-ml-project/
│
├── api/
│ ├── main.py
│ ├── requirements.txt
│ ├── label_map.pkl
│ ├── normalization_values.pkl
│ └── student_data_cleaned_for_ML.pkl
│
└── ui/
├── public/
├── src/
├── package.json
└── .gitignore

MACHINE LEARNING DETAILS

• Model trained using only 5 sample records (for learning purposes)
• Labels:
0 → Low
1 → Medium
2 → High

• Preprocessing: Min–max normalization
• Model: Basic classifier (demonstration level)

This model is NOT accurate — it is only for learning how to train, save, load, and integrate ML with API & UI.

TECHNOLOGIES USED

Backend (API):
• Python 3
• Flask
• Pickle
• Render (Hosting)

Frontend (UI):
• React (Create React App)
• HTML, CSS, JavaScript
• Fetch API
• Render (Deployment)

UI FEATURES

• Enter Age and Marks
• Sends request to ML API
• Displays:
– Predicted label
– Probabilities (Low, Medium, High)

(No input validations added — kept simple for learning.)

API ENDPOINT

GET /predict?age=VALUE&marks=VALUE

Example:
https://student-ml-api.onrender.com/predict?age=35&marks=89

Sample Response:
{
"age": 35.0,
"marks": 89.0,
"predicted_class": 2,
"predicted_label": "High",
"probabilities": {
"Low": 0.0,
"Medium": 0.23,
"High": 0.77
}
}

HOW TO RUN LOCALLY

Running the API

Step 1:
cd api

Step 2:
pip install -r requirements.txt

Step 3:
python main.py

API available at: http://127.0.0.1:5000/predict?age=20&marks=80

Running the React UI

Step 1:
cd ui

Step 2:
npm install

Step 3:
npm start

UI available at: http://localhost:3000/

FUTURE IMPROVEMENTS

• Train with larger dataset
• Add validations in UI
• Improve model accuracy
• Better error handling
• Charts / confidence visualization in UI
• Dockerize the project

PROJECT PURPOSE

This is a learning project created to understand:

• Training and saving ML models
• Building APIs using Flask
• Connecting frontend to backend
• Deploying APIs and UIs
• Organizing code in GitHub
