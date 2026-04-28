def get_active_devices(devices):
    active_names = []
    for device in devices:
        try:
            if device["status"] == "active":
                active_names.append(device["name"])
        except KeyError:
            print(f"device['name'] has no status key - skipping")
    return active_names

devices = [
    {"name": "router-01", "status": "active"},
    {"name": "router-02", "status": "down"},
    {"name": "switch-01"},
    {"name": "switch-02", "status": "active"}
]

result = get_active_devices(devices)
print(result)


