from fastapi import FastAPI

from app.tickets import router as tickets_router

app = FastAPI(title="Helpdesk API")
app.include_router(tickets_router)


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}
