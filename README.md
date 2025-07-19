# 🚲 Bike Rental Demand Prediction – PRCP-1018

This machine learning project predicts the daily demand for bike rentals based on weather, seasonal, and calendar features. Built as part of the PRCP-1018 assessment, the solution includes end-to-end analysis, model comparison, and a Streamlit web app for real-time predictions.

---

## 📊 Project Overview

- **Goal:** Predict daily rental counts (`cnt`) using weather and date features.
- **Dataset:** `day.csv` (from UCI Bike Sharing Dataset)
- **Duration:** 2011–2012, 731 records

---

## 📁 Project Structure

| File                             | Description                                |
|----------------------------------|--------------------------------------------|
| `Bike_Rental_Prediction_Final.ipynb` | Complete Jupyter Notebook with EDA, modeling, evaluation |
| `final_bike_rental_model.joblib`    | Final trained Random Forest model         |
| `day.csv`                          | Daily bike rental data                    |
| `app.py`                           | Streamlit app for predictions             |
| `requirements.txt`                 | List of dependencies for this project     |

---

## ⚙️ Features Used

- **Numerical:** `temp`, `atemp`, `hum`, `windspeed`
- **Categorical:** `season`, `mnth`, `weekday`, `weathersit`, `yr`, `holiday`, `workingday`

---

## 🧠 Models Compared

- Linear Regression  
- Random Forest Regressor ✅ *(Best Model)*  
- Support Vector Regressor (SVR)  
- XGBoost Regressor  

> **Evaluation Metric:** RMSE on Test Set

---

## 🚀 Run the Streamlit App

Install the dependencies:

```bash
pip install -r requirements.txt
