import conf
import telebot

bot = telebot.TeleBot(conf.BOT_TOKEN)

@bot.message_handler (content_types=["text"])
def repeat_all_message (message):
    bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
    bot.infinity_polling()
