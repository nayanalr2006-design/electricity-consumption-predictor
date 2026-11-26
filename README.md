# Intelligent Electricity Consumption Predictor

## Abstract
This project estimates household electricity consumption in kWh/day using a Linear Regression model. It uses temperature, household size, appliance count and usage hours as inputs. A Tkinter graphical interface accepts user values, shows the predicted daily consumption and classifies the estimate as LOW, MODERATE or HIGH. It also displays a test-set comparison graph.

## Requirements
- Python 3.9+
- pandas
- scikit-learn
- matplotlib
- tkinter (normally included with Python on Windows)

## Installation
Open a terminal in this project folder and run:

```bash
pip install pandas scikit-learn matplotlib
```

## Run
```bash
python electricity_predictor_gui.py
```

## Inputs
- Temperature (°C)
- Number of people in household
- Number of appliances
- Daily appliance usage hours

## Output
- Predicted consumption in kWh/day
- Usage category
- Test-data graph

## Important limitation
The project uses a small synthetic dataset for demonstration. Predictions are not a utility-grade forecast and should not be used for billing or energy-management decisions. Replace the sample dataset with measured consumption records for realistic performance.
