# 🚖 NYC Taxi Fare Prediction API

This project is a simple API for predicting NYC taxi fares using a machine learning model (Random Forest). It provides an endpoint for making fare predictions based on trip details.

---

## 🚀 Project Structure
- **`data/`** - Directory for the NYC taxi dataset.
- **`src/model/`** - Directory for the model related files (`nyc_taxi_rf_model.pkl`).
- **`nyc_taxi_api.py`** - FastAPI application for fare prediction.
- **`train_model.py`** - Script for training the Random Forest model.
- **`streamlit_app/app.py`** - Streamlit app for a user-friendly interface.

---

## ⚙️ Setup Instructions
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/mjdocevedo/nyc_taxi_simple.git
   cd nyc_taxi

2. **Install Dependencies:**
```bash
pip install -r requirements.txt
```

3. **Train the Model:**
```bash
python src/train_model.py
```

4. **Run the FastAPI Server:**
```bash
uvicorn nyc_taxi_api:app --reload
```

5. **Run the Streamlit App:**
```bash
streamlit run streamlit_app.py
```

## 🚦 API Usage
* Endpoint: POST /fare_predict
* Request JSON Body:

```bash
{
  "pickup_longitude": -73.985428,
  "pickup_latitude": 40.748817,
  "dropoff_longitude": -73.985428,
  "dropoff_latitude": 40.748817,
  "passenger_count": 1
}
```

* Response:

```bash 
{
  "predicted_fare": 12.34
}
```

## 🌐 Streamlit App
The Streamlit app provides a simple user interface for entering trip details and getting fare predictions.

## 📌 Model Details
Model Type: Random Forest Regressor
Features: Trip coordinates, passenger count, time, and additional trip details.
Trained on: NYC Taxi dataset.
