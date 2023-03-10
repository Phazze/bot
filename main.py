import requests
from datetime import datetime
import telebot
from telebot import types
from auto_data import token
def get_data():
    req = requests.get("https://yobit.net/api/3/ticker/btc_usd")
    response = req.json()
    sell_price = response["btc_usd"]["sell"]
    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nSell BTC price: {sell_price}")

def telegram_bot(token):
    bot = telebot.TeleBot(token)

    @bot.message_handler(commands= ["start"])
    def start_message(message):
        markup = types.InlineKeyboardMarkup(row_width=1)
        btc_button = types.InlineKeyboardButton('BTC $$$', callback_data='price btc')
        eth_button = types.InlineKeyboardButton('ETH $$$', callback_data='price eth')
        trx_button = types.InlineKeyboardButton('TRX $$$', callback_data='price trx')
        usdt_button = types.InlineKeyboardButton('USDT $$$', callback_data = 'price usdt')
        markup.add(btc_button, eth_button, trx_button, usdt_button)
        bot.send_message(message.chat.id, "Hello my friend! Write the 'price' to find price", reply_markup=markup)

    @bot.callback_query_handler(func= lambda call:True )
    #def send_text(message):
    def callback(call):
        if call.message:
            if call.data == 'price btc':
                try:
                    req = requests.get("https://yobit.net/api/3/ticker/btc_usd")
                    response = req.json()
                    sell_price = response["btc_usd"]["sell"]
                    bot.send_message(
                        call.message.chat.id,
                        f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nSell BTC price: {sell_price}"
                    )

                except Exception as ex:
                    print(ex)
                    bot.send_message(
                        call.message.chat.id,
                        "Damn.....Somethng was wrong..."
                    )
            elif call.data == "price eth":
                try:
                    req = requests.get("https://yobit.net/api/3/ticker/eth_usd")
                    response = req.json()
                    sell_price = response["eth_usd"]["sell"]
                    bot.send_message(
                        call.message.chat.id,
                        f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nSell ETH price: {sell_price}"
                    )

                except Exception as ex:
                    print(ex)
                    bot.send_message(
                        call.message.chat.id,
                        "Damn.....Somethng was wrong..."
                    )

            elif call.data == "price trx":
                try:
                    req = requests.get("https://yobit.net/api/3/ticker/trx_usd")
                    response = req.json()
                    sell_price = response["trx_usd"]["sell"]
                    bot.send_message(
                        call.message.chat.id,
                        f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\n Sell TRX price:{sell_price}"
                    )

                except Exception as ex:
                    print(ex)
                    bot.send_message(
                        call.message.chat.id,
                        "Damn......Something was wrong..."
                    )
            elif call.data == "price usdt":
                try:
                    req = requests.get("https://yobit.net/api/3/ticker/usdt_usd")
                    responce = req.json()
                    sell_price = responce["usdt_usd"]["sell"]
                    bot.send_message(
                        call.message.chat.id,
                        f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\n Sell USDT price:{sell_price}"
                    )
                except Exception as ex:
                    print(ex)
                    bot.send_message(
                        call.message.chat.id,
                        "Damn...Something was wrong..."
                    )
            else:
                bot.send_message(call.message.chat.id, "What??? Check the command dude!")
    bot.polling()

if __name__ == "__main__":
    #get_data()
    telegram_bot(token)


