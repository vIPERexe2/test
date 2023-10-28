proxy_list = [
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

def connect_to_proxy(proxy):
    # Code to connect to the proxy
    pass

def make_proxy_multi_terminal(proxy_list):
    for proxy in proxy_list:
        try:
            connect_to_proxy(proxy)
            print(f"Connected to proxy: {proxy}")
        except Exception as e:
            print(f"Failed to connect to proxy: {proxy}")
            print(f"Error: {str(e)}")

make_proxy_multi_terminal(proxy_list)
