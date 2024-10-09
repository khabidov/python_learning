names=[]
numbers=[]
services=[]

while True:
    choice=input('Choose list to add to: ')
    if choice=='Name':
        new_name=input('Please enter name: ')
        names.append(new_name)
        print('Name added!')
        print(names)
    elif choice=='Service':
        new_service=input('Enter new service: ')
        services.append(new_service)
        print('Service added!')
        print(services)
    elif choice=='Number':
        new_number=input('Enter new number: ')
        numbers.append(new_number)
        print('Number added!')
        print(numbers)
    elif choice=='Stop':
        break

    else:print('Wrong entry!')