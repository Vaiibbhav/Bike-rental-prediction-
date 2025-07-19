import streamlit as st
import pandas as pd
import joblib

# Load the trained model (pipeline with preprocessor)
model = joblib.load("final_bike_rental_model.joblib")

# App Title
st.set_page_config(page_title="Bike Rental Predictor", page_icon="🚲")
st.title("🚲 Daily Bike Rental Demand Prediction")
st.markdown("Enter the conditions below to estimate the number of bike rentals.")

# Sidebar input form
with st.form("input_form"):
    st.subheader("📋 Input Features")

    season = st.selectbox("Season", [1, 2, 3, 4], format_func=lambda x: {
        1: "Spring", 2: "Summer", 3: "Fall", 4: "Winter"}[x])
    yr = st.selectbox("Year", [0, 1], format_func=lambda x: "2011" if x == 0 else "2012")
    mnth = st.slider("Month", 1, 12, 6)
    holiday = st.selectbox("Is it a holiday?", [0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
    weekday = st.slider("Day of Week (0=Sun)", 0, 6, 2)
    workingday = st.selectbox("Is it a working day?", [0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
    weathersit = st.selectbox("Weather Situation", [1, 2, 3], format_func=lambda x: {
        1: "Clear or Partly Cloudy", 2: "Mist + Cloudy", 3: "Light Snow/Rain"}[x])

    temp = st.slider("Temperature (normalized)", 0.0, 1.0, 0.5)
    atemp = st.slider("Feels Like Temp (normalized)", 0.0, 1.0, 0.5)
    hum = st.slider("Humidity (normalized)", 0.0, 1.0, 0.5)
    windspeed = st.slider("Windspeed (normalized)", 0.0, 1.0, 0.2)

    submitted = st.form_submit_button("🚲 Predict Rentals")

# Prediction
if submitted:
    input_data = pd.DataFrame([{
        "season": season,
        "yr": yr,
        "mnth": mnth,
        "holiday": holiday,
        "weekday": weekday,
        "workingday": workingday,
        "weathersit": weathersit,
        "temp": temp,
        "atemp": atemp,
        "hum": hum,
        "windspeed": windspeed
    }])

    prediction = model.predict(input_data)[0]
    st.success(f"📈 Predicted Number of Bike Rentals: **{int(prediction):,} bikes**")
