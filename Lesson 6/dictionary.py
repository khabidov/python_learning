# x={'name':'Pasha','job':'TGbotcreator'}
# print(x['name'])
# print(x['job'])
#
# data={'name':['Jordan','Pavel'],'age':(12,21),'job':'programmers'}
# print(data['name'][0],data['job'][-1])
#
# instructor={'name':'Jordan', 'age':21, 'job':'programmer'}
# print(instructor.values())
# print(instructor.keys())
# print(instructor.items())
#
# if 21 in instructor.values():
#     print("Yes, it's there")
# else:
#     print('What are you talking about?')
#
#
# if 21 in instructor:
#     print("Yes, it's there")
# else:
#     print('What are you talking about?')

# users={}
# users['name']='Jordan'
# print(users)
# print(users['name'])
#
# cafees={'Evos':{'Gorod':'Tashkent','Filialov':'Mnogo','Otkritie':2007}}
# cafees['Evos']['kuchnya']='Fast Food'
# print(cafees)

# my_dict={'name': 'Jordan'}
# my_dict['name']='Pasha'
# print(my_dict)
# my_dict['name']='Pasha'
# print(my_dict)

# my_dict={'song': 'Godzilla','singer':'Eminem'}
#
# my_dict.pop('song')
# print(my_dict)
#
# my_dict.popitem()
# print(my_dict)
#
# my_dict.clear()
# print(my_dict)

instructor=dict(name='Jordan', age=32, job='Python developer')
y=instructor['age']*2
instructor['age']=y
print(instructor)

