class Animal:
    def make_sound(self, s):
        print(s)


class Horse(Animal):
    def galop(self):
        print('Runs gallop')

pony=Horse()
pony.make_sound('Igogogo')
pony.galop()

