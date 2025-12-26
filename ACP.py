def is_strong_password(password):
    special_characters = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~"

    if len(password) < 8:
        return "Password must be at least 8 characters long."

    has_lower = False
    has_upper = False
    has_digit = False
    has_special = False

    for char in password:
        if char.islower():
            has_lower = True
        elif char.isupper():
            has_upper = True
        elif char.isdigit():
            has_digit = True
        elif char in special_characters:
            has_special = True

    if not has_lower:
        return "Password must contain a lowercase letter."
    if not has_upper:
        return "Password must contain an uppercase letter."
    if not has_digit:
        return "Password must contain a number."
    if not has_special:
        return "Password must contain a special character."

    return "Password is strong!"


while True:
    password = input("\nEnter a password: ")
    result = is_strong_password(password)
    print(result)

    if result == "Password is strong!":
        break
    print("Please try again.\n")