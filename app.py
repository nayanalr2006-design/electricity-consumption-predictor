
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Electricity Predictor",
    page_icon="⚡",
    layout="wide"
)

st.title("⚡ Intelligent Electricity Consumption Predictor")
st.write("Smart household energy estimation using Machine Learning.")

st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Select Page",
    ["Home", "Prediction", "About"]
)

if page == "Home":
    st.header("Welcome to Our Project")
    st.write(
        "This website estimates household electricity "
        "consumption using household details."
    )
    st.info("Use the Prediction page to estimate electricity usage.")

elif page == "Prediction":
    st.header("🏠 Enter Household Details")

    temperature = st.number_input(
        "Temperature (°C)", 0, 60, 30
    )

    appliances = st.number_input(
        "Number of Appliances", 1, 50, 5
    )

    people = st.number_input(
        "Number of People", 1, 20, 4
    )

    hours = st.number_input(
        "Daily Usage Hours", 1, 24, 6
    )

    if st.button("Predict Electricity Consumption"):
        # Illustrative estimate, not a trained ML model
        consumption = (
            appliances * hours * 0.5
            + people * 0.3
            + temperature * 0.1
        )

        st.success("Estimated consumption calculated!")
        st.metric(
            "Estimated Electricity Consumption",
            f"{consumption:.2f} kWh"
        )

        st.subheader("Energy Saving Tips")
        st.write("• Switch off unused appliances.")
        st.write("• Use LED bulbs.")
        st.write("• Avoid unnecessary electricity usage.")

elif page == "About":
    st.header("About This Project")
    st.write("""
    Project: Intelligent Electricity Consumption Predictor

    Technology:
    - Python
    - Streamlit
    - Pandas
    - Matplotlib

    Objective:
    To estimate household electricity consumption
    using household information.
    """)
st.subheader("💰 Electricity Bill Calculator")

rate = st.number_input(
    "Electricity rate per unit (₹)",
    min_value=0.0,
    value=7.0,
    step=0.5
)

if st.button("Calculate Electricity Bill"):
    bill = prediction * rate

    st.success("Electricity Bill Calculated!")
    st.metric("Estimated Electricity Bill", f"₹{bill:.2f}")