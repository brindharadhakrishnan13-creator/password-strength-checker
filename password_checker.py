password = input("Enter a password: ")
score = 0
if len(password) >= 8:
    score += 1
if any(c.isupper() for c in password):
    score += 1
if any(c.islower() for c in password):
    score += 1
if any(c.isdigit() for c in password):
    score += 1
special = "!@#$%^&*()-_=+[]{}|;:',.<>?/"
if any(c in special for c in password):
    score += 1
if score <= 2:
    print("Weak Password")
elif score == 3 or score == 4:
    print("Medium Password")
else:
    print("Strong Password")
