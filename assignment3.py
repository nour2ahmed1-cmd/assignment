#define the correct username, password, and user role

correct_username =  "nour" # this can be any string, but I will use "nour" as the correct username
correct_password = 123 # this can be any number, but I will use 123 as the correct password
user_role = "admin"  # This can be "admin", "moderator", or "user"

username = input("Enter your username: ")
password = float(input("Enter your password: "))
role = input("Enter your role (admin/moderator/user): ").strip().lower()

if username == correct_username:
    if password == correct_password:
        if role == "admin":
            print("Welcome, admin!")
        elif role == "moderator":
            print("Welcome, moderator!")
        elif role == "user":
            print("Welcome, user!")
        else:
            print("Unknown role.")
    else:
        print("Wrong password.")
else:    print("Wrong username.")
