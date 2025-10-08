from fastapi import FastAPI
from app.api.routers import health as health_router

app = FastAPI(title="Vichintarka API")

app.include_router(health_router.router, prefix="/api")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
