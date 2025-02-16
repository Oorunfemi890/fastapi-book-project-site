from fastapi import APIRouter
from api.routes import books, stage2_router  # Import both routers

api_router = APIRouter()

@api_router.get("/", tags=["root"])
async def read_root():
    return {"message": "Welcome to FastAPI!"}

# Include the stage2 endpoint router
api_router.include_router(stage2_router, tags=["stage2"])

# Include the books endpoint router
api_router.include_router(books.router, prefix="/books", tags=["books"])
