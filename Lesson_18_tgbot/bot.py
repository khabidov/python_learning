from array import array

import telebot.types
from pyexpat.errors import messages

from Lesson2.Lesson2 import spam1
from Lesson_4_Cycles.Lesson_4_8 import number

#Creating bot object
bot=telebot.Telebot('')
#Administrator ID
admin_id=
#Temp data
admins={}
users ={}






























#Stage actions on goods
@bot.callback_query_handler(lambda call: call.data in ['increment', 'decrement', 'to_cart', 'back']
def choose_count(call):
    if call.data=='increment':
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message.id=call.message.message.id,
        reply_markup=bt.choice_pr_buttons(db.get_exact_pr(users[call.message.chat.id]['pr_name'])[4],
                                          'increment',users[call.message.chat.id]['pr_amount']))
        users[call.message.chat.id]['pr_amount']+=1
    elif call.data=='decrement':
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message.id = call.message.message.id,
        reply_markup = bt.choice_pr_buttons(db.get_exact_pr(users[call.message.chat.id]['pr_name'])[4],
                                            'increment', users[call.message.chat.id]['pr_amount']))













def cart_handle(call):
    text='Your cart \n\n'
    if call.data=='clear':
        db.clear_cart(call.message.chat.id)
        bot.delete_message

    bot.send_message(call.message.chat.id,)









#Working with cart stage
@bot.callback_query_handler(lambda call:call.data in ['cart','order','clear'])
def cart_handle(call):
    text='Your cart:\n]n'
    if call.data=='clear':
        db.clear_cart(call.message.chat.id)
        bot.delete_message(chat_id=call.message.chat.id,message_id=call.message.message_id)
        bot.send_message(call.message.chat.id,'Cart is cleared!', reply_markup=bt.main_menu(db.get_pr_buttons()))
    elif call.data=='cart':
        user_cart=db.show_cart(call.message.chat.id)
        total=0.0
        for i in user_cart:
            text +=(f'Goods: {i[1]}\n'
                    f'Quantity: {i[2]}\n\n')
            total=db.get_exact_price(i[0])[0]*i[2]
        text +=f'Total: {round(total,1)}'
        bot.delete_message(chat_id=call.message.chat.id,message_id=call.message.message.id)
        bot.send_message(call.messsage.chat.id, text)
    elif call.data=='order':
        text.replace('Your cart: ', 'New order!')
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message.id)
        bot.send_message(call.message.chat.id, 'Send your location for delivery', reply_markup=bt.location_button())

#Location receiving stage
def get_user_location(message,text):
    user_id=message.from_user.id
    #check if location sent using button
    if message.location:
        text +=f'Client@{message.from_user.username}'
        bot.send_message(admin_id,latitude=message.location.latitude, longitude=message.location.longitude)
        db.make_order(user_id)
        bot.send_message(user_id,'Your order is registered! You will be contacted soon!', reply_markup=telebot.types.ReplyKeyboardRemove())
        bot.




@bot.callback_query_handler(lambda call: int(call.data) in [i[0] for i in db.get_all_pr()])
def choose_pr_count(call):
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message.id)
    pr_info=db.get_exact_pr(int(call.data))
    bot.send_photo(call.message.chat.id,photo=pr_info[5]),
                    caption=f'{pr_info[1]}\n\n'
                    f'Description:{pr_info[2]}\n'
                    f'Quantity: {pr_info[4]}\n'
                    f'Price: {pr_info[3]}', reply_markup=bt.choice_pr_buttons(pr_info[4]))
    users[call.message.chat.id]={'pr_name':call_data, 'pr_amount':1}




##Admin panel##
#/admin command handler

























































#Receiving product to delete
def get_product_to_del(message):
    pr_to_del=message.text
    bot.send_message(admin_id,'Are you sure?',reply_marking=bt.confirm_buttons())
    #Switching to confirmation stage
    bot.register_next_step_handler



#Receiving product to change













































#Confirmation stage
def confirm_channge(message, attr):
    bot.send_message(admin_id,'Are you sure?', reply_markup=bt.confirm_buttons())
    new_value=message



#Stage confirming deletion
def confirm_delete(message, pr_to_del):
    if message.text=='Yes':
        db.del_product(pr_to_del)
        bot.send_message(admin_id,'Product successfully deleted', reply_markup=bt_adminmenu())
        #Swithing to selection stage
        bot.register_next_step_handler(massage, admin_choice)
    elif message.text=='No':
        bot.send_message(admin_id, 'Going back')






#Confirmation change stage
def confirm_change_attr(message, attr, new_value):
    if message.text=='Yes':
        if attr=='price':
            db.change_pr_attr(admins[message.from_user.ud],float(new_value),attr)
        else:
            db_change_pr_attr(admins[message.from_user.id], new_value, attr)
        bot.send_message(admin_id,'Change was successful', reply_markup=bt.admin_menu())
        #Switching to selection stage
        bot.register_next_step_handler(message, admin_choice)
    elif message.text=='No':
