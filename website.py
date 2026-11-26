import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# ---------------- PAGE SETTINGS ----------------
st.set_page_config(
    page_title="Smart Electricity Predictor",
    page_icon="⚡",
    layout="wide"
)

# ---------------- DESIGN ----------------
st.markdown("""
<style>
.stApp {
    background-color: #f4f7fb;
}
h1, h2, h3 {
    color: #12345a;
}
[data-testid="stMetric"] {
    background-color: white;
    padding: 18px;
    border-radius: 12px;
    border: 1px solid #e0e7ef;
}
</style>
""", unsafe_allow_html=True)

# ---------------- DEMO ML MODEL ----------------
np.random.seed(42)

data_size = 500

people_data = np.random.randint(1, 8, data_size)
appliances_data = np.random.randint(3, 20, data_size)
temperature_data = np.random.randint(18, 42, data_size)
previous_data = np.random.uniform(50, 600, data_size)

target_data = (
    previous_data * 0.65
    + people_data * 35
    + appliances_data * 12
    + temperature_data * 4
    + np.random.normal(0, 20, data_size)
)

X = pd.DataFrame({
    "Previous Units": previous_data,
    "People": people_data,
    "Appliances": appliances_data,
    "Temperature": temperature_data
})

model = LinearRegression()
model.fit(X, target_data)

# ---------------- SIDEBAR ----------------
st.sidebar.title("⚡ Smart Energy")
page = st.sidebar.radio(
    "Navigation",
    ["Home", "Prediction", "Insights", "About"]
)

st.sidebar.markdown("---")
st.sidebar.caption("Intelligent Electricity Consumption Predictor")

# ---------------- HOME ----------------
if page == "Home":

    st.title("⚡ Intelligent Electricity Consumption Predictor")

    st.markdown(
        "### Smart Machine Learning Dashboard"
    )

    st.write(
        "Predict household electricity consumption "
        "and understand your energy usage."
    )

    col1, col2, col3 = st.columns(3)

    col1.metric("Project", "Smart Energy")
    col2.metric("Technology", "Machine Learning")
    col3.metric("Algorithm", "Linear Regression")

    st.markdown("---")

    st.subheader("Welcome to the Energy Dashboard")

    st.write("""
    This application estimates future household electricity
    consumption using household information and a
    Machine Learning model.
    """)

    st.info("Select Prediction from the sidebar to begin.")

# ---------------- PREDICTION ----------------
elif page == "Prediction":

    st.title("🔮 Electricity Consumption Prediction")

    st.write("Enter your household details below.")

    col1, col2 = st.columns(2)

    with col1:
        previous_units = st.number_input(
            "Previous electricity usage (kWh)",
            min_value=0.0,
            value=150.0
        )

        people = st.number_input(
            "Number of people",
            min_value=1,
            max_value=20,
            value=3
        )

    with col2:
        appliances = st.number_input(
            "Number of electrical appliances",
            min_value=1,
            max_value=100,
            value=8
        )

        temperature = st.number_input(
            "Average temperature (°C)",
            min_value=0,
            max_value=60,
            value=30
        )

    days = st.number_input(
        "Days for previous consumption",
        min_value=1,
        max_value=365,
        value=30
    )

    tariff = st.number_input(
        "Electricity cost per unit (₹)",
        min_value=0.0,
        value=7.0
    )

    if st.button("⚡ Predict Consumption", use_container_width=True):

        daily_units = previous_units / days

        features = pd.DataFrame([{
            "Previous Units": daily_units * 30,
            "People": people,
            "Appliances": appliances,
            "Temperature": temperature
        }])

        prediction = model.predict(features)[0]
        prediction = max(0, prediction)

        bill = prediction * tariff

        st.markdown("---")
        st.subheader("Prediction Results")

        c1, c2, c3 = st.columns(3)

        c1.metric(
            "Predicted Monthly Units",
            f"{prediction:.2f} kWh"
        )

        c2.metric(
            "Estimated Electricity Bill",
            f"₹ {bill:.2f}"
        )

        c3.metric(
            "Average Daily Usage",
            f"{prediction / 30:.2f} kWh"
        )

        st.subheader("Consumption Comparison")

        chart_data = pd.DataFrame({
            "Category": ["Previous", "Predicted"],
            "Units (kWh)": [
                previous_units / days * 30,
                prediction
            ]
        })

        st.bar_chart(
            chart_data.set_index("Category")
        )

        st.subheader("Energy Saving Suggestions")

        tips = [
            "Switch off lights when not in use.",
            "Use LED bulbs.",
            "Avoid leaving appliances on standby.",
            "Use energy-efficient appliances.",
            "Monitor your electricity usage regularly."
        ]

        for tip in tips:
            st.write("💡", tip)

# ---------------- INSIGHTS ----------------
elif page == "Insights":

    st.title("📊 Energy Insights")

    st.write(
        "Understand the factors that affect electricity consumption."
    )

    st.markdown("""
    ### Factors influencing electricity usage

    - **People:** More occupants can increase electricity use.
    - **Appliances:** More electrical devices can increase demand.
    - **Temperature:** Weather conditions can affect cooling and heating.
    - **Previous consumption:** Historical usage helps estimate future usage.
    """)

    st.subheader("Example Consumption")

    example = pd.DataFrame({
        "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
        "Units": [120, 135, 145, 170, 190, 160]
    })

    st.line_chart(
        example.set_index("Month")
    )

    st.caption("The graph above is illustrative sample data.")

# ---------------- ABOUT ----------------
elif page == "About":

    st.title("ℹ️ About the Project")

    st.write("""
    ### Intelligent Electricity Consumption Predictor

    This mini-project uses Machine Learning to estimate
    household electricity consumption.

    **Technologies used:**

    - Python
    - Streamlit
    - Pandas
    - NumPy
    - Scikit-learn
    - Matplotlib

    **Algorithm:**

    Linear Regression

    **Objective:**

    To estimate electricity consumption and encourage
    efficient electricity usage.
    """)

    st.warning(
        "The current model is trained on synthetic demonstration "
        "data. Its predictions are not trained on actual meter records "
        "and should not be used for billing."
    )

# ---------------- FOOTER ----------------
st.markdown("---")
st.caption("Mini Project | Intelligent Electricity Consumption Predictor")