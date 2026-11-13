from fastapi import FastAPI

app = FastAPI(title="Helpdesk API")


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}
