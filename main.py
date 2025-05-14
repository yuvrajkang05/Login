
# School Login System
# This system manages user authentication and provides different menus for admins and regular users

def read_users():
    """Read user credentials from file or return default users if file doesn't exist"""
    try:
        file = open('users.txt', 'r')
        users = {}
        for line in file:
            username, password = line.strip().split(':')
            users[username] = password
        file.close()
        return users
    except:
        # Return default users if file not found
        return {'YKang': '2010', 'student': '1234'}

def save_users(users):
    """Save current user credentials to file"""
    file = open('users.txt', 'w')
    for username in users:
        file.write(f'{username}:{users[username]}\n')
    file.close()

def show_admin_menu(users, username):
    """Display admin menu with user management options"""
    while True:
        print("\nADMIN MENU")
        print("1. View all users")
        print("2. Add new user")
        print("3. Remove user")
        print("4. Change your password")
        print("5. Log out")

        choice = input("\nType 1, 2, 3, 4 or 5: ")

        if choice == '1':
            # Display all registered users
            print("\nAll Users:")
            print("====================")
            for user in users:
                print(f"Username: {user}")
            print("====================")

        elif choice == '2':
            # Add a new user to the system
            new_username = input("Enter new username: ")
            new_password = input("Enter new password: ")
            users[new_username] = new_password
            save_users(users)
            print("New user has been added!")

        elif choice == '3':
            # Remove a user from the system
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
            # Change admin password
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
    """Display regular user menu with limited options"""
    while True:
        print("\nUSER MENU")
        print("1. Change your password")
        print("2. Log out")

        choice = input("\nType 1 or 2: ")

        if choice == '1':
            # Change user password
            new_password = input("Enter your new password: ")
            users[username] = new_password
            save_users(users)
            print("Your password has been changed!")

        elif choice == '2':
            print("Thank you for using the system!")
            break

        else:
            print("Please choose 1 or 2!")

# Main program starts here
print("Welcome to the School Login System!")
users = read_users()

while True:
    print("\n====================")
    print("LOGIN SCREEN")
    print("====================")

    # Get login credentials
    username = input("Username: ")
    password = input("Password: ")

    # Verify login and show appropriate menu
    if username in users and users[username] == password:
        print(f"\nWelcome back {username}!")

        # Check if user has admin privileges
        if username == 'admin' or username == 'YKang':
            show_admin_menu(users, username)
        else:
            show_user_menu(users, username)

    else:
        print("Sorry, wrong username or password!")

    # Ask if user wants to try logging in again
    again = input("\nWould you like to try again? (yes/no): ")
    if again.lower() != 'yes':
        print("Goodbye!")
        break
