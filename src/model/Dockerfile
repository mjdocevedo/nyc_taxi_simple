# Use an official Python image as the base
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the model file and API script into the container
COPY nyc_taxi_rf_model.pkl .  
COPY nyc_taxi_api.py .        
# Expose the port where FastAPI will run
EXPOSE 8000

# Run the API with Uvicorn
CMD ["uvicorn", "nyc_taxi_api:app", "--host", "0.0.0.0", "--port", "8000"]
