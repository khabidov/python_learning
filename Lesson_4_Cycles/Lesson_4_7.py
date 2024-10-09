names=['Ivan','Steve','Mike']
while True:
    new=input('Enter ')
    if new=='List':
        print(names)
    elif new in names:
        print(f'{new} already in the list')
    else:
        names.append(new)
        print(f'{new} added')