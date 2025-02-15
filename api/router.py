from fastapi import APIRouter

from api.routes import books

api_router = APIRouter()

@api_router.get("/", tags=["root"])
async def read_root():
    return {"message": "Welcome to FastAPI!"}

api_router.include_router(books.router, prefix="/books", tags=["books"])
