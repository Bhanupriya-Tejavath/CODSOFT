import random
import string

print("=" * 45)
print("      CodSoft Secure Password Generator")
print("=" * 45)

try:
    length = int(input("Enter desired password length: "))

    if length < 4:
        print("Password length should be at least 4 characters.")
    else:
        lowercase = random.choice(string.ascii_lowercase)
        uppercase = random.choice(string.ascii_uppercase)
        digit = random.choice(string.digits)
        special = random.choice("!@#$%^&*()_+-=[]{}")

        remaining = length - 4
        all_characters = (
            string.ascii_letters +
            string.digits +
            "!@#$%^&*()_+-=[]{}"
        )

        password_list = [lowercase, uppercase, digit, special]

        for _ in range(remaining):
            password_list.append(random.choice(all_characters))

        random.shuffle(password_list)
        password = "".join(password_list)

        print("\nGenerated Password:")
        print(password)

except ValueError:
    print("Please enter a valid number.")
                
