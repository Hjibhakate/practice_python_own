password = input("Enter your password : ")

has_number = False 

has_uppercase = False 

has_special = False 

special_chars = "!@#$%^&*&()"

for char in  password:

    if char.isdigit():
        has_number = True 
    if char.isupper():
        has_uppercase = True 
    if char in special_chars:
        has_special = True

if len(password) < 8:
    print("Weak Password")
elif has_number and has_uppercase and has_special:
    print("Strong Password ")
else:
    print("Medium Password ")