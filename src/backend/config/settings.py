from pydantic_settings import BaseSettings

class Settings(BaseSettings):

    log_path: str
    diabetes_model_path: str
    heart_disease_model_path: str
    
    class Config:
        env_file=".env"
        env_file_encoding="utf-8"
     # encoding of the text file so that it can works on other machine also as well
        extra="allow"

 # extra : allow also allow the variable apart from logpath, diabetes, heartd.., from .env to run