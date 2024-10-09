class Car:
    def __init__(self,model,color,year):
        self.model=model
        self.color=color
        self.year=year

    def stop(self):
        print('Car stopped')
    def start(self):
        print('Car started running')
    def change_color(self,new_color):
        self.color=new_color



class Person:
    name='Jordan'
    age=30
    job='Programmer'

class House:
    def __init__(self, number,street,index,city,country):
        self.number=number
        self.street=street
        self.index=index
        self.city=city
        self.country=country

    def sell(self):
        print('House is for sale')


home=House(2, 'Ainiy',100042, 'Tashkent', 'Uzbekistan')

print(home)
print(f'{vars(home).values()}')

class Comment:
    def __init__(self, username, text, likes=0):
        self.username=username
        self.text=text
        self.likes=likes

gentra=Car('Ravon','White',2022)


gentra.stop()
gentra.start()
gentra.change_color('Black')
print(gentra.color)
home.sell()
