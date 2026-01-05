from fastapi import FastAPI

app = FastAPI(title="Space Control System")

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/info")
def health_info():
    return {"info": "info aqui"}