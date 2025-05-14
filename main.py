
# Simple Login System
# This program allows users to login and manage accounts

# Function to get users from file
def get_users():
    try:
        # Try to open and read the users file
        file = open('users.txt', 'r')
        users = {}
        # Read each line and split username:password
        for line in file:
            username, password = line.strip().split(':')
            users[username] = password
        file.close()
        return users
    except:
        # If file doesn't exist, return default admin account
        return {'admin': 'pass123'}

# Function to save users to file
def save_users(users):
    # Open file and write all username:password pairs
    file = open('users.txt', 'w')
    for username in users:
        file.write(f'{username}:{users[username]}\n')
    file.close()

# Main program
def main():
    # Load all users
    users = get_users()
    
    # Main program loop
    while True:
        # Get login details
        print("\n=== LOGIN SYSTEM ===")
        username = input("Enter username: ")
        password = input("Enter password: ")
        
        # Check if login is correct
        if username in users and users[username] == password:
            print("\nWelcome", username)
            
            # Menu loop
            while True:
                print("\nMENU")
                print("1. Add new user")
                print("2. Change my password")
                print("3. Logout")
                
                choice = input("\nEnter choice (1-3): ")
                
                # Add new user
                if choice == '1':
                    new_user = input("New username: ")
                    new_pass = input("New password: ")
                    users[new_user] = new_pass
                    save_users(users)
                    print("User added!")
                
                # Change password
                elif choice == '2':
                    new_pass = input("New password: ")
                    users[username] = new_pass
                    save_users(users)
                    print("Password changed!")
                
                # Logout
                elif choice == '3':
                    print("Goodbye!")
                    break
        
        else:
            print("Wrong username or password!")
        
        # Ask to try again
        again = input("\nTry again? (yes/no): ")
        if again.lower() != 'yes':
            break

# Start the program
main()
