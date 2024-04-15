import os
from typing import Union
from dotenv import load_dotenv
from pathlib import Path

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

class Settings:
    PROYECT_NAME:str = "USER"
    PROYECT_VERSION:str = "1.0"
    MONGODB_DATABASE_NAME:Union[str, None] = os.getenv('MONGODB_DATABASE_NAME')
    MONGODB_PASSWORD:Union[str, None] = os.getenv('MONGODB_PASSWORD')
    MONGODB_USER:Union[str, None] = os.getenv('MONGODB_USER')
    MONGODB_NAME:Union[str, None] = os.getenv('MONGODB_NAME')
    MONGODB_SERVER:Union[str, None] = os.getenv('MONGODB_SERVER')
    SECRET_KEY:Union[str, None] = os.getenv("SECRET_KEY")
    ALGORITHM:Union[str, None] = os.getenv("ALGORITHM")
    MONGODB_DATABASE_URL:str = f"mongodb+srv://{MONGODB_USER}:{MONGODB_PASSWORD}@{MONGODB_SERVER}/?retryWrites=true&w=majority&appName={MONGODB_NAME}"

settings = Settings()
