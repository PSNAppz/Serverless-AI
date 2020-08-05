from starlette.testclient import TestClient
from app.main import app
from app.core.config import API_V1_STR
import json

client = TestClient(app)

def is_json(myjson):
    try:
        json_object = json.loads(myjson)
    except ValueError as e:
        return False
    return True

def test_example_endpoint_availability():
    response = client.get(API_V1_STR + "/")
    assert response.status_code == 200

def test_example_route_valid_json():
    response = client.get(API_V1_STR + "/")
    assert is_json(response.content)

