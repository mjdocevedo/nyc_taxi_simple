import pickle
import joblib

# Step 1: Create a test model file (for testing purposes)
with open('./nyc_taxi_rf_model.pkl', 'wb') as f:
    pickle.dump("test_model", f)  # Save a simple test string instead of a real model

# Step 2: Try loading the model to test if the file exists and can be read
try:
    with open("nyc_taxi_rf_model.pkl", "rb") as f:
        print(f.read())  # Display the raw content of the file (should print 'test_model')
        model = joblib.load(f)  # Attempt to load it using joblib (should fail, since it's not a real model)

except FileNotFoundError as e:
    print("FileNotFoundError:", e)
except Exception as e:
    print("An error occurred:", e)
