class Worker:
    def __init__(self, name, position):
        self.name=name
        self.position=position

class HR(Worker):
    def __init__(self,name, position):
        super().__init__(name,position)

    def show_position(self, worker):
        return worker.position

jordan=Worker('Jordan','middle dev')
pavel=HR('Steve', 'HR')

print(pavel.show_position(jordan))