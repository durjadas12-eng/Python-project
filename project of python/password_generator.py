#this is a password generator
import random
import string

def generate_password():
        length = int(input("Enter the length of the password: "))
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        return password
while True:
    print("Welcome to the password generator!!")
    password = generate_password()
    print(f"generated password: {password}")
    again = input("Do you want to generate another password? (yes/no):")
    if again.lower() != "yes":
          print("exiting the password generator. Good bye!")
          break