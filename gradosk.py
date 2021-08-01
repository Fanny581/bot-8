import telebot # importamos la libreria de telebot
bot = telebot.TeleBot('1717580618:AAH8xtXrBlziXF3LzSNDzHRb8Q2h745fJCA') #anadimos el token
updates = bot.get_updates()
message = updates[0].message
from_user = message.from_user
id = from_user.id
get_me = bot.get_me()
@bot.message_handler(commands=['hola', 'hi']) #definimos el comando
def hola(mensaje):
    bot.reply_to(mensaje, "Hola como estás?")
    print("Mandaron hola o hi")
@bot.message_handler(commands=['celsius', 'celsius']) #definimos el comando
def hola(mensaje):
    bot.reply_to(mensaje, " la formulas Grados Celsius a Grados Kelvin es  K = ºC + 273.15.")
    print("Mandaron Celsius o Celsius")
@bot.message_handler(commands=['kelvin', 'kelvin']) #definimos el comando
def hola(mensaje):
    bot.reply_to(mensaje, " la formulas Grados kelvin a Grados Celsius es ºC = K – 273.15")
    print("Mandaron kelvin o kelvin")
bot.polling()