devices = ["router-01", "switch-01", "router-02", "switch-02"]

def check_device(devices):
    for device in devices:
        if device.startswith("router"):
            print(f"router found: {device}")
        else:
            print(f"other device: {device}")
check_device(devices)