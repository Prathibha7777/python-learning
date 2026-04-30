def validate_api_response(response, required_keys):
    missing_count = 0
    for key in required_keys:
        if key in response:
            print(f"{key} found")
        else:
            print(f"{key} not found")
            missing_count += 1
    return missing_count

response = {"id": 1, "name": "Ravi", "email": "ravi@test.com"}
result = validate_api_response(response, ["id", "name", "email", "phone", "address"])
print(f"Missing keys: {result}")