from auth import AuthSystem

auth = AuthSystem("users.txt")

while True:

    print("\n======= LOGIN SYSTEM ======")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        username = input("Enter username: ").lower()
        password = input("Enter password: ")

        auth.register(username,password)
    elif choice == "2":
        username = input("Enter username: ").lower()
        password = input("Enter password: ")

        auth.login(username,password)
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid option")