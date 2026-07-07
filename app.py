import streamlit as st
import joblib
import numpy as np

# Load trained model
model = joblib.load("model.pkl")

st.title("🏠 House Price Prediction")

st.write("Enter the house details below:")

area_type = st.number_input("Area Type (Encoded)", min_value=0, step=1)
availability = st.number_input("Availability (Encoded)", min_value=0, step=1)
location = st.number_input("Location (Encoded)", min_value=0, step=1)
bhk = st.number_input("BHK", min_value=1, step=1)
total_sqft = st.number_input("Total Sqft", min_value=100.0)
bath = st.number_input("Bathrooms", min_value=1, step=1)
balcony = st.number_input("Balconies", min_value=0, step=1)

if st.button("Predict Price"):
    data = np.array([[area_type, availability, location,
                      bhk, total_sqft, bath, balcony]])

    prediction = model.predict(data)

    st.success(f"🏠 Predicted House Price: {prediction[0]:.2f} Lakhs")