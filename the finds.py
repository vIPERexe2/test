import re

def find_gmails(name, lastname):
    email_regex = re.compile(r'[a-zA-Z0-9._%+-]+@gmail.com')
    emails = []
    for i in range(10):
        email = name.lower() + '.' + lastname.lower() + str(i) + '@gmail.com'
        if email_regex.match(email):
            emails.append(email)
    return emails

name = input("Enter name: ")
lastname = input("Enter lastname: ")
gmails = find_gmails(name, lastname)
print("Gmails found:")
for gmail in gmails:
    print(gmail)
