import random
import string


def generate_password(length):
    if length < 1:
        return "Password length should be at least 1"
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")

    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            password = generate_password(length)
            print(f"Generated Password: {password}")
        except ValueError:
            print("Invalid input. Please enter a numeric value for the length.")
        
        another_password = input("Do you want to generate another password? (yes/no): ")
        if another_password.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
