import sys

def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py <username> <password_list>")
        return

    username = sys.argv[1]
    password_list = sys.argv[2]

    brute_force_gmail(username, password_list)

if __name__ == "__main__":
    main()
