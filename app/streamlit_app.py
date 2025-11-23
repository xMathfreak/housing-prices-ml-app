import os
import streamlit as st
import pandas as pd
import pickle

MODEL_PATH = os.path.join("models", "final_model.pkl")

st.title("House Pricing Predictions")
st.write("Enter home features below to predict the price.")

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

OverallQual = st.slider("Overall Quality (1 - 10)", 1, 10, 5)
GrLivArea = st.number_input("Above Ground Living Area (ft²)", 300, 6000, 1500)
GarageCars = st.slider("Garage Car Capacity", 0, 4, 2)
GarageArea = st.number_input("Garage Area (ft²)", 0, 1500, 400)
TotalBsmtSF = st.number_input("Basement Area (ft²)", 0, 3000, 800)
FirstFlrSF = st.number_input("1st Floor Area (ft²)", 200, 3000, 1000)
FullBath = st.slider("Number of Full Bathrooms", 0, 4, 2)
YearBuilt = st.number_input("Year Built", 1870, 2024, 1995)
YearRemodAdd = st.number_input("Year Remodeled", 1950, 2024, 2005)
LotArea = st.number_input("Lot Area (ft²)", 1000, 50000, 8000)

KitchenQual = st.selectbox("Kitchen Quality", ["Excellent", "Good", "Average", "Fair"])

input_df = pd.DataFrame({
    "OverallQual": [OverallQual],
    "GrLivArea": [GrLivArea],
    "GarageCars": [GarageCars],
    "GarageArea": [GarageArea],
    "TotalBsmtSF": [TotalBsmtSF],
    "1stFlrSF": [FirstFlrSF],
    "FullBath": [FullBath],
    "YearBuilt": [YearBuilt],
    "YearRemodAdd": [YearRemodAdd],
    "LotArea": [LotArea],
    "KitchenQual": [KitchenQual]
})

if st.button("Predict Price"):
    prediction = model.predict(input_df)[0]
    st.success(f"Estimated House Price: ${prediction:,.0f}")