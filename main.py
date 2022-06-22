# Library import
import csv
import os

try:
    import telebot
except ModuleNotFoundError:
    os.system('cmd /c "pip install pyTelegramBotAPI"')

# Bot ID
bot = telebot.TeleBot("5092374817:AAFNdFjjcLuOLRqmVkpwIe-DwRUghkOIMbg")

# Reading of a database file into a variable
database_csv_file = []
with open("database.csv", "r") as file:
    file_read = csv.reader(file, delimiter=',')
    database_csv_file = [row for row in file]


# Definition for finding a keyword
def keyword_finder(keyword):
    keyword_index = database_csv_file.index(keyword)
    return database_csv_file[keyword_index]

#    for col in range (0,len(array),1):
#        if (mes == (array[col][0])): return(array[col][1])
# print(finder(temp))


users = [264293916]


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, message.from_user.id)


@bot.message_handler(func=lambda message: message.chat.id not in users)
def welcome_song(message):
    bot.send_message(message.chat.id, """Twinkle, twinkle, little star,\n
                     How I wonder what you are!\n
                     Up above the world so high,\n
                     Like a diamond in the sky.\n
                     Twinkle, twinkle, little star,\n
                     How I wonder what you are!""")


@bot.message_handler(func=lambda message: True)
def send_message(message):
    bot.reply_to(message, keyword_finder(message.text))


#    bot.reply_to(message, '1434')

bot_alive = bot.infinity_polling()

while bot_alive:
    try:
        bot_alive
    except KeyboardInterrupt:
        bot_alive = False
        continue
