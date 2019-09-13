#!/usr/bin/python

# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.

import telebot
import time

API_TOKEN = '933543664:AAGVT6FjXMGfOuee6Pm2ID31gOo97piGXBg'

bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.kick_chat_member(message.chat.id, message.from_user.id)
    unique_code = extract_unique_code(message.text)
    bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say {0} the exact same thing to you!\
""".format(unique_code))


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
# @bot.message_handler(commands=['help', 'start'])
# def echo_message(message):
#     # bot.kick_chat_member('933543664', message.from_user.id)
#     bot.reply_to(message, message.text)

def extract_unique_code(text):
    # Extracts the unique_code from the sent /start command.
    return text.split()[1] if len(text.split()) > 1 else None

def in_storage(unique_code):
    # Should check if a unique code exists in storage
    return True

def get_username_from_storage(unique_code):
    # Does a query to the storage, retrieving the associated username
    # Should be replaced by a real database-lookup.
    return "ABC" if in_storage(unique_code) else None

def save_chat_id(chat_id, username):
    # Save the chat_id->username to storage
    # Should be replaced by a real database query.
    pass


bot.infinity_polling(True)
