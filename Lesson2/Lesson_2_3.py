x=int(input('enter 1st number '))
action=input('enter operator ')
y=int(input('enter 2nd number '))

if action== '/':
    print(x/y)
elif action=='+':
    print(x+y)
elif action=='*':
    print(x*y)
else:
    print(x-y)

