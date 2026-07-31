
import streamlit as st
import joblib
import numpy as np

# Load saved model
model = joblib.load("best_svm_iris.pkl")

# Page settings
st.set_page_config(
    page_title="Iris Flower Prediction",
    page_icon="🌸"
)

# Title
st.title("🌸 Iris Flower Prediction App")

st.write("Enter the flower measurements below:")

# Input fields
sepal_length = st.number_input(
    "Sepal Length (cm)",
    min_value=0.0,
    max_value=10.0,
    value=5.1
)

sepal_width = st.number_input(
    "Sepal Width (cm)",
    min_value=0.0,
    max_value=10.0,
    value=3.5
)

petal_length = st.number_input(
    "Petal Length (cm)",
    min_value=0.0,
    max_value=10.0,
    value=1.4
)

petal_width = st.number_input(
    "Petal Width (cm)",
    min_value=0.0,
    max_value=10.0,
    value=0.2
)

# Prediction button
if st.button("Predict Flower"):

    # Prepare input
    input_data = np.array([[
        sepal_length,
        sepal_width,
        petal_length,
        petal_width
    ]])

    # Prediction
    prediction = model.predict(input_data)[0]

    # Class names
    flower_names = [
        "Setosa",
        "Versicolor",
        "Virginica"
    ]

    result = flower_names[prediction]

    st.success(f"🌸 Predicted Flower: {result}")
