from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def home():
    return {
        "message": "Welcome to FitBuddy AI"
    }


@router.get("/health")
def health():
    return {
        "status": "healthy"
    }