import pytest

from src.app import create_app


@pytest.fixture()
def client():
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as c:
        yield c


# /health


def test_health_returns_200(client):
    res = client.get("/health")
    assert res.status_code == 200


def test_health_payload(client):
    res = client.get("/health")
    assert res.get_json() == {"status": "ok"}


# /items


def test_list_items_returns_200(client):
    res = client.get("/items")
    assert res.status_code == 200


def test_list_items_returns_list(client):
    res = client.get("/items")
    data = res.get_json()
    assert isinstance(data, list)
    assert len(data) == 3


def test_list_items_shape(client):
    res = client.get("/items")
    first = res.get_json()[0]
    assert "id" in first
    assert "name" in first


# /items/<id>


def test_get_existing_item(client):
    res = client.get("/items/1")
    assert res.status_code == 200
    assert res.get_json()["name"] == "Widget"


def test_get_missing_item_returns_404(client):
    res = client.get("/items/999")
    assert res.status_code == 404


def test_get_missing_item_error_payload(client):
    res = client.get("/items/999")
    assert res.get_json() == {"error": "not found"}
