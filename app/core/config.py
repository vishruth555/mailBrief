# app/core/config.py
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Email Summarization App"
    debug: bool = True

    EMAIL_USERNAME: str = ""
    EMAIL_PASSWORD: str = ""
    IMAP_SERVER: str = "imap.gmail.com"
    GEMINI_API_KEY: str = ""
    OLLAMA_MODEL: str = "llama3.2"

    class Config:
        env_file = ".env"

settings = Settings()
