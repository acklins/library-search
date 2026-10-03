#Library Search API
from fastapi import FastAPI
from app.routers import books

app = FastAPI(title="Library Search API")

app.include_router(
    books.router, 
    prefix="/books", 
    tags=["books"]
)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        app, 
        host="0.0.0.0", 
        port=8000
    )
