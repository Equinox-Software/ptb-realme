import logging

from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler, CallbackQueryHandler

from config import *
from constants import FORBIDDEN_TEXT
from messages.control import *
from messages.general import *
from messages.offtopic import *
from messages.support import *
from postgres import PostgresPersistence
from utils import remove_message

##########################################
# This file serves as an entry point to the program.
# Here all the stuff is initialized and updates being handled.
##########################################


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


def start_session() -> scoped_session:
    engine = create_engine(DATABASE_URL, client_encoding="utf8")
    return scoped_session(sessionmaker(bind=engine, autoflush=False))


def error(update: Update, context: CallbackContext):
    logger.warning('Update "%s" caused error "%s"', update, context.error)
    if update is Update:
        context.bot.send_message(CONTROL_GROUP,
                                 "<b>🤖 Affected Bot</b>\n@" + context.bot.username +
                                 "\n\n<b>⚠️ Error</b>\n<code>" + str(context.error) +
                                 "</code>\n\n<b>Caused by Update</b>\n<code>" + str(update) + "</code>",
                                 ParseMode.HTML)


if __name__ == '__main__':
    session = start_session()

    updater = Updater(TOKEN, persistence=PostgresPersistence(session))
    dp = updater.dispatcher

    for i in FORBIDDEN_TEXT:
        dp.add_handler(MessageHandler(Filters.regex(r"(?i)" + i), remove_message))

    # General
    dp.add_handler(CommandHandler("gcam", gcam))
    dp.add_handler(CommandHandler("cleaners", cleaners))
    dp.add_handler(CommandHandler("polls", polls))
    dp.add_handler(CommandHandler("rules", rules))
    dp.add_handler(CommandHandler("cool", cool))
    dp.add_handler(MessageHandler(Filters.regex(r"(?i)(?:(?!/)rmx\d{4})"), rmx))

    # Support
    dp.add_handler(CommandHandler("android11", android11, Filters.chat(SUPPORT_GROUP)))
    dp.add_handler(CommandHandler("help", commands, Filters.chat(SUPPORT_GROUP)))
    dp.add_handler(CommandHandler("admins", admins, Filters.chat(SUPPORT_GROUP)))
    dp.add_handler(CommandHandler("experts", experts, Filters.chat(SUPPORT_GROUP)))
    dp.add_handler(CommandHandler("debloat", debloat, Filters.chat(SUPPORT_GROUP)))
    dp.add_handler(CommandHandler("ask", ask, Filters.chat(SUPPORT_GROUP)))
    dp.add_handler(CommandHandler("form", form, Filters.chat(SUPPORT_GROUP)))
    dp.add_handler(CommandHandler("battery", battery, Filters.chat(SUPPORT_GROUP)))
    dp.add_handler(CommandHandler("whatsapp", whatsapp, Filters.chat(SUPPORT_GROUP)))
    dp.add_handler(CommandHandler("benchmark", benchmark, Filters.chat(SUPPORT_GROUP)))
    dp.add_handler(CommandHandler("aod", aod, Filters.chat(SUPPORT_GROUP)))
    dp.add_handler(CommandHandler("manual", manual, Filters.chat(SUPPORT_GROUP)))
    dp.add_handler(CommandHandler("offtopic", move_to_offtopic, Filters.chat(SUPPORT_GROUP)))
    dp.add_handler(CommandHandler("bug", bug, Filters.chat(SUPPORT_GROUP)))
    dp.add_handler(CommandHandler("stable", stable, Filters.chat(SUPPORT_GROUP)))
    dp.add_handler(CommandHandler("push", push, Filters.chat(SUPPORT_GROUP)))

    # Personal opinion
    dp.add_handler(CommandHandler("ram", ram, Filters.chat(SUPPORT_GROUP)))
    dp.add_handler(CommandHandler("rant", rant, Filters.chat(SUPPORT_GROUP)))
    dp.add_handler(CommandHandler("fps", fps, Filters.chat(SUPPORT_GROUP)))

    # Offtopic
    dp.add_handler(CommandHandler("translate", translate, Filters.chat(OFFTOPIC_GROUP)))
    dp.add_handler(CommandHandler("support", move_to_support, Filters.chat(OFFTOPIC_GROUP)))

    # Upcoming
    dp.add_handler(CommandHandler("warn", warn, Filters.chat(OFFTOPIC_GROUP) & Filters.user(ADMINS)))
    dp.add_handler(CommandHandler("ban", ban, Filters.chat(OFFTOPIC_GROUP) & Filters.user(ADMINS)))
    dp.add_handler(MessageHandler(Filters.text("@admin"), admin))
    dp.add_handler(CallbackQueryHandler(remove_click, pattern="BAN_remove"))
    dp.add_handler(CallbackQueryHandler(button_click))

    # Control
    dp.add_handler(CommandHandler("reset", reset, Filters.chat(CONTROL_GROUP) & Filters.user(ADMINS)))
    dp.add_handler(CommandHandler("clear", clear, Filters.chat(CONTROL_GROUP) & Filters.user(ADMINS)))

    # Private
    dp.add_handler(MessageHandler(Filters.chat_type.private, private_not_available))

    # Crap
    dp.add_handler(CommandHandler("banana", banana))
    dp.add_handler(CommandHandler("realistic", realistic))
    dp.add_handler(MessageHandler(Filters.regex(r"69"), nice, Filters.chat(OFFTOPIC_GROUP)))

    # Commands have to be added above
    # dp.add_error_handler(error)  # comment this one out for full stacktrace

    updater.start_webhook("0.0.0.0", PORT, TOKEN, webhook_url='https://ptb-realme.herokuapp.com/' + TOKEN)
    updater.idle()
