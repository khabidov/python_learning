usernames=[]
while True:
    name=input('Enter name ')
    if name in usernames:
        print('Name already in the list, enter new name')
    else:
        usernames.append(name)
        print(usernames)