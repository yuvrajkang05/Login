def load_users():
    try:
        with open('users.txt', 'r') as file:
            return dict(line.strip().split(':') for line in file)
    except:
        return {'admin': 'admin'}

def save_users(users):
    with open('users.txt', 'w') as file:
        for username, password in users.items():
            file.write(f'{username}:{password}\n')

def main():
    users = load_users()

    while True:
        username = input('Username: ')
        password = input('Password: ')

        if username in users and users[username] == password:
            print('Access granted')

            while True:
                choice = input('\n1. Add user\n2. Change password\n3. Logout\nChoice: ')

                if choice == '1':
                    new_user = input('New username: ')
                    new_pass = input('New password: ')
                    users[new_user] = new_pass
                    save_users(users)
                    print('User added')

                elif choice == '2':
                    new_pass = input('New password: ')
                    users[username] = new_pass
                    save_users(users)
                    print('Password changed')

                elif choice == '3':
                    break
        else:
            print('Access denied')
            if input('Try again? (y/n): ').lower() != 'y':
                break

if __name__ == '__main__':
    main()