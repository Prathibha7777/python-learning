# import json
# device = {"hostname": "router-01", "status": "active"}
# json_string = json.dumps(device)
# print(json_string)
# #prints device as dictionary
# print(type(json_string))

# back_to_dict = json.loads(json_string)
# print(back_to_dict)
# print(type(back_to_dict))

import os

# current_dir = os.getcwd()
# print(f"current_directory: {current_dir}")

# file_exists = os.path.exists("test_users.py")
# print(f"test_users exists: {file_exists}")

# file_exists2 = os.path.exists("fake_file.py")
# print(f"fake_file exists: {file_exists2}")

# import requests
# import json

# def get_user_data(user_id):
#     response = requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}")
#     return response.json()

# def check_user(user_id, expected_name):
#     data = get_user_data(user_id)
#     if data["name"] == expected_name:
#         print(f" Pass - user {user_id} name is correct: {data["name"]}")
#     else:
#         print(f"Fail - expected {expected_name} but got {data["name"]}")

# check_user(1, "Leanne Graham")
# check_user(2, "Ervin Howell")
# check_user(3, "Wrong name")

# import requests
# import json
# import os

# def load_config():
#     if os.path.exists("config.json"):
#         with open("config.json") as f:
#             return json.load(f)
#     else:
#         return {"base_url": "https://jsonplaceholder.typicode.com"}
    
# def get_devices(config):
#     url = f"{config['base_url']}/users"
#     response = requests.get(url)
#     return response.json()
# config = load_config()
# devices = get_devices(config)

# print(f"config loaded: {config}")
# print(f"Total devices found: {len(devices)}")
# print(f"First device name: {devices[0]['name']}")

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
    response = requests.get("https://jsonplaceholder.typicode.com/users/1")
    data = response.json()
    assert len(data) == 10

