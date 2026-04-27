import pytest
import requests

@pytest.fixture(scope="module")
def user_data():
    response = requests.get("https://jsonplaceholder.typicode.com/users/1")
    return response.json()

@pytest.fixture(scope="module")
def all_users():
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    return response.json()

def test_user_id(user_data):
    assert user_data["id"] == 1

def test_user_has_email(user_data):
    assert "email" in user_data

def test_user_name(user_data):
    assert user_data["name"] == "Leanne Graham"

def test_total_users(all_users):
    assert len(all_users) == 10

def test_first_user_has_email(all_users):
    assert "email" in all_users[0]