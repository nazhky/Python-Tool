import requests

def lookup_ip(ip_address):
    response = requests.get(f"http://ip-api.com/json/{ip_address}", timeout=5)
    data = response.json()
    if data["status"] == "success":
        return data
    return None