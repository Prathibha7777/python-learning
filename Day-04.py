
# def greet():
#     print("Hello I am function")

# greet()

# def greet():
#     print("Hello")

# greet()
# greet()
# greet()

# def check_status():
#     status_code = 200
#     print(f"status code is : {status_code}")
#     print(f"Test passed: {status_code == 200}")

# check_status()

# def check_status(code):
#     print(f"status: {code}")
#     print(f"Is Success: {code == 200}")

# check_status(200)
# check_status(404)
# check_status(201)

# def check_device(hostname, status):
#     print(f"Device: {hostname}")
#     print(f"Status: {status}")
#     print(f"Is active: {status == 'active'}")

# check_device("router-01", "active")
# check_device("router-02", "down")
# check_device("switch-01", "active")

def is_success(status_code):
    return status_code == 200

print(is_success(200))
print(is_success(404))

assert is_success(200) == True
print("Assertion passed")