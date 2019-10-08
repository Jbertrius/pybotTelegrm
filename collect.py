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

from upload import *

API_TOKEN = '933543664:AAEpeH1_liPQ2c8KTnGkHYF5j5YYN04qjj8'

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

ADD, NAME, GENDER, AGE, INDO, DATE, NUM, PLACE, \
PERSONA, NATIONALITY, RELIGION, INTEREST, HOME, \
ENV, VACATION, OPPORTUNITY, THREAT, CHURCH_STICK, OT, FRIEND = range(20)


def start(update, context):
    # reply_keyboard = [['Add', 'Edit', 'List']]
    reply_keyboard = [[InlineKeyboardButton('🍎Add', callback_data='add'),
                       InlineKeyboardButton('✏Edit', callback_data='edit'),
                       InlineKeyboardButton('📝List', callback_data='list')]]

    if check_members(update.message.chat_id, ALL_MEMBERS):
        context.user_data['user_id'] = update.message.chat_id
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

        return ADD


def add(update, context):
    """Show new choice of buttons"""
    query = update.callback_query
    bot = context.bot
    context.user_data['type'] = query.data

    user = query.from_user

    # update.message.reply_text('Thank you! I hope we can talk again some day.')

    bot.edit_message_text(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text="Donnez le nom du fruit !"
    )
    return NAME


def name(update, context):
    user = update.message.from_user
    context.user_data['name'] = update.message.text

    reply_keyboard = [[InlineKeyboardButton('👦🏻Boy', callback_data='M'),
                       InlineKeyboardButton('👧🏻Girl', callback_data='F'),
                       InlineKeyboardButton('🔙Retour', callback_data='retry')]]
    update.message.reply_text('{} est une fille ou un garçon ?'.format(context.user_data['name']),
                              reply_markup=InlineKeyboardMarkup(reply_keyboard))
    return GENDER


def gender(update, context):
    """Show new choice of buttons"""
    query = update.callback_query
    bot = context.bot
    context.user_data['gender'] = query.data

    user = query.from_user
    bot.edit_message_text(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text="{} a quel âge ?".format(context.user_data['name'])
    )
    return AGE


def age(update, context):
    """Show new choice of buttons"""
    user = update.message.from_user
    context.user_data['age'] = update.message.text
    update.message.reply_text("Donnez le nom de l'INDOJA !")

    return INDO


def indo(update, context):
    """Show new choice of buttons"""
    user = update.message.from_user
    context.user_data['indo'] = update.message.text
    update.message.reply_text("Quel est le numero de telephone de {} ?".format(context.user_data['name']))

    return NUM


def num(update, context):
    """Show new choice of buttons"""
    user = update.message.from_user
    context.user_data['num'] = update.message.text
    update.message.reply_text("Où est-ce que vous l'avez évangélisez ?")

    return PLACE


def place(update, context):
    """Show new choice of buttons"""
    user = update.message.from_user
    context.user_data['place'] = update.message.text

    # update.message.reply_text(TEMPLATE.format(
    #     context.user_data['name'],
    #     context.user_data['age'],
    #     context.user_data['gender'],
    #     context.user_data['indo'],
    #     context.user_data['num']
    # ))

    update.message.reply_text("Quel jour l'avez vous subae ?")

    # res = save_to_datastore(context.user_data)
    # if res:
    #     update.message.reply_text("{} a été bien enregistré".format(context.user_data['name']))
    # else:
    #     update.message.reply_text("Erreur d'enregistrement !!")

    return DATE


def date(update, context):
    """Show new choice of buttons"""
    user = update.message.from_user
    context.user_data['date'] = update.message.text
    update.message.reply_text("😻Décrivez brievement sa personnalité ! 😻")

    return PERSONA

def persona(update, context):
    """Show new choice of buttons"""
    user = update.message.from_user
    context.user_data['persona'] = update.message.text
    update.message.reply_text("Et heu.., {} est de quel pays ?".format(context.user_data['name']))

    return NATIONALITY

def nationality(update, context):
    """Show new choice of buttons"""
    user = update.message.from_user
    context.user_data['nationality'] = update.message.text
    update.message.reply_text("J'espere que tu sais là où le fruit habite 😫 ?")

    return HOME

def home(update, context):
    """Show new choice of buttons"""
    user = update.message.from_user
    context.user_data['home'] = update.message.text
    update.message.reply_text("Evangélique, Catholique, ...?")

    return RELIGION

def religion(update, context):
    """Show new choice of buttons"""
    user = update.message.from_user
    context.user_data['religion'] = update.message.text
    update.message.reply_text(
        """Comment est son environnement:
        **Suivez le modèle** ➡️ Weekdays/WeekEnd : Exemple ⏺ 08:00-16:00/Free
        """)

    return ENV

def env(update, context):
    """Show new choice of buttons"""
    user = update.message.from_user
    context.user_data['env'] = update.message.text
    update.message.reply_text(
        """
        Finish
        """)

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
            ADD: [CallbackQueryHandler(add, pattern='^' + 'add' + '$')],
            NAME: [MessageHandler(Filters.text, name)],
            GENDER: [CallbackQueryHandler(gender, pattern='^' + '(M|F)' + '$')],
            AGE: [MessageHandler(Filters.regex('^[0-9]{2}$'), age)],
            INDO: [MessageHandler(Filters.text, indo)],
            NUM: [MessageHandler(Filters.regex('^[0-9]{10}$'), num)],
            PLACE: [MessageHandler(Filters.text, place)],
            DATE: [MessageHandler(Filters.text, date)],
            PERSONA: [MessageHandler(Filters.text, persona)],
            NATIONALITY: [MessageHandler(Filters.text, nationality)],
            HOME: [MessageHandler(Filters.text, home)],
            ENV: [MessageHandler(Filters.text, env)],
            RELIGION: [MessageHandler(Filters.text, religion)],

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
