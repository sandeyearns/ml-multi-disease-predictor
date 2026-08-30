# schema directory -> wil validate input and output request and response that is coming 
# and going from API

from typing import Dict
from pydantic import BaseModel

class PredictionRequest(BaseModel): 
    # PredictionRequest is a input data the API will recieve for api end points

    # below disease and features indicating each request should have key value pairs
    # so request would be having this payload in the form of jason. jason is like a python dictionary.
    # NOTE: So, here we are saying that when my API end points is called ut should have 2 values.
    disease: str
    features: Dict[str, int | float]
    # so it comes from predictor.py file from def predict_disease(disease: str, input_data: dict):


class PredictionResponse(BaseModel):
    disease: str
    prediction: int
    probability: float
