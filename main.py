import conf
import telebot

bot = telebot.TeleBot(conf.BOT_TOKEN)

@bot.message_handler (content_types=["text"])
def repeat_all_message (message):
    reply_text = "Привет"
    bot.send_message(message.chat.id, reply_text + ", " + message.from_user.first_name)

if __name__ == '__main__':
    bot.infinity_polling()

