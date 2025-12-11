from fastapi import FastAPI
import joblib
import numpy as np
from fastapi.middleware.cors import CORSMiddleware


app=FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all origins for now
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


#load saved files
model=joblib.load("student_data_cleaned_for_ML.pkl")
norm_values=joblib.load("normalization_values.pkl")
label_map=joblib.load("label_map.pkl")
#extract normalization values
age_min=norm_values["age_min"]
age_max=norm_values["age_max"]
marks_min=norm_values["marks_min"]
marks_max=norm_values["marks_max"]

#Function to normalize new inputs
def nornalize_new(age,marks):
    age_norm = (age - age_min) / (age_max - age_min) if age_max != age_min else 0.0
    marks_norm = (marks - marks_min) / (marks_max - marks_min) if marks_max != marks_min else 0.0
    return np.array([[age_norm, marks_norm]])

@app.get("/")
def home():
    return{"message":"ML API is running"}

@app.get("/predict")
def predict(age:float,marks:float):
    X= nornalize_new(age,marks)
    pred_class=model.predict(X)[0]
    pred_label=label_map[pred_class]
    pred_proba=model.predict_proba(X)[0].tolist()
    return{
        "age":age,
        "marks":marks,
        "predicted_class":int(pred_class),
        "predicted_label":pred_label,
        "probabilities":{"Low":pred_proba[0],"Medium":pred_proba[1],"High":pred_proba[2]}
    }
    
