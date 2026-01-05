from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="Space Control System")

app.include_router(router)

@app.get("/health")
def health_check():
    return {"status": "ok"}