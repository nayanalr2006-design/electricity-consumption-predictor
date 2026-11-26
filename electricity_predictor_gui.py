# Intelligent Electricity Consumption Predictor
# Mini Project: Machine Learning + Tkinter GUI

import tkinter as tk
from tkinter import messagebox
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
import matplotlib.pyplot as plt

# -------------------- SAMPLE DATASET --------------------
data = {
    "temperature": [25,30,22,35,28,32,20,27,33,24,29,36,21,31,26,34,23,28,37,22,
                    26,31,24,34,29,21,32,27,35,23],
    "people": [3,4,2,5,3,4,2,3,5,2,4,5,2,4,3,5,2,3,5,2,3,4,2,5,3,2,4,3,5,2],
    "appliances": [5,8,4,9,6,7,3,5,8,4,7,10,3,8,5,9,4,6,10,3,5,7,4,9,6,3,8,5,10,4],
    "usage_hours": [4,7,3,9,5,6,2,4,8,3,6,10,2,7,4,8,3,5,10,2,4,6,3,9,5,2,7,4,10,3],
    "consumption": [8,18,6,25,12,16,4,9,22,7,17,30,4,20,10,26,6,13,32,5,
                    9,17,7,27,13,5,19,10,29,6]
}
df = pd.DataFrame(data)

# Train/test split and model training
X = df[["temperature", "people", "appliances", "usage_hours"]]
y = df["consumption"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42
)
model = LinearRegression()
model.fit(X_train, y_train)

test_predictions = model.predict(X_test)
mae = mean_absolute_error(y_test, test_predictions)
r2 = r2_score(y_test, test_predictions)

# -------------------- GUI --------------------
root = tk.Tk()
root.title("Intelligent Electricity Consumption Predictor")
root.geometry("650x570")
root.configure(bg="#f3f6fa")

title = tk.Label(root, text="⚡ Intelligent Electricity Predictor",
                 font=("Arial", 20, "bold"), bg="#f3f6fa", fg="#17324d")
title.pack(pady=18)

subtitle = tk.Label(root, text="Estimate household electricity use (kWh/day)",
                   font=("Arial", 11), bg="#f3f6fa", fg="#46596b")
subtitle.pack(pady=2)

form = tk.Frame(root, bg="#f3f6fa")
form.pack(pady=18)

fields = [
    ("Temperature (°C)", "temperature"),
    ("People in household", "people"),
    ("Number of appliances", "appliances"),
    ("Daily usage hours", "usage_hours"),
]
entries = {}

for row, (label_text, key) in enumerate(fields):
    tk.Label(form, text=label_text, font=("Arial", 12),
             bg="#f3f6fa", width=23, anchor="w").grid(row=row, column=0, padx=10, pady=9)
    entry = tk.Entry(form, font=("Arial", 12), width=18)
    entry.grid(row=row, column=1, padx=10, pady=9)
    entries[key] = entry

result_label = tk.Label(root, text="Enter values and click Predict.",
                        font=("Arial", 14, "bold"), bg="#f3f6fa",
                        fg="#17324d", justify="center")
result_label.pack(pady=20)

def predict():
    try:
        temperature = float(entries["temperature"].get())
        people = int(entries["people"].get())
        appliances = int(entries["appliances"].get())
        usage_hours = float(entries["usage_hours"].get())

        if people < 0 or appliances < 0 or usage_hours < 0:
            raise ValueError("Values cannot be negative.")
        if usage_hours > 24:
            raise ValueError("Daily usage hours must be 24 or less.")

        new_data = pd.DataFrame(
            [[temperature, people, appliances, usage_hours]],
            columns=["temperature", "people", "appliances", "usage_hours"]
        )
        prediction = float(model.predict(new_data)[0])
        prediction = max(0, prediction)

        if prediction < 10:
            level = "LOW"
        elif prediction < 20:
            level = "MODERATE"
        else:
            level = "HIGH"

        result_label.config(
            text=f"Predicted consumption: {prediction:.2f} kWh/day\nUsage level: {level}",
            fg="#176b43"
        )
    except ValueError as error:
        messagebox.showerror("Invalid input", str(error) or "Please enter valid numbers.")
    except Exception as error:
        messagebox.showerror("Error", f"Unable to predict: {error}")

def show_chart():
    plt.figure(figsize=(8, 5))
    plt.scatter(y_test, test_predictions)
    plt.xlabel("Actual consumption (kWh/day)")
    plt.ylabel("Predicted consumption (kWh/day)")
    plt.title("Actual vs Predicted Consumption (Test Data)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

buttons = tk.Frame(root, bg="#f3f6fa")
buttons.pack(pady=8)

tk.Button(buttons, text="Predict Consumption", command=predict,
          font=("Arial", 12, "bold"), bg="#176b43", fg="white",
          padx=12, pady=8).grid(row=0, column=0, padx=8)

tk.Button(buttons, text="View Model Graph", command=show_chart,
          font=("Arial", 12), bg="#17324d", fg="white",
          padx=12, pady=8).grid(row=0, column=1, padx=8)

metrics = tk.Label(root, text=f"Model MAE: {mae:.2f} kWh  |  R²: {r2:.2f}",
                   font=("Arial", 10), bg="#f3f6fa", fg="#46596b")
metrics.pack(pady=14)

footer = tk.Label(root, text="Educational prototype using a small synthetic dataset.",
                  font=("Arial", 9), bg="#f3f6fa", fg="#657786")
footer.pack(side="bottom", pady=12)

root.mainloop()
