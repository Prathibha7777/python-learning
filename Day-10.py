# import pytest
# import requests

# @pytest.fixture
# def user():
#     response = requests.get("https://jsonplaceholder.typicode.com/users/1")
#     return response.json()

# def test_user_has_id(user):
#     assert user["id"] == 1

# def test_user_has_name(user):
#     assert "name" in user

# def test_user_name_is_correct(user):
#     assert user["name"] == "Leanne Graham"

# def test_user_has_address(user):
#     assert "address" in user

# def test_user_city(user):
#     assert user["address"]["city"] == "Gwenborough"

# @pytest.fixture
# def user_with_cleanup():
#     print("\nSETUP : Fetching user data")
#     response = requests.get("https://jsonplaceholder.typicode.com/users/2")
#     data = response.json()
#     yield data
#     print("\nTEAR DOWN: Test finished, cleaning up")

# def test_user2_name(user_with_cleanup):
#     assert user_with_cleanup["name"] == "Ervin Howell"

# def test_user2_email(user_with_cleanup):
#     assert "email" in user_with_cleanup

# @pytest.fixture(scope="module")
# def user_module_scope():
#     print("\nMODULE SETUP: runs once per entire file")
#     response = requests.get("https://jsonplaceholder.typicode.com/users/3")
#     data = response.json()
#     yield data
#     print("\nMODULE TEARDOWN: runs once after all tests done")

# def test_user3_id(user_module_scope):
#     assert user_module_scope["id"] == 3

# def test_user3_name(user_module_scope):
#     assert "name" in user_module_scope

# def test_user3_email(user_module_scope):
#     assert "email" in user_module_scope

# @pytest.fixture(scope="session")
# def base_url():
#     return "https://jsonplaceholder.typicode.com"

# @pytest.fixture(scope="session")
# def user4(base_url):
#     response = requests.get(f"{base_url}/users/4")
#     return response.json()

# def test_user4_id(user4):
#     assert user4["id"] == 4

# def test_user4_website(user4):
#     assert "website" in user4

# def test_base_url_is_correct(base_url):
#     assert "jsonplaceholder" in base_url

import pytest
import requests

@pytest.fixture()
def post_data():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    return response.json()

@pytest.fixture()
def all_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    return response.json()

def test_post_has_title(post_data):
    assert "title" in post_data

def test_post_user_id(post_data):
    assert post_data["userId"] == 1

def test_total_posts(all_posts):
    assert len(all_posts) == 100

def test_first_post_has_body(all_posts):
    assert "body" in all_posts[0]