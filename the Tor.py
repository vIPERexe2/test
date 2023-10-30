import requests
import subprocess

def generate_tor_proxies():
    try:
        # Fetch list of Tor proxies
        response = requests.get('https://api.proxyscrape.com/?request=getproxies&proxytype=socks5&timeout=10000&country=all')
        proxies = response.text.split('\r\n')

        # Set up Tor proxies
        for proxy in proxies:
            try:
                subprocess.run(['torify', 'curl', '--socks5', proxy, 'https://api.ipify.org'], check=True)
                print(f"Successfully set up Tor proxy: {proxy}")
            except subprocess.CalledProcessError:
                print(f"Failed to set up Tor proxy: {proxy}")
    
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching Tor proxies: {e}")

generate_tor_proxies()
