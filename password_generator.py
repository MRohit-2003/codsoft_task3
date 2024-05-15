import random
import string

def generate_password(length, uppercase, digits, special_chars):
    characters = string.ascii_lowercase
    if uppercase:
        characters += string.ascii_uppercase
    if digits:
        characters += string.digits
    if special_chars:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to my Password Generator!")

    length = int(input("Enter the length of the password: "))
    uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
    digits = input("Include digits? (yes/no): ").lower() == 'yes'
    special_chars = input("Include special characters? (yes/no): ").lower() == 'yes'

    password = generate_password(length, uppercase, digits, special_chars)
    print("Generated Password:", password)

if __name__ == "__main__":
    main()
