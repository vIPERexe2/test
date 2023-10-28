import requests

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
    # Add more proxy servers as needed
]

def write_callback(response, contents):
    response += contents
    return len(contents)

def make_network_request(url):
    for proxy in proxies:
        proxy_host, proxy_port = proxy.split(':')
        proxies = {
            'http': f'http://{proxy_host}:{proxy_port}',
            'https': f'http://{proxy_host}:{proxy_port}'
        }
        try:
            response = requests.get(url, proxies=proxies)
            if response.status_code == 200:
                return response.text
        except requests.exceptions.RequestException:
            pass
    raise Exception("Failed to make a successful request using any proxy server.")
