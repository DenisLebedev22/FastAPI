import pytest
from fastapi.testclient import TestClient
from main import app

# Создаем клиент для тестирования без Nginx
client = TestClient(app)

def test_read_main():
    # Тестируем напрямую FastAPI, минуя Nginx
    response = client.get("/")
    print(f"\nGET / -> {response.status_code}")
    print(f"Ответ: {response.json()}")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

def test_create_item():
    response = client.post("/items", json={"name": "test"})
    print(f"\nPOST /items -> {response.status_code}")
    print(f"Ответ: {response.json()}")
    assert response.status_code == 201
    assert response.json()["item"]["name"] == "test"

def test_get_items():
    response = client.get("/items")
    print(f"\nGET /items -> {response.status_code}")
    print(f"Ответ: {response.json()}")
    assert response.status_code == 200

