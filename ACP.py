#Write a python program to generate a random password consisting of lower case and upper case characters along with numbers. You can also use random module for shuffling the password generated.

import random

def generate_password(length=8): 
    # Define character sets
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789"
    
    # Make sure we include at least one of each type
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits)
    ]
    
    # Combine all characters together
    all_chars = lower + upper + digits
    
    # Fill the rest of the password
    for _ in range(length - 3):
        password.append(random.choice(all_chars))
    
    # Shuffle so it's not predictable
    random.shuffle(password)
    
    # Convert list to string
    return "".join(password)

# Example usage
print("Generated Password:", generate_password())