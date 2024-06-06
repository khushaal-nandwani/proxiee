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
    return files[file_num-1]

def main():
    files = get_files()
    if not files:
        print('No files found')
        return
    file = get_file(files)

    users_data = {}
    safe = True
    
    with open(file) as f:
        for line in f:
            fields = line.split(',')
            user = fields[0]
            if user not in users_data:
                # TODO: A user may switch IP through a day, since log is created everyday. Manage a permanent list. 
                users_data[user] = {'Count': 0, 'Client_IP': fields[-1].strip(), 'Safe': True}
            users_data[user]['Count'] += 1
            if users_data[user]['Client_IP'] != fields[-1].strip():
                users_data[user]['Safe'] = False
                print('\n!!!!!!!!!!!!!!!! ALERT !!!!!!!!!!!!!!!!')
                print(f'{user} is not safe. IP changed from {users_data[user]["Client_IP"]} to {fields[-1].strip()}\n\n')
                safe = False
    
    for user, data in users_data.items():
        print(f'{user} called {data["Count"]} APIs')
    
    if safe:
        print('\nAll users are safe')
    else:
        print('\nSome users are not safe. Check the alerts above')

if __name__ == '__main__':
    main()
            


            
            

