import random
import string
while True:
    try:
        length = int(input("Enter the length of the password ( min 7 ) 🔒:"))
        if length < 7:
            print("🔴 The password should be at least 7 characters 🔴")
        else:
            break
    except ValueError:
        print("Please Enter a valid number")

upper = random.choice(string.ascii_uppercase)
lower = random.choice(string.ascii_lowercase)
digit = random.choice(string.digits)
special = random.choice(string.punctuation)

remaining = length - 4
all_chars = string.ascii_letters + string.digits + string.punctuation
password = upper + lower + digit + special 
for i in range (remaining):
    password += random.choice(all_chars)
password_list = list(password)
random.shuffle(password_list)
print("Strong password:", "".join(password_list))

