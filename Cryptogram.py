from telegram.ext import Updater
token = '463277822:AAGhIn--7kELcYSB7MhVp-JUTkOOZtCWZUo'
updater = Updater(token=token)
dispatcher = updater.dispatcher

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

import requests
import sys

URL = "https://coinmarketcap.com/currencies/bitcoin/"
page = requests.get(URL)
from bs4 import BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')
BTCPrice = soup.find_all('span', class_="text-large")[0].get_text()

# This code block adds a thousands separator to the given price.
btcPriceNoDollarSign = BTCPrice[1:]
btcPriceFloated = float(btcPriceNoDollarSign)
btcPriceWithCommas = "{:,}".format(btcPriceFloated)
formattedPrice = "1 BTC = $" + btcPriceWithCommas

def btc(bot, update): 
	bot.send_message(chat_id=update.message.chat_id, text=formattedPrice)

def insultMe(bot, update):
	bot.send_message(chat_id=update.message.chat_id, text="Go fuck yourself.")

from telegram.ext import CommandHandler
start_handler = CommandHandler('btc', btc)
dispatcher.add_handler(start_handler)

insultMe_handler = CommandHandler('insultMe', insultMe)
dispatcher.add_handler(insultMe_handler)

updater.start_polling()



