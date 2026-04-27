def safe_get_value(dictionary, key):
    try:
        return dictionary[key]
    except KeyError:
        return "Key not found"
    
data = {"name": "Ravi", "role": "qa"}
print(safe_get_value(data, "name"))
print(safe_get_value(data, "salary"))