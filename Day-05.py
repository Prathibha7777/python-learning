# It will print test passed

status_code = "200"

if status_code == 200:
    print("Testcase passed")
else:
    print("Testcase failed")

# status_code = 404

# if status_code == 200:
#     print("Success")
# elif status_code == 404:
#     print("Not found")
# elif status_code == 500:
#     print("Server error")
# else:
#     print("Unknown status")
#first and third will pass
# def check_response(status_code, expected_code):
#     if status_code == expected_code:
#         print(f"Pass - got {status_code} as expected")
#     else:
#         print(f"Expected {expected_code} but got {status_code}")

# check_response(200, 200)
# check_response(404, 200)
# check_response(201, 201)
# check_response(500, 200)


# def check_device_status(device_name, actual_status, expected_status):
#     if actual_status == expected_status:
#         print(f" {device_name} is {actual_status}")
#     else:
#         print(f"{device_name} expected {expected_status} but got {actual_status}")

# check_device_status("router-01", "active", "active")
# check_device_status("router-02", "down", "active")
# check_device_status("switch-01", "active", "active")
# check_device_status("switch-02", "rebooting", "active")