from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import os
import pandas as pd

# Initialize FastAPI
app = FastAPI()

# Define a Pydantic model for request data
class RequestData(BaseModel):
    pickup_longitude: float
    pickup_latitude: float
    dropoff_longitude: float
    dropoff_latitude: float
    passenger_count: int
    pickup_hour: int
    pickup_dayofweek: int
    pickup_month: int
    pickup_weekday: int

# Function to get the model path
def get_model_path():
    return f"{os.path.dirname(os.path.realpath(__file__))}/nyc_taxi_rf_model.pkl"

# Function to load the model
def load_model():
    model_path = get_model_path()
    model = joblib.load(model_path)
    return model

# Load the model once at startup
model = load_model()
required_features = model.feature_names_in_ if hasattr(model, 'feature_names_in_') else None

# Define a route for making predictions
@app.post("/fare_predict")
async def predict(data: RequestData):
    # Create an input DataFrame matching the model's expected feature set
    input_df = pd.DataFrame([{feature: 0 for feature in required_features}])
    
    # Update the DataFrame with provided values
    input_df["pickup_longitude"] = data.pickup_longitude
    input_df["pickup_latitude"] = data.pickup_latitude
    input_df["dropoff_longitude"] = data.dropoff_longitude
    input_df["dropoff_latitude"] = data.dropoff_latitude
    input_df["passenger_count"] = data.passenger_count
    input_df["pickup_hour"] = data.pickup_hour
    input_df["pickup_dayofweek"] = data.pickup_dayofweek
    input_df["pickup_month"] = data.pickup_month
    input_df["pickup_weekday"] = data.pickup_weekday
    
    # Make prediction
    try:
        prediction = model.predict(input_df)
        return {"predicted_fare": float(prediction[0])}
    except ValueError as e:
        return {"error": str(e)}
