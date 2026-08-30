# api directory -> that going to routes the request depending on upon request the front end is
#sending.
from fastapi import APIRouter

from src.backend.schemas.prediction_schema import (
    PredictionRequest,
    PredictionResponse
)

from src.backend.services.predictor import predict_disease

router = APIRouter()

# previous we said app = fastapi and app.get but now we have separate router

@router.get("/health") # this is the YILT API
def health_check():
    return {
        "status" : "ok",
        "message": "API is healthy and running"
    }
@router.post("/predict", response_model=PredictionResponse)
def predict_endpoint(request: PredictionRequest):
  
    disease = request.disease # this disease we aleady config on schemas
    features = request.features
    result = predict_disease(
        disease=disease,
        input_data=features
    ) # this result in the form of dictionary
    # and to convert predictionresponse format

    return PredictionResponse(**result)
