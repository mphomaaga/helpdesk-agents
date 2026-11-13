from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_create_ticket():
    r = client.post("/tickets", json={"title": "Printer broken"})
    assert r.status_code == 201
    body = r.json()
    assert isinstance(body["id"], int)
    assert body["title"] == "Printer broken"
    assert body["status"] == "open"


def test_create_ticket_invalid():
    assert client.post("/tickets", json={}).status_code == 422


def test_list_tickets():
    created = client.post("/tickets", json={"title": "A"}).json()
    r = client.get("/tickets")
    assert r.status_code == 200
    assert created in r.json()


def test_list_tickets_wrong_method():
    assert client.delete("/tickets").status_code == 405


def test_get_ticket():
    created = client.post("/tickets", json={"title": "B"}).json()
    r = client.get(f"/tickets/{created['id']}")
    assert r.status_code == 200
    assert r.json() == created


def test_get_ticket_missing():
    assert client.get("/tickets/999999").status_code == 404


def test_close_ticket():
    created = client.post("/tickets", json={"title": "C"}).json()
    r = client.patch(f"/tickets/{created['id']}")
    assert r.status_code == 200
    assert r.json()["status"] == "closed"
    assert client.get(f"/tickets/{created['id']}").json()["status"] == "closed"


def test_close_ticket_missing():
    assert client.patch("/tickets/999999").status_code == 404
