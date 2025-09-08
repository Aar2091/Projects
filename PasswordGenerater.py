import random
import string

def generate_password():
    length = int(input("Enter password length (8-25): "))
    if length < 8 or length > 25:
        print("Password length must be between 8 and 25.")
        return
    characters = string.ascii_lowercase + string.ascii_uppercase + string.digits
    password = "".join(random.choice(characters) for _ in range(length))
    print("Your random password is:", password)

generate_password()

#Used help by ChatGPT
