from fastapi import APIRouter

# 1. El objeto DEBE llamarse 'router' para coincidir con tu importación en main.py
router = APIRouter(prefix="/uploads", tags=["Uploads"])

@router.post("/")
async def upload_file():
    return {"message": "Archivo subido correctamente"}