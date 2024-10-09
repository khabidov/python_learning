class Rectangle:
    def __init__(self, width, height):
        self.width=width
        self.height=height

    @property
    def area(self):
        return self.width*self.height

room=Rectangle(4,5)
print(room.area)

room=Rectangle(5,10)
print(room.area)
print(vars(room))