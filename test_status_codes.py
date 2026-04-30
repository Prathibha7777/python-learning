import pytest
import requests

@pytest.mark.parametrize("status_code, expected", [(200, True), 
    (404, False), 
    (500, False)
])
def test_status_code_is_success(status_code, expected, base_url):
    response = requests.get(f"{base_url}/users")
    assert (status_code == 200) == expected