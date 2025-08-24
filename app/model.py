import joblib
import numpy as np
import pandas as pd

# Load trained pipeline
pipe = joblib.load("models/car_price_pipeline.pkl")

def predict_price(input_data: dict):
    # Create DataFrame
    df = pd.DataFrame([input_data])

    rename_dict = {
        "Engine_HP": "Engine HP",
        "Engine_Cylinders": "Engine Cylinders",
        "Number_of_Doors": "Number of Doors",
        "Transmission_Type": "Transmission Type",
        "Engine_Fuel_Type": "Engine Fuel Type",
        "Vehicle_Size": "Vehicle Size",
        "Vehicle_Style": "Vehicle Style"
    }
    df.rename(columns=rename_dict, inplace=True)

    # Fill missing categorical
    for col in ['Engine Fuel Type', 'Vehicle Size', 'Vehicle Style', 'Driven_Wheels', 'Make']:
        if col not in df.columns or df[col].isnull().any():
            df[col] = "unknown"

    # Fill missing numeric
    for col in ['Engine HP', 'Engine Cylinders', 'Number of Doors', 'avg_mpg', 'Year']:
        if col not in df.columns or df[col].isnull().any():
            df[col] = 0

    # Predict
    y_pred_log = pipe.predict(df)
    y_pred_log = np.clip(y_pred_log, a_min=None, a_max=15)
    y_pred_real = np.expm1(y_pred_log)

    return float(y_pred_real[0])