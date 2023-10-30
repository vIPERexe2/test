import requests

def turn_off_ps5():
    url = "http://<PS5_IP_ADDRESS>/settings/power/standby"
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    data = {
        "status": False,
        "passCode": ""
    }
    response = requests.put(url, headers=headers, json=data)
    
    if response.status_code == 200:
        print("PS5 turned off successfully.")
    else:
        print("Failed to turn off PS5. Please check your network connection and try again.")

turn_off_ps5()
