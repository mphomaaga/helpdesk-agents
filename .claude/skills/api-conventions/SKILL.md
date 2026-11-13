---
name: api-conventions
description: House rules for endpoints in this API. Use when adding or changing routes, models or error responses.
---

# API conventions

- Plural nouns for resources: /tickets, /tickets/{id}.
- Pydantic models for request and response bodies, in the same module as the routes.
- Each resource gets its own APIRouter in app/<resource>.py, included in app/main.py.
- Errors: raise HTTPException with 404 for missing items, 422 is left to FastAPI validation.
- Tests use fastapi.testclient.TestClient; one happy-path and one failure-path test per endpoint.
