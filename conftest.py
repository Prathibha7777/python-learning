import pytest
import requests

@pytest.fixture(scope="session")
def base_url():
    return "https://jsonplaceholder.typicode.com"

@pytest.fixture(scope="session")
def user_data(base_url):
    response = requests.get(f"{base_url}/users/1")
    return response.json()

@pytest.fixture(scope="session")
def all_users(base_url):
    response = requests.get(f"{base_url}/users")
    return response.json()

@pytest.fixture(scope="session")
def single_post(base_url):
    response =requests.get(f"{base_url}/posts/1")
    return response.json()