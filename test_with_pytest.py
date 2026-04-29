import pytest
import requests

@pytest.fixture
def post_data(base_url):
    response =requests.get(f"{base_url}/post/1")
    return response.json()

def test_post_has_title(post_data):
   assert "title" in post_data

def test_post_user_id(post_data):
   assert post_data["userId"] == 1

def test_post_has_body(post_data):
    assert "body" in post_data