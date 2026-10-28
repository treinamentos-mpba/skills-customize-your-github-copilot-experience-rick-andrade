from fastapi import FastAPI

app = FastAPI(title="Book API")


@app.get("/health")
def health_check():
    return {"status": "ok"}
