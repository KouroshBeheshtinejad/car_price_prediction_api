from fastapi import FastAPI
from app.schemas import CarFeatures
from app.model import predict_price
import logging
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Car Price Prediction API")

logging.basicConfig(level=logging.INFO)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware("http")
async def log_requests(request, call_next):
    logging.info(f"Request: {request.method} {request.url}")
    response = await call_next(request)
    logging.info(f"Response status: {response.status_code}")
    return response

@app.get("/")
def read_root():
    return {"message": "Welcome to Car Price Prediction API!"}

@app.post("/predict")
def predict(car: CarFeatures):
    try:
        input_data = car.dict()
        price = predict_price(input_data)
        return {"predicted_price": price}
    except Exception as e:
        logging.error(f"Prediction error: {str(e)}")
        return {"error": str(e)}