# import pytest

# @pytest.mark.parametrize("user_id", [1,2,-3,4,5])
# def test_user_id_is_valid(user_id):
#     assert user_id > 0

# import pytest
# import requests

# @pytest.mark.parametrize("user_id", [1,2,3,4,5])
# def test_user_exists(user_id):
#     response = requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}")
#     assert response.status_code == 200

import pytest
import requests

@pytest.mark.parametrize("user_id, expected_name", [(1, "Leanne Graham"),
    (2, "Ervin Howell"),
    (3, "Clementine Bauch")
])
def test_user_name(user_id, expected_name):
    response = requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}")
    data = response.json()
    assert data["name"] == expected_name
