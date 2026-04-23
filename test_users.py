import requests

def test_get_user_status():
    response = requests.get("https://jsonplaceholder.typicode.com/users/1")
    assert response.status_code == 200

def test_user_has_name():
    response = requests.get("https://jsonplaceholder.typicode.com/users/1")
    data = response.json()
    assert "name" in data

def test_user_id_is_correct():
    response = requests.get("https://jsonplaceholder.typicode.com/users/1")
    data = response.json()
    assert data["id"] == 1

def test_email_exists():
    response = requests.get("https://jsonplaceholder.typicode.com/users/1")
    data = response.json()
    assert "email" in data
def test_address_exists():
    response = requests.get("https://jsonplaceholder.typicode.com/users/1")
    data = response.json()
    assert "address" in data
def test_city_not_empty():
    response = requests.get("https://jsonplaceholder.typicode.com/users/1")
    data = response.json()
    assert data["address"]["city"] != ""

def test_all_users_returns_list():
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
def test_first_user_has_email():
    resonse = requests.get("https://jsonplaceholder.typicode.com/users")
    data = resonse.json()
    assert "email" in data[0]