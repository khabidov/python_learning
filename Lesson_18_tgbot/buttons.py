


































def choice_pr_buttons(pr_amount, plus_or_minus='',amount=1):
    kb=types.InlineKeyboardMarkup(row_width=3)
    #Create buttons

#Cart buttons
def cart_buttons():
    #create space
    kb=types.InlineKeyboardMarkup(row_width=2)
    #create buttons
    order=types.InlineKeyboardButton(text='Process order ', callback_data='order')
    back=types.InlineKeyboardButton(text='Back', callback_data='back')
    clear=types.InlineKeyboardButton(text='Clear cart', callback_data='clear')
    #Add buttons to space
    kb.add(order, back)
    kb.row(clear)

    return kb
