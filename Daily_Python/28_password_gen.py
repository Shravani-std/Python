import random
import string
print(" === Passwprd Generator ===")
print("Create super strong and seacure password with ease!")

length = int(input("Enter password length (8 - 30): "))

print("Let's customize your password! ")

while True:
    length = int(input("Enter password length (8-30): "))
    if length < 8 or length > 30:
        print("Please choose a lenght betwoon 8 - 30")
        continue
    use_lower = input("Include lowercase letters (a-z)? (y/n): ").lower().startswith('y')
    use_upper = input("Include uppercase letters (A-Z)? (y/n): ").lower().startswith('y')
    use_digits = input("Include numbers (0-9)? (y/n): ").lower().startswith('y')
    use_special = input("Include special characters (!@#$%^&*())? (y/n): ").lower().startswith('y')
    
    char = []

    if use_lower:
        char += list(string.ascii_lowercase)
    if use_upper:
        char += list(string.ascii_uppercase)
    if use_digits:
        char += list(string.digits)
    if use_special:
        char += list("~!@#$%^&*()_+")

    if not char:
        print("You must select at least one character type!")
        continue
    
    print("Generating password...")


    password = []
    if use_lower:
        password.append(random.choice(string.ascii_lowercase))
    if use_upper:
        password.append(random.choice(string.ascii_uppercase))
    if use_digits:
        password.append(random.choice(string.digits))
    if use_special:
        password.append(random.choice("!@#$%^&*()"))

    while len(password) < length:
        password.append(random.choice(char))

    random.shuffle(password)

    final_password = ''.join(password)
    print("=== Your New Password ===")
    print(final_password)
    new = input(print("Would you like to create another awesome password? "))
    if not new.startswith('y'):
        print("Thank you for using the super fun pass gen...")
        break




    
    
    