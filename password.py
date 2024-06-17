import random
import string

def generate_password(length):
    # Define character sets
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation
    
    # Combine all character sets
    all_chars = lower + upper + digits + special
    
    # Ensure the password has at least one character from each set
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(special)
    ]
    
    # Generate the remaining characters randomly from all sets
    password += random.choices(all_chars, k=length-4)
    
    # Shuffle the generated password list to avoid any predictable pattern
    random.shuffle(password)
    
    # Join the list to form the final password string
    return ''.join(password)

def main():
    # Prompt user for the desired password length
    while True:
        try:
            length = int(input("Enter the desired length of the password (minimum 4): "))
            if length < 4:
                print("Please enter a length of at least 4.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
    
    # Generate the password
    password = generate_password(length)
    
    # Display the generated password
    print(f"Generated Password: {password}")

# Run the main function
if __name__ == "__main__":
    main()
