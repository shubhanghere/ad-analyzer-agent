import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    # Changed from OPENAI_API_KEY to GOOGLE_API_KEY
    GOOGLE_API_KEY: str = os.getenv("GOOGLE_API_KEY")

    class Config:
        case_sensitive = True

settings = Settings()