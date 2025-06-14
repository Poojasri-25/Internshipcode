import random
import string
import pyperclip  

def generate_password(length, use_upper, use_lower, use_digits, use_special):
    characters = ''
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if not characters:
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


try:
    print("🔐 Welcome to the Password Generator\n")

    length = int(input("Enter desired password length: "))

    print("\nInclude the following character types:")
    use_upper = input("Include UPPERCASE letters? (y/n): ").lower() == 'y'
    use_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include numbers? (y/n): ").lower() == 'y'
    use_special = input("Include special characters? (y/n): ").lower() == 'y'

    password = generate_password(length, use_upper, use_lower, use_digits, use_special)

    if password:
        print(f"\n✅ Your generated password is: {password}")
        
        copy = input("Do you want to copy it to clipboard? (y/n): ").lower()
        if copy == 'y':
            pyperclip.copy(password)
            print("📋 Password copied to clipboard!")
    else:
        print("\n❌ Error: Please select at least one character type.")

except ValueError:
    print("⚠️ Please enter a valid number for length.") 