def device_list(devices):
    active_count = 0
    for device in devices:
        status = device.get("status")
        if status == "active":
            print(f"{device['hostname']}")
            active_count += 1
        elif status == "inactive":
            pass
        else:
            print("unknown devices")
    print(f"Active devices: {active_count}")
    return active_count

devices = [
    {"hostname": "R1", "status": "active"},
    {"hostname": "R2", "status": "inactive"},
    {"hostname": "R3"},
    {"hostname": "R4", "status": "active"},
]
device_list(devices)