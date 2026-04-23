status_codes = [200, 404, 500, 201, 403]
def check_status_codes(codes):
    for code in codes:
        if code == 200 or code == 201:
            print(f"Pass: {code}")
        elif code == 404:
            print(f"Not found: {code}")
        else:
            print(f"Fail: {code}")
check_status_codes(status_codes)