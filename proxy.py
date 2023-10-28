import requests

proxies = [
    {"address": "138.2.61.140", "port": 88},
    {"address": "123.182.58.221", "port": 8089},
    {"address": "185.189.199.75", "port": 23500},
    {"address": "164.132.170.100", "port": 80},
    {"address": "153.92.214.224", "port": 80},
    {"address": "120.196.207.10", "port": 80},
    {"address": "31.40.27.214", "port": 3128},
    {"address": "153.92.214.224", "port": 80},
    {"address": "177.185.92.193", "port": 3128},
    {"address": "170.81.241.14", "port": 999},
    {"address": "185.189.199.75", "port": 23500},
    {"address": "177.185.92.193", "port": 3128},
    # Add more proxy servers as needed
]

def make_network_request(url):
    for proxy in proxies:
        proxy_address = f"{proxy['address']}:{proxy['port']}"
        try:
            response = requests.get(url, proxies={"http": proxy_address, "https": proxy_address})
            response.raise_for_status()  # Raise an exception if the request was unsuccessful
            return response
        except requests.exceptions.RequestException as e:
            print(f"Failed to make a request using proxy {proxy_address}: {e}")
    raise Exception("Failed to make a successful request using any proxy server.")
