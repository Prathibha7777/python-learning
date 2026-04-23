import requests
def test_response_is_success():
    response = requests.get("https://jsonplaceholder.typicode.com/users/1")
    assert response.status_code == 200

def test_response_has_required_keys():
    response = requests.get("https://jsonplaceholder.typicode.com/users/1")
    data = response.json()
    assert "name" in data
    assert "email" in data
    assert "phone" in data

def test_users_count():
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    data = response.json()
    assert len(data) == 10
