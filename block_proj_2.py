import re
import random
import string

def generate_strong_password(length=30):
    """Generate a random strong password with a mix of uppercase, lowercase, digits, and special characters."""
    characters = (
        string.ascii_uppercase +
        string.ascii_lowercase +
        string.digits +
        string.punctuation
    )
    password = ''.join(random.sample(characters, length))
    return password

def check_password_strength(password):
    """Check if the given password meets strength criteria."""
    min_length = 8

    if len(password) < min_length:
        return "Password must be at least 8 characters long."

    if not re.search(r"[a-z]", password):
        return "Password must contain at least one lowercase letter."

    if not re.search(r"[A-Z]", password):
        return "Password must contain at least one uppercase letter."

    if not re.search(r"\d", password):
        return "Password must contain at least one number."

    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return "Password must contain at least one special character."

    return "Strong: Password meets all the criteria."

def main():
    print("Password Strength Checker")
    choice = input("Do you want to enter a password (E) or receive a randomly generated one (G)? ").strip().lower()

    if choice == "g":
        password = generate_strong_password()
        print(f"Generated strong password: {password}")
        return
    elif choice == "e":
        while True:        
            password = input("Enter your password to check its strength: ")
            result = check_password_strength(password)
            print(result)

            if result == "Strong: Password meets all the criteria.":
                while True:
                    confirm_password = input("Re-enter your password to verify: ")
                    if confirm_password == password:
                        print("Password successfully verified!")
                        return
                    else:
                        print("Passwords do not match. Please try again.")
    else:
        print("Invalid choice. Please enter 'E' to enter a password or 'G' to generate one.")
        return

if __name__ == "__main__":
    main()
