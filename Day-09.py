# response_data = { "status": "active", "name": "router-01"}

# try:
#     print(response_data["cpu"])
# except KeyError as e:
#     print(f"Key not found: {e}")

# try:
#     number = int("not-a-number")
# except ValueError as e:
#     print(f"Value is not found: {e}")

# try:
#     result = 10/0
# except ZeroDivisionError as e:
#     print(f"Math error: {e}")

# print("Program continues after errors")

# with open("test_config.txt", "w") as f:
#     f.write("base_url=https://jsonplaceholder.typicode.com\n")
#     f.write("timeout=30\n")
#     f.write("environment=test\n")

# with open("test_config.txt", "r") as f:
#     content = f.read()
#     print(content)

# with open("test_config.txt", "r") as f:
#     for line in f:
#         print(f"Line: {line.strip()}")

# import json
# import os

# def load_config(filename):
#     if not os.path.exists(filename):
#         print(f" Config file not found: {filename}")
#         return {}
#     try:
#         with open(filename, "r") as f:
#             config = json.load(f)
#             print("Config loaded successfully")
#             return config
#     except json.JSONDecodeError as e:
#         print(f"Invalid JSON in config: {e}")
#         return {}
    
# config1 = load_config("missing.json")
# print(f"config1: {config1}")

# with open("valid_config.json", "w") as f:
#     json.dump({"base_url": "https://jsonplaceholder.typicode.com", "timeout": 30}, f)

# config2 = load_config("valid_config.json")
# print(f"config2: {config2}")


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