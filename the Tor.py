import subprocess

def disable_remote_turn_off():
    # Disable remote turn off by password for PS5/PS4 in LAN
    command = "sudo sysctl -w net.inet.tcp.blackhole=2"
    subprocess.call(command, shell=True)

disable_remote_turn_off()
