import secrets
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits
    password_chars = [secrets.choice(characters) for _ in range(length)]
    return ''.join(password_chars)
def password_generator():
    print("=== Random Password Generator ===")

    while True:
        user_input = input("Enter the desired password length: ").strip()
        try:
            length = int(user_input)
            if length <=0:
                print("Length must be a positive number.\n")
                continue
            break
        except ValueError:
            print("Invalid input.Please enter a Whole number.\n")

    password = generate_password(length)
    print(f"\nGenerated Password: {password}")

if __name__ == "__main__":
    password_generator()
