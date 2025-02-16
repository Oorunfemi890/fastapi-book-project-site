from fastapi import APIRouter
from api.routes import books, stage2_router  # Ensure stage2_router is imported

from api.routes import books

api_router = APIRouter()

@api_router.get("/", tags=["root"])
async def read_root():
    return {"message": "Welcome to FastAPI!"}
router.include_router(stage2_router)

api_router.include_router(books.router, prefix="/books", tags=["books"])
