device = {
    "hostname": "router-01",
    "ip": "192.168.1.1",
    "status": "active",
    "port_count": 24
}
# for key in device:
#     print(key)
#     for key in device:
# for key in device:
#     print(key, device[key])



for key, value in device.items():
    print(f"{key} -> {value}")