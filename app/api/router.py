# app/api/v1/endpoints/example.py
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def read_root():
    return {"message": "Hello from FastAPI"}

@router.post("/ollama")
def get_summary(number_of_emails: int, type: str):
    from app.services.app import query_ollama
    summary = query_ollama(number_of_emails, type)
    return summary

@router.post("/gemini")
def get_summary(number_of_emails: int, type: str):
    print(f"Parsing {number_of_emails} emails of type {type}")
    from app.services.app import query_gemini
    summary = query_gemini(number_of_emails, type)
    return summary

