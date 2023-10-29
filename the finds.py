def find_gmails(name, last_name):
    gmails = []
    # Assuming the list of Gmail addresses is stored in a variable called 'emails'
    for email in emails:
        # Splitting the email address into name and domain parts
        parts = email.split('@')
        if len(parts) == 2:
            # Extracting the name part
            email_name = parts[0]
            # Splitting the name into first name and last name
            name_parts = email_name.split('.')
            if len(name_parts) == 2:
                # Extracting the first name and last name
                first_name = name_parts[0]
                last_name = name_parts[1]
                # Checking if the given name and last name match
                if first_name.lower() == name.lower() and last_name.lower() == last_name.lower():
                    gmails.append(email)
    return gmails

# Example usage
name = input("Enter the name: ")
last_name = input("Enter the last name: ")
found_gmails = find_gmails(name, last_name)
if found_gmails:
    print("Gmail addresses found:")
    for gmail in found_gmails:
        print(gmail)
else:
    print("No Gmail addresses found.")
