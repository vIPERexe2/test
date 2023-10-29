def find_gmails(name, last_name, num_gmails):
    gmails = []
    for i in range(1, num_gmails+1):
        gmail = f"{name.lower()}.{last_name.lower()}{i}@gmail.com"
        gmails.append(gmail)
    return gmails

name = input("Enter the name: ")
last_name = input("Enter the last name: ")
num_gmails = int(input("Enter the number of Gmail addresses to generate: "))

found_gmails = find_gmails(name, last_name, num_gmails)
print("Gmail addresses found:")
for gmail in found_gmails:
    print(gmail)
