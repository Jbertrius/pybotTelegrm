# !/usr/bin/env python
# -*- coding: utf-8 -*-
# This program is dedicated to the public domain under the CC0 license.

"""
First, a few callback functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Example of a bot-user conversation using ConversationHandler.
Send /start to initiate the conversation.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import logging

from Members import *
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler,
                          ConversationHandler)

API_TOKEN = '933543664:AAEpeH1_liPQ2c8KTnGkHYF5j5YYN04qjj8'

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

NAME, GENDER, AGE, INDO, DATE, PHONE = range(6)


def start(update, context):
    # reply_keyboard = [['Add', 'Edit', 'List']]
    reply_keyboard = [[InlineKeyboardButton('🍎Add', callback_data='add'),
                       InlineKeyboardButton('✏Edit', callback_data='edit'),
                       InlineKeyboardButton('📝List', callback_data='list')]]

    if check_members(update.message.chat_id, ALL_MEMBERS):
        update.message.reply_text(
            """
Hello {},

Bienvenue sur le bot de gestion des fruits après le sobae. 

Vous pouvez :
▪️Enregistrez les informations de vos fruits
▪️Modifiez les informations de vos fruits
▪️Consultez la liste vos fruits

Enjoy ‼️🙈
            """.format(update.message.from_user.username),
            reply_markup=InlineKeyboardMarkup(reply_keyboard))

        return NAME


def gender(update, context):
    user = update.message.from_user

    reply_keyboard = [[InlineKeyboardButton('🍎Boy', callback_data='boy'),
                       InlineKeyboardButton('✏Girl', callback_data='girl'),
                       InlineKeyboardButton('📝Retour', callback_data='retry')]]

    update.message.reply_text('Est-ce une fille ou un garçon ?',
                              reply_markup=InlineKeyboardMarkup(reply_keyboard))

    return ConversationHandler.END

#
# def photo(update, context):
#     user = update.message.from_user
#     photo_file = update.message.photo[-1].get_file()
#     photo_file.download('user_photo.jpg')
#     logger.info("Photo of %s: %s", user.first_name, 'user_photo.jpg')
#     update.message.reply_text('Gorgeous! Now, send me your location please, '
#                               'or send /skip if you don\'t want to.')
#
#     return LOCATION
#
#
# def skip_photo(update, context):
#     user = update.message.from_user
#     logger.info("User %s did not send a photo.", user.first_name)
#     update.message.reply_text('I bet you look great! Now, send me your location please, '
#                               'or send /skip.')
#
#     return LOCATION

#
# def location(update, context):
#     user = update.message.from_user
#     user_location = update.message.location
#     logger.info("Location of %s: %f / %f", user.first_name, user_location.latitude,
#                 user_location.longitude)
#     update.message.reply_text('Maybe I can visit you sometime! '
#                               'At last, tell me something about yourself.')
#
#     return BIO


# def skip_location(update, context):
#     user = update.message.from_user
#     logger.info("User %s did not send a location.", user.first_name)
#     update.message.reply_text('You seem a bit paranoid! '
#                               'At last, tell me something about yourself.')
#
#     return BIO

def name(update, context):
    """Show new choice of buttons"""
    query = update.callback_query
    bot = context.bot

    user = query.from_user
    # update.message.reply_text('Thank you! I hope we can talk again some day.')

    bot.edit_message_text(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text="Donnez le nom du fruit !"
    )
    return GENDER


# def bio(update, context):
#     user = update.message.from_user
#     logger.info("Bio of %s: %s", user.first_name, update.message.text)
#     update.message.reply_text('Thank you! I hope we can talk again some day.')
#
#     return ConversationHandler.END


def cancel(update, context):
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    update.message.reply_text('Bye! I hope we can talk again some day.',
                              reply_markup=ReplyKeyboardRemove())

    return ConversationHandler.END


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def check_members(user_id, autorized_list):
    return user_id in autorized_list


def main():
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(API_TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Add conversation handler with the states GENDER, PHOTO, LOCATION and BIO
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],

        states={
            NAME: [CallbackQueryHandler(name, pattern='^' + 'add' + '$'),],
            GENDER: [MessageHandler(Filters.regex('^(boy|girl)$'), gender)],

            # PHOTO: [MessageHandler(Filters.photo, photo),
            #         CommandHandler('skip', skip_photo)],
            #
            # LOCATION: [MessageHandler(Filters.location, location),
            #            CommandHandler('skip', skip_location)],
            #
            # BIO: [MessageHandler(Filters.text, bio)]
        },

        fallbacks=[CommandHandler('cancel', cancel)]
    )

    dp.add_handler(conv_handler)

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
