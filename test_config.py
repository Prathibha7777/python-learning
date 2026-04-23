import json
import os
import requests

def test_config_file_exists():
    assert os.path.exists("valid_config.json") == True

def test_config_has_base_url():
    with open("valid_config.json", "r") as f:
        config = json.load(f)
    assert "base_url" in config

def test_api_with_config():
    with open("valid_config.json", "r") as f:
        config = json.load(f)
    response = requests.get(f"{config['base_url']}/users/1")
    assert response.status_code == 200