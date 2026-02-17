import streamlit as st
import joblib
import numpy as np

st.title("🎓 Student Score Predictor 🇹🇿")
st.write("Enter student details to predict total score!")

# Load model
model = joblib.load('best_model.pkl')

# Inputs
study_h = st.slider("Weekly Study Hours", 0, 40, 15)
attend = st.slider("Attendance %", 0, 100, 85)
partic = st.slider("Participation (0-10)", 0, 10, 5)

if st.button("🔮 PREDICT SCORE"):
    pred = model.predict([[study_h, attend, partic]])[0]
    st.success(f"**Predicted Score: {pred:.1f}/100**")
    grade = "A" if pred>=85 else "B" if pred>=70 else "C" if pred>=55 else "D" if pred>=40 else "F"
    st.balloons()
    st.info(f"**Expected Grade: {grade}**")