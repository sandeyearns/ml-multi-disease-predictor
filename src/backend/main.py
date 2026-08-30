from fastapi import FastAPI

from src.backend.api.routes import router

app = FastAPI(
    title="Dr. ML Prediction App",
    version="1.0.0",
    description="Multi-disease prediction backend"
)

app.include_router(router, prefix="/api")
# instead of localhost:8000/health or predict
# now 0> localhost:8000/api/predict or health

# NOTE: RUN --> python -m src.backend.main
#               uvicorn src.backend.main:app  (--reload optional to referesh)
#               THEN OPEN -> http://127.0.0.1:8000/docs
#                            http://127.0.0.1:8000/api/health OR PREDITCT


# For your Windows + Pydantic setup, do this:
# 1. Activate .venv
# .\.venv\Scripts\Activate.ps1

# 2. Start FastAPI
# uvicorn src.backend.main:app --reload
# set -a
# source .env
# set +a
# because my settings.py already has:
# model_config = SettingsConfigDict(
#     env_file=".env",
#     env_file_encoding="utf-8",
#     extra="allow"
# )
# So Settings() automatically reads .env.

# NOTE: THIS IS TO PASTE IN THIS WAY 


# {

#     "disease" : "diabetes",
#     "features" :  {
#     "Pregnancies": 2,
#     "Glucose": 120,
#     "BloodPressure": 70,
#     "SkinThickness": 25,
#     "Insulin": 80,
#     "BMI": 28.5,
#     "DiabetesPedigreeFunction": 0.5,
#     "Age": 30

#     }
# }





# {

#     "disease" : "heart_disease",
#     "features" :  {
#     "age": 52,
#     "sex": 1,
#     "cp": 0,
#     "trestbps": 125,
#     "chol": 212,
#     "fbs": 0,
#     "restecg": 1,
#     "thalach": 168,
#     "exang": 0,
#     "oldpeak": 1.0,
#     "slope": 2,
#     "ca": 0,
#     "thal": 2
#     }
# }


