
import json
import os

def load_users():
    if os.path.exists('users.txt'):
        with open('users.txt', 'r') as file:
            return json.load(file)
    return {}

def save_users(users):
    with open('users.txt', 'w') as file:
        json.dump(users, file)

def create_new_user(current_user, users):
    print("\nCreate New User")
    username = input("Enter new username: ")
    if username in users:
        print("Username already exists!")
        return
    
    password = input("Enter password for new user: ")
    users[username] = password
    save_users(users)
    print(f"User '{username}' created successfully!")

def change_password(current_user, users):
    print("\nChange Password")
    old_password = input("Enter your current password: ")
    if users[current_user] != old_password:
        print("Current password is incorrect!")
        return
    
    new_password = input("Enter new password: ")
    users[current_user] = new_password
    save_users(users)
    print("Password changed successfully!")

def main():
    users = load_users()
    
    # Create default admin user if no users exist
    if not users:
        users = {"admin": "admin"}
        save_users(users)

    while True:
        username = input("Username: ")
        password = input("Password: ")

        if username in users and users[username] == password:
            print("Login successful!")
            print("Access granted.")
            
            while True:
                print("\nOptions:")
                print("1. Create new user")
                print("2. Change password")
                print("3. Logout")
                
                choice = input("Enter your choice (1-3): ")
                
                if choice == "1":
                    create_new_user(username, users)
                elif choice == "2":
                    change_password(username, users)
                elif choice == "3":
                    print("Logging out...")
                    break
                else:
                    print("Invalid choice!")
        else:
            print("Access denied.")
            retry = input("Try again? (y/n): ")
            if retry.lower() != 'y':
                break

if __name__ == "__main__":
    main()
