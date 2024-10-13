name='Javlon'
favorite_number=7
value_of_pi=3.14

print(name)
print(favorite_number)
print(value_of_pi)

spam, spam1 = 36, 50
print (spam)

print(type(spam))
print(type(2.00))
print(type('2.00'))

spam=input('enter something ')
print(spam)


t = [1, 2, 4, 3, 8, 9]
b = [t[i] for i in range(0, len(t), 2)]
print(b)

d = {"john":40, "peter":45}
print(d["john"])

t = (1, 2)
b = 2 * t
print(b)

nums = set([1,1,2,3,3,3,4,4])
print(len(nums))

a={5,4}
b={1,2,4,5}
print(a<b)

a=[4,5,6]
b=[2,8,6]
print(a+b)