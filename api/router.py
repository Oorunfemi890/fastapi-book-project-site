from fastapi import APIRouter
from api.routes.books import router as books_router
from api.routes.stage2 import router as stage2_router  # Import directly from stage2.py

api_router = APIRouter()

@api_router.get("/", tags=["root"])
async def read_root():
    return {"message": "Welcome to FastAPI!"}

# Include the stage2 endpoint router
api_router.include_router(stage2_router, tags=["stage2"])

# Include the books endpoint router
api_router.include_router(books_router, prefix="/books", tags=["books"])

