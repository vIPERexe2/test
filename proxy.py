import requests

def connect_to_proxy(proxy):
    proxies = {
        'http': f'http://{proxy}',
        'https': f'http://{proxy}'
    }
    try:
        response = requests.get('https://www.example.com', proxies=proxies)
        if response.status_code == 200:
            print(f"Connected to proxy: {proxy}")
        else:
            print(f"Failed to connect to proxy: {proxy}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to connect to proxy: {proxy}")
        print(f"Error: {str(e)}")

proxies = [
    "138.2.61.140:88",
    "123.182.58.221:8089",
    "185.189.199.75:23500",
    "164.132.170.100:80",
    "153.92.214.224:80",
    "120.196.207.10:80",
    "31.40.27.214:3128",
    "153.92.214.224:80",
    "177.185.92.193:3128",
    "170.81.241.14:999",
    "185.189.199.75:23500",
    "177.185.92.193:3128"
]

for proxy in proxies:
    connect_to_proxy(proxy)
