device = {
    "hostname": "Router-011",
    "ip": "192.168.1.1",
    "status": "active",
    "port_count": 24

}
print(device["hostname"])
print(device["ip"])
print(device["status"])
print(device["port_count"])

#it will give the status but location doesn't exist
print(device.get("status"))
print(device.get("location"))
print(device.get("location", "unknown"))


api_response = {
    "status_code": 200,
    "data": {
        "device_id": "router-01",
        "health": {
            "cpu": 45,
            "memory": 78,
            "uptime": "5 days"
        }

    }
}

print(api_response["status_code"])
print(api_response["data"]["device_id"])
print(api_response["data"]["health"]["cpu"])
print(api_response["data"]["health"]["uptime"])

assert api_response["status_code"] == 200
assert api_response["data"]["health"]["cpu"] < 90
print("All assertions passed")
