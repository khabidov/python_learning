import telebot

bot=telebot.TeleBot()

@bot.message_handler(command=['start'])
    def start(message):
        bot.send_invoice(message.from_user.id,
                         tittle='PAYMENT',
                         description='MAKE PAYMENT',
                         provider_token=pay_me_token,
                         currency='uzs',
                         photo_url=
                         