from dotenv import load_dotenv
from pydantic_settings import BaseSettings
import os

# Load from config.env file
load_dotenv("config.env")

class Settings(BaseSettings):
    # Try to load from environment first, then use hardcoded as fallback
    TAVILY_API_KEY: str = os.getenv("TAVILY_API_KEY", "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")
    
    class Config:
        env_file = "config.env"

