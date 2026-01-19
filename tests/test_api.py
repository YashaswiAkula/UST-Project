from fastapi.testclient import TestClient
from Project.app import app


client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_create_ticket_api():
    response = client.post(
        "/tickets",
        headers={"x-user-email": "customer1@example.com"},
        json={
            "title": "API Ticket",
            "description": "Created via API",
            "priority": "Medium"
        }
    )

    assert response.status_code == 201
    assert response.json()["title"] == "API Ticket"
