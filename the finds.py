import re

def find_gmails_by_name(name, last_name):
    # Validate name and last name inputs
    if not name or not last_name:
        raise ValueError("Name and last name cannot be empty.")

    # Construct the Gmail address pattern
    pattern = r"{}\.{}@gmail\.com".format(name.lower(), last_name.lower())

    # Search for Gmail addresses
    gmails = []
    # You can replace this with your own list of Gmail addresses or use an API to search for Gmail addresses
    gmail_list = ["john.doe@gmail.com", "jane.doe@gmail.com", "james.smith@gmail.com"]

    for gmail in gmail_list:
        if re.match(pattern, gmail, re.IGNORECASE):
            gmails.append(gmail)

    return gmails

# Test the function
try:
    name = input("Enter the name: ")
    last_name = input("Enter the last name: ")
    found_gmails = find_gmails_by_name(name, last_name)
    if found_gmails:
        print("Found Gmail addresses:")
        for gmail in found_gmails:
            print(gmail)
    else:
        print("No Gmail addresses found.")
except ValueError as e:
    print("Error:", str(e))
except Exception as e:
    print("An error occurred:", str(e))
