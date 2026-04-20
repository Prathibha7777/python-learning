# devices = ["router-01", "router-02", "switch-01", "switch-02"]

# print(devices)
# print(devices[0])
# print(devices[1])
# print(devices[-1])

# devices = ["router-01", "router-02", "switch-01", "switch-02"]

# #prints devices length, how many items are there
# print(len(devices))

# #adds extra item to length
# devices.append("firewall-01")
# print(devices)

# print("router-01" in devices)
# print("router-99" in devices)

# for device in devices:
#     print(f"checking: {device}")

response_data = {
    "status": "success",
    "devices": ["router-01", "router-02", "switch-01"]
}

devices = response_data["devices"]

assert len(devices) == 3
assert "router-01" in devices
assert devices[0] == "router-01"
assert devices[-1] == "switch-01"

print(f"Total devices: {len(devices)}")
print(f"First device: {devices[0]}")
print(f" router-99 exists: {'router-99' in devices}")
print("All assertion passed")