import random
import string

def generate_password(length=12, use_Digits=True, use_Specials=True, use_Uppercase=True, use_Lowercase=True): # Set default values for the parameters
    # Define the character sets
    digits = string.digits
    specials = string.punctuation
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase

    # Initialize the character set
    charset = ""

    # Error 
    if not use_Digits and not use_Specials and not use_Uppercase and not use_Lowercase:
        raise ValueError("Please select at least one character set")

    # Add the character sets to the charset
    if use_Digits:
        charset += digits

    if use_Specials:
        charset += specials

    if use_Uppercase:
        charset += uppercase

    if use_Lowercase:
        charset += lowercase

    # Generate the password
    password = "".join(random.choice(charset) for i in range(length))
    return password

# Test the function
if __name__ == "__main__":
    length = int(input("Enter the length of the password: "))
    use_Digits = input("Use digits? (y/n): ").lower() == "y"
    use_Specials = input("Use special characters? (y/n): ").lower() == "y"
    use_Uppercase = input("Use uppercase letters? (y/n): ").lower() == "y"
    use_Lowercase = input("Use lowercase letters? (y/n): ").lower() == "y"
    password = generate_password(length, use_Digits, use_Specials, use_Uppercase, use_Lowercase)
    print("Generated password: ", password)

