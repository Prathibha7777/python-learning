devices = [
    {"name": "router-01", "status": "active"},
    {"name": "router-02", "status": "down"},
    {"name": "switch-01", "status": "active"},
    {"name": "switch-02", "status": "rebooting"}
]

def filter_active_devices(devices):
    active = []
    for device in devices:
        if device["status"] == "active":
            active.append(device)
    return active
    
result = filter_active_devices(devices)
print(result)
        
