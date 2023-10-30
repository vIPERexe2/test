import subprocess

def create_tor_proxy():
    try:
        # Start Tor service
        subprocess.run(['tor'])

        # Get Tor proxy information
        output = subprocess.check_output(['tor', '--socks5-hostname', '--quiet'])

        # Extract proxy IP and port from output
        proxy_info = output.decode().strip().split(':')
        proxy_ip = proxy_info[0]
        proxy_port = int(proxy_info[1])

        # Print proxy information
        print(f'Tor proxy created successfully:')
        print(f'IP: {proxy_ip}')
        print(f'Port: {proxy_port}')

    except subprocess.CalledProcessError:
        print('Error creating Tor proxy.')

if __name__ == '__main__':
    create_tor_proxy()
