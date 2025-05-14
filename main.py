` tags.

```
<replit_final_file>
def read_users():
    try:
        file = open('users.txt', 'r')
        users = {}
        for line in file:
            username, password = line.strip().split(':')
            users[username] = password
        file.close()
        return users
    except:
        return {'YKang': '2010', 'student': '1234'}

def save_users(users):
    file = open('users.txt', 'w')
    for username in users:
        file.write(f'{username}:{users[username]}\n')
    file.close()

def show_admin_menu(users, username):
    while True:
        print("\nADMIN MENU")
        print("1. View all users")
        print("2. Add new user")
        print("3. Remove user")
        print("4. Change your password")
        print("5. Log out")

        choice = input("\nType 1, 2, 3, 4 or 5: ")

        if choice == '1':
            print("\nAll Users:")
            print("====================")
            for user in users:
                print(f"Username: {user}")
            print("====================")

        elif choice == '2':
            new_username = input("Enter new username: ")
            new_password = input("Enter new password: ")
            users[new_username] = new_password
            save_users(users)
            print("New user has been added!")

        elif choice == '3':
            remove_username = input("Enter username to remove: ")
            if remove_username == 'admin':
                print("Cannot remove admin account!")
            elif remove_username in users:
                del users[remove_username]
                save_users(users)
                print(f"User {remove_username} has been removed!")
            else:
                print("User not found!")

        elif choice == '4':
            new_password = input("Enter your new password: ")
            users[username] = new_password
            save_users(users)
            print("Your password has been changed!")

        elif choice == '5':
            print("Logging out of admin account!")
            break

        else:
            print("Please choose a valid option!")

def show_user_menu(users, username):
    while True:
        print("\nUSER MENU")
        print("1. Change your password")
        print("2. Log out")

        choice = input("\nType 1 or 2: ")

        if choice == '1':
            new_password = input("Enter your new password: ")
            users[username] = new_password
            save_users(users)
            print("Your password has been changed!")

        elif choice == '2':
            print("Thank you for using the system!")
            break

        else:
            print("Please choose 1 or 2!")

print("Welcome to the School Login System!")
users = read_users()

while True:
    print("\n====================")
    print("LOGIN SCREEN")
    print("====================")

    username = input("Username: ")
    password = input("Password: ")

    if username in users and users[username] == password:
        print(f"\nWelcome back {username}!")

        if username == 'admin' or username == 'YKang':
            show_admin_menu(users, username)
        else:
            show_user_menu(users, username)

    else:
        print("Sorry, wrong username or password!")

    again = input("\nWould you like to try again? (yes/no): ")
    if again.lower() != 'yes':
        print("Goodbye!")
        break