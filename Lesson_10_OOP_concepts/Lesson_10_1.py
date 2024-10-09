class Cook:
    def cook_food(self):
        print('Cook food')

class Chef(Cook):
    def manage_kitchen(self):
        print('Chef in da house!')

Mike=Chef()
Mike.manage_kitchen()