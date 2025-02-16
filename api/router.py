from fastapi import APIRouter
from api.routes.books import router as books_router
# Removed stage2 router inclusion from here since it’s included directly in main.py

api_router = APIRouter()

@api_router.get("/", tags=["root"])
async def read_root():
    return {"message": "Welcome to FastAPI!"}

# Include the books endpoint router
api_router.include_router(books_router, prefix="/books", tags=["books"])


