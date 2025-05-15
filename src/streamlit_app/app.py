import requests
import streamlit as st
from datetime import datetime

def taxi_api_call(payload):
    url = "http://nyc_taxi_model_service:8000/fare_predict"
    headers = {'accept': 'application/json'}
    response = requests.post(url, json=payload, headers=headers)
    return response

def main():
    st.title("NYC Taxi Fare Prediction")
    st.write("Enter trip details:")

    pickup_longitude = st.number_input("Pickup Longitude", format="%.6f")
    pickup_latitude = st.number_input("Pickup Latitude", format="%.6f")
    dropoff_longitude = st.number_input("Dropoff Longitude", format="%.6f")
    dropoff_latitude = st.number_input("Dropoff Latitude", format="%.6f")
    passenger_count = st.number_input("Passenger Count", min_value=1, max_value=10, value=1)

    pickup_datetime = st.date_input("Pickup Date", datetime.today())
    pickup_time = st.time_input("Pickup Time", datetime.now().time())

    if st.button("Predict Fare"):
        try:
            pickup_dt = datetime.combine(pickup_datetime, pickup_time)
            pickup_hour = pickup_dt.hour
            pickup_dayofweek = pickup_dt.weekday()
            pickup_month = pickup_dt.month
            pickup_weekday = 1 if pickup_dayofweek < 5 else 0

            payload = {
                "pickup_longitude": pickup_longitude,
                "pickup_latitude": pickup_latitude,
                "dropoff_longitude": dropoff_longitude,
                "dropoff_latitude": dropoff_latitude,
                "passenger_count": passenger_count,
                "pickup_hour": pickup_hour,
                "pickup_dayofweek": pickup_dayofweek,
                "pickup_month": pickup_month,
                "pickup_weekday": pickup_weekday
            }

            response = taxi_api_call(payload)

            if response.status_code == 200:
                prediction = response.json()
                st.success(f"Predicted Fare Amount: ${prediction['predicted_fare']:.2f}")
            else:
                st.error(f"API Error: {response.status_code} - {response.text}")

        except Exception as e:
            st.error(f"Error: {e}")

if __name__ == "__main__":
    main()
