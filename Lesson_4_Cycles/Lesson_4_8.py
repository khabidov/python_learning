names=[]
numbers=[]
services=[]
while True:
    choice=input('Select the list to add to ')
    if choice=='Names':
        name=input('Type name to add: ')
        names.append(name)
        print(names)
    elif choice=='Numbers':
        number=input('Type number to add: ')
        numbers.append(number)
        print(numbers)
    elif choice=="Services":
        service=input('Type service to add: ')
        services.append(service)
        print(services)
    elif choice=='Stop':
        break
    else:
        print('Wrong entry')
