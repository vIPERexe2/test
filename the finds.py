import re

def find_gmails(name, lastname):
    email_regex = re.compile(r'[a-zA-Z0-9._%+-]+@gmail.com')
    test_emails = ['test1@gmail.com', 'test2@gmail.com', 'test3@gmail.com']
    full_name = name.lower() + '.' + lastname.lower()
    possible_emails = [full_name + '@gmail.com', full_name + '1@gmail.com', full_name + '2@gmail.com']
    valid_emails = []
    for email in possible_emails:
        if email_regex.match(email):
            valid_emails.append(email)
    print('Valid Gmails:')
    for email in valid_emails:
        print(email)
    print('Test Gmails:')
    for email in test_emails:
        print(email)
