import streamlit as st
import joblib
import numpy as np
import pandas as pd

st.set_page_config(page_title="Student Predictor", layout="wide")

st.title("🎓 Student Performance Predictor 🇹🇿")
st.markdown("---")

try:
    # Load model with error handling
    @st.cache_data
    def load_model():
        model = joblib.load('best_model.pkl')
        return model
    
    model = load_model()
    st.success("✅ Model loaded successfully!")
    
except Exception as e:
    st.error(f"❌ Model loading failed: {str(e)}")
    st.stop()

# Sidebar with info
with st.sidebar:
    st.header("📊 How to use")
    st.info("Enter student details → Click Predict → See score!")

# Main inputs
col1, col2, col3 = st.columns(3)
with col1:
    study_hours = st.slider("📚 Weekly Study Hours", 0.0, 40.0, 15.0)
with col2:
    attendance = st.slider("📈 Attendance %", 0.0, 100.0, 85.0)
with col3:
    participation = st.slider("💬 Class Participation (0-10)", 0.0, 10.0, 5.0)

# Predict button
if st.button("🔮 **PREDICT TOTAL SCORE**", type="primary", use_container_width=True):
    try:
        # Create input array
        input_data = np.array([[study_hours, attendance, participation]])
        prediction = model.predict(input_data)[0]
        
        # Display results
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Predicted Score", f"{prediction:.1f}/100")
        with col2:
            grade = "A" if prediction >= 90 else "B" if prediction >= 80 else "C" if prediction >= 70 else "D"
            st.metric("Grade", grade)
        
        st.balloons()
        
    except Exception as e:
        st.error(f"Prediction failed: {str(e)}")

st.markdown("---")
st.markdown("*Built for Tanzanian students* 🇹🇿")