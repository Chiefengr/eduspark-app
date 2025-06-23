import sys
import os
import pytest

# ✅ Dynamically add the parent directory to sys.path (where `app/` lives)
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))

try:
    from app.main_flask import app
except ModuleNotFoundError as e:
    raise RuntimeError()


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_home_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"EduSpark" in response.data
