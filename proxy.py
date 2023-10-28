import requests
import stem.process

# Define a list of Tor SOCKS proxy ports and IP addresses
tor_proxies = [
    ('103.176.108.1', 1338),
    ('85.112.193.37', 8080),
    ('58.20.82.103', 2323),
    ('190.113.40.40', 999),
    ("80.249.112.162", 80),
    ('202.40.177.69', 80)
]

# Iterate through the list of Tor proxies and make requests
for ip, port in tor_proxies:
    with stem.process.launch_tor_with_config(
        config={
            'SocksPort': str(port),  # Use the specified Tor SOCKS port
        },
    ) as tor_process:
        session = requests.Session()
        session.proxies = {'http': f'socks5://{ip}:{port}', 'https': f'socks5://{ip}:{port}'}

        response = session.get("https://example.com")
        print(f"Proxy: {ip}:{port}, Status Code: {response.status_code}")
