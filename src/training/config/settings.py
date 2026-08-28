# NOTE:
# instead of mannually loading example
# import os, from dotenv import load_dotenv, load_env(), log_path = os.getenb(), ... for other..
# we will used pydantic based setting and
#  it also provide control in date type like choosing float, intm string...
# it will also show error in  this file before deployment  which is a effective to know




from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    
    # just take the file or foldername from .env and store there data type in small letter.
    log_path: str

    diabetes_dataset_path: str
    heart_disease_dataset_path: str

    diabetes_model_path: str
    heart_disease_model_path: str

    diabetes_target_col: str
    heart_disease_target_col: str

    test_size: float
    random_state: int

    hyper_params_yaml_path: str

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="allow"
    )


# This overall code manages the application's configuration in one place.

# It reads paths and ML settings from the .env file and validates them using Pydantic,
#  making the application easier to configure and maintain.”

# ROBUST WAY THAN USING load_dotenv()