#! /usr/bin/env python3

import sys
import telebot
import argparse
import data_info as data

parser = argparse.ArgumentParser()
parser.add_argument( "-t", "--token", required = True )
parser.add_argument( "-c", "--chat_id", required = True )
args = parser.parse_args()

#------------------------------------------------------------------------------
bot_token = args.token
bot = telebot.TeleBot( bot_token )
pepe_chat_id = int( args.chat_id )

#------------------------------------------------------------------------------
@bot.message_handler( content_types=['text'] )
def get_text_messages( message ):
    if message.chat.id == pepe_chat_id:
        process_pepe_messeges( message )

def process_pepe_messeges( message ):
    if message.text.lower() in data.pp_uk_info:
        bot.reply_to( message, data.pp_uk_info_answer )
    elif message.text.lower() in data.pp_mail:
        bot.reply_to( message, data.pp_mail_answer )
        bot.send_location( message.chat.id, data.pp_mail_lat, data.pp_mail_long )
    elif message.text.lower() in data.pp_health:
        bot.reply_to( message, data.pp_health_answer )
        bot.send_location( message.chat.id, data.pp_health_lat, data.pp_health_long )
    elif message.text.lower() in data.pp_health_kids:
        bot.reply_to( message, data.pp_health_kids_answer )
    elif message.text.lower() in data.pp_passport:
        bot.reply_to( message, data.pp_passport_answer )
        bot.send_location( message.chat.id, data.pp_passport_lat, data.pp_passport_long )
    elif message.text.lower() in data.pp_emergency:
        bot.reply_to( message, data.pp_emergency_answer )
    elif message.text.lower() in data.pp_police:
        bot.reply_to( message, data.pp_police_answer )
    elif message.text.lower() in data.pp_kvd:
        bot.reply_to( message, data.pp_kvd_answer )
        bot.send_location( message.chat.id, data.pp_kvd_lat, data.pp_kvd_long )

#------------------------------------------------------------------------------
def main():
    bot.polling( none_stop=True, interval=0 )

#------------------------------------------------------------------------------
if __name__ == "__main__":
    sys.exit( main() )