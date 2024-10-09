class User:
    def __init__(self,name,email,age,telephone):
        self.name=name
        self.email=email
        self.age=age
        self.telephone=telephone

    def change_username(self, new_name):
        self.name=new_name

    def change_number(self,new_number):
        self.telephone=new_number

    def change_email(self, new_email):
        self.email=new_email

pavel=User('Pavel','pavel@mail.com',23,'+998999999999')
print(vars(pavel))