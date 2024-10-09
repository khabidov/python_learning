clients=['John','Steve','Mike']
print(clients)
name_to_add=input('Enter name to add: ')
clients.append(name_to_add)
print(clients)

name_to_delete=input('Enter name to delete: ')
if name_to_delete in clients:
    clients.remove(name_to_delete)
    print(clients)
else:
    print('Name is not in the list')

name_to_change=input('Enter name to change: ')
if name_to_change in clients:
    change_name=input('Enter new name: ')
    clients[clients.index(name_to_change)]=change_name
    print(clients)
else:
    print('Name is not in the list')


