from fastapi import FastAPI

app = FastAPI()

@app.get("/healthcheck")
async def healtcheck() -> dict:
    return {"status": "ok"}