# app/main.py
from fastapi import FastAPI

from app.api.router import router
from app.core.config import settings
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title=settings.app_name, debug=settings.debug)

# Include your API routes
app.include_router(router, prefix="/api", tags=["Example"])

app.mount("/", StaticFiles(directory="app/static", html=True), name="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost", "http://localhost:8000"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)