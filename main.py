
# Simple Login System for Year 10
# This program lets users log in and manage their passwords

# Store users and passwords in a simple text file
def read_users():
    try:
        file = open('users.txt', 'r')
        users = {}
        for line in file:
            # Split each line into username and password
            username, password = line.strip().split(':')
            users[username] = password
        file.close()
        return users
    except:
        # If no file exists, create a default user
        return {'student': '1234'}

# Save all users to the file
def save_users(users):
    file = open('users.txt', 'w')
    for username in users:
        file.write(f'{username}:{users[username]}\n')
    file.close()

# Main program starts here
print("Welcome to the School Login System!")
users = read_users()

while True:
    # Show login screen
    print("\n====================")
    print("LOGIN SCREEN")
    print("====================")
    
    # Get username and password
    username = input("Username: ")
    password = input("Password: ")
    
    # Check if login is correct
    if username in users and users[username] == password:
        print(f"\nWelcome back {username}!")
        
        # Show menu
        while True:
            print("\nWhat would you like to do?")
            print("1. Add a new user")
            print("2. Change your password")
            print("3. Log out")
            
            choice = input("\nType 1, 2 or 3: ")
            
            if choice == '1':
                # Add new user
                new_username = input("Enter new username: ")
                new_password = input("Enter new password: ")
                users[new_username] = new_password
                save_users(users)
                print("New user has been added!")
                
            elif choice == '2':
                # Change password
                new_password = input("Enter your new password: ")
                users[username] = new_password
                save_users(users)
                print("Your password has been changed!")
                
            elif choice == '3':
                print("Thank you for using the system!")
                break
            
            else:
                print("Please choose 1, 2 or 3!")
    
    else:
        print("Sorry, wrong username or password!")
    
    # Ask to try again
    again = input("\nWould you like to try again? (yes/no): ")
    if again.lower() != 'yes':
        print("Goodbye!")
        break
