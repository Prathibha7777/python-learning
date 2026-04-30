import pytest
import requests

@pytest.mark.parametrize("post_id", [1,2,3])
def test_post_exists(post_id, base_url):
    response = requests.get(f"{base_url}/posts/{post_id}")
    assert response.status_code == 200
    assert "title" in response.json()