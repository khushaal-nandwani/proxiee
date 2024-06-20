import os

def get_files():
    files = [f for f in os.listdir('.') if os.path.isfile(f) and f.startswith('proxiee_logs_')]
    return files

def print_files(files):
    for i, f in enumerate(files):
        print(f'{i+1}. {f}')

def get_file(files):
    print_files(files)
    file_num = int(input('Enter the number of the file: '))
    print('\n')
    return files[file_num-1]

Users = {
}

def main():
    files = get_files()
    if not files:
        print('No files found')
        return
    file = get_file(files)

    
    with open(file) as f:
        for line in f:
            fields = line.split(',')
            user = fields[0]

            # Create a new user and set the ip
            if user not in Users:
                Users[user] = {
                    'Client_IP': fields[-1].strip(),
                    'Safe': True
                }
            # check the ip
            else:
                if Users[user]['Client_IP'] != fields[-1].strip():
                    Users[user]['Safe'] = False

            # Record the API called and count
            api_called = fields[2].split('/')[2]
            if api_called not in Users[user]:
                Users[user][api_called] = 1
            else:
                Users[user][api_called] += 1
            
    for user in Users:
        print(f'User: {user}')
        for key, value in Users[user].items():
            print(f'{key}: {value}')
        print('\n')

if __name__ == '__main__':
    main()
            


            
            

