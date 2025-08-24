# Car Price Prediction API 

**Car Price Prediction API** is a full-stack project that predicts car prices based on technical specifications and vehicle features using a **machine learning model**. It’s built with **FastAPI** for backend, ready for deployment via **Docker**, and comes with an optional **frontend** for testing.

---

## Features

- Predict car prices based on features like Make, Year, Engine HP, Cylinders, Transmission, etc.
- Robust ML pipeline with preprocessing, scaling, and encoding.
- RESTful API built with FastAPI.
- Fully containerized with Docker for smooth deployment.
- Optional frontend interface for testing and demonstration.
- Deployed live on Render (URL included below).
- Easy to extend and integrate into bigger applications.

---

## Tech Stack

- **Backend:** Python, FastAPI
- **Machine Learning:** scikit-learn, pandas, numpy, joblib
- **Deployment:** Docker, Render
- **Frontend (optional):** HTML, CSS, JavaScript
- **Data Handling:** pandas
- **Serialization:** joblib for model persistence

---

## Project Structure

```bash
├─ app/ # FastAPI application
│ ├─ main.py # API entrypoint
│ ├─ model.py # Prediction functions
│ └─ schemas.py # Pydantic models
├─ models/ # Trained ML models (joblib)
├─ data/ # Dataset or any reference data (optional)
├─ frontend/ # Optional HTML/CSS/JS frontend
├─ Dockerfile # For containerization
├─ requirements.txt # Python dependencies
├─ README.md
```


---

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/KouroshBeheshtinejad/car_price_prediction_api.git
cd car_price_prediction_api
```

### 2. Set up Python environments
```bash
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows
pip install -r requirements.txt
```

### 3. Run API locally
```bash
uvicorn app.main:app --reload --port 5000
```

---

## API Usage

### 1. Root endpoint
```bash
GET /
```
Response:
```bash
{"message": "Welcome to Car Price Prediction API!"}
```

### 2. Predict endpoint
```bash
POST /predict
Content-Type: application/json
```
Request Body Example
```bash
{
  "Make": "Toyota",
  "Year": 2020,
  "Engine_HP": 200,
  "Engine_Cylinders": 4,
  "Transmission_Type": "Automatic",
  "Driven_Wheels": "front",
  "Vehicle_Size": "Midsize",
  "Vehicle_Style": "Sedan",
  "Number_of_Doors": 4,
  "avg_mpg": 28
}
```
Response Example
```bash
{
  "predicted_price": 34657.65
}
```

---

## Deployment
- This project is containerized with **Docker**.
- Can be deployed anywhere: Render, AWS, Heroku, Google Cloud, etc.
- Example Render live deployment: https://car-price-prediction-byxo.onrender.com.

### Docker Commands
```bash
docker build -t car-price-api .
docker run -p 5000:5000 car-price-api
```

---

## Model Details
- Trained using **scikit-learn**.
- Includes preprocessing for categorical and numerical features.
- Pipeline steps: Scaling, OneHotEncoding, Ridge Regression.
- Stored as `models/car_price_pipeline.pkl`.

**Note**: Make sure the scikit-learn version matches or is compatible to avoid unpickling warnings

---

## Testing & Validation
- Test the API endpoints using **Postman**, **curl**, or the optional frontend.
- Validate edge cases, missing fields, and incorrect inputs.
- Ensure the predicted prices are reasonable for different car types.

---

## Contribution
- Clone the repo and submit PRs for new features, frontend upgrades, or additional ML models.
- Add new car-related features or datasets to improve predictions.

---

## Author
Kourosh Beheshtinejad
- Github: **[Kourosh Beheshtinejad](https://github.com/KouroshBeheshtinejad)**

---

## Notes/Future Improvements
- Add real car datasets for broader coverage.
- Expand frontend into a full car review and news portal.
- Integrate user authentication for personalized predictions.
- Add more ML models (Random Forest, XGBoost) for better accuracy.
- Continuous deployment setup for automatic updates.

---

## Acknowledgements
- FastAPI & Uvicorn for lightweight API
- scikit-learn for ML pipeline
- Render.com for hassle-free deployment