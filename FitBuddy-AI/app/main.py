from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from .config import settings
from .routes import router

app = FastAPI(
    title=settings.app_name,
    description="AI-powered 7-day wellness plan generator using Gemini.",
    version="1.0.0",
)

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(router)


@app.get("/api")
def api_root():
    return {
        "message": "FitBuddy API is running",
        "docs": "/docs",
        "health": "/api/health",
    }