# Step 1: Import necessary libraries
import pandas as pd  # Data manipulation
from sklearn.ensemble import RandomForestRegressor  # Regression algorithm
from sklearn.model_selection import train_test_split  # Split data
import joblib  # Save and load models
import pickle  # Serialization

# Step 2: Load the NYC Taxi dataset
df = pd.read_csv("/home/ubuntu/nyc_taxi/data/nyc_taxi.csv")

# Extract features (X) and target (y)
df["tpep_pickup_datetime"] = pd.to_datetime(df["tpep_pickup_datetime"], errors="coerce")
df["tpep_dropoff_datetime"] = pd.to_datetime(df["tpep_dropoff_datetime"], errors="coerce")
df["pickup_hour"] = df["tpep_pickup_datetime"].dt.hour
df["pickup_dayofweek"] = df["tpep_pickup_datetime"].dt.dayofweek
df["pickup_month"] = df["tpep_pickup_datetime"].dt.month
df["pickup_weekday"] = df["pickup_dayofweek"].apply(lambda x: 1 if x < 5 else 0)
df["trip_duration"] = (df["tpep_dropoff_datetime"] - df["tpep_pickup_datetime"]).dt.total_seconds() / 60
df["total_fare"] = (
        df["fare_amount"]
        + df["extra"]
        + df["mta_tax"]
        + df["improvement_surcharge"]
        + df["tolls_amount"]
        + df.get("Airport_fee", 0)
    )
df = df.drop(columns=["tpep_pickup_datetime", "tpep_dropoff_datetime", "store_and_fwd_flag", "payment_type", "tip_amount", "total_amount", "trip_distance", "trip_duration"])

X = df.drop(["total_fare", "fare_amount"], axis = 1)
y = df["total_fare"]

# Step 3: Train the model
# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the Random Forest Regressor
model = RandomForestRegressor(n_estimators=100, max_depth=5, random_state=42)
model.fit(X_train, y_train)

# Step 4: Save the trained model
# Save the model using joblib
joblib.dump(model, 'src/model/nyc_taxi_rf_model.pkl')

# Alternatively, save the model using pickle
with open('src/model/nyc_taxi_rf_model.pkl', 'wb') as f:
    pickle.dump(model, f)

# Print feature samples
print(X.head())
