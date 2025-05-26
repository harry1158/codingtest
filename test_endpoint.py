from fastapi.testclient import TestClient
from main import app  

client = TestClient(app)

def test_split_endpoint_normal():
    data = {
        "count": 3,
        "amount": 1000,
        "delimiter": ","
    }
    response = client.post("/api/v1/split", json=data)
    assert response.status_code == 200
    assert response.json() == {"perPerson": [333, 333, 334]}

def test_split_endpoint_error():
    data = {
        "count": 0,
        "amount": 1000,pip
        "delimiter": ","
    }
    response = client.post("/api/v1/split", json=data)
    assert response.status_code == 400
    assert "error" in response.json()  
