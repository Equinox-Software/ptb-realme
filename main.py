"""
This file serves as an entry point to the program.

Here all the stuff is initialized and updates being handled.
"""

import logging

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from telegram import Update, ParseMode
from telegram.ext import (
    CallbackContext,
    CommandHandler,
    Filters,
    MessageHandler,
    Updater, Defaults,
)

import config
from constants import FORBIDDEN_TEXT
from messages.control import clear, reset
from messages.general import (
    banana,
    benchmark,
    cool,
    polls,
    private_not_available,
    realistic,
    rmp,
    rmx,
    rules, about
)
from messages.offtopic import (
    move_to_support
)
from messages.support import (
    android11,
    android12,
    aod,
    apk,
    ask,
    battery,
    bug,
    cleaners,
    commands,
    debloat,
    form,
    fps,
    gcam,
    manual,
    move_to_offtopic,
    push,
    ram,
    rant,
    stable,
    whatsapp, fooview, swap, charge, miss
)
from postgres import PostgresPersistence
from utils import remove_message

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


def start_session() -> scoped_session:
    """Start the database session."""
    engine = create_engine(config.DATABASE_URL, client_encoding="utf8")
    return scoped_session(sessionmaker(bind=engine, autoflush=False))


def error(update: Update, context: CallbackContext):
    """Log the error to control group."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)
    if update is Update:
        context.bot.send_message(
            config.CONTROL_GROUP,
            (
                "<b>🤖 Affected Bot</b>\n@{context.bot.username}\n\n"
                "<b>⚠️ Error</b>\n"
                "<code>{context.error}</code>\n\n"
                "<b>Caused by Update</b>\n"
                "<code>{update}</code>"
            )
        )


if __name__ == "__main__":
    session = start_session()

    updater = Updater(config.TOKEN, persistence=PostgresPersistence(session),
                      defaults=Defaults(parse_mode=ParseMode.HTML))
    dp = updater.dispatcher

    for i in FORBIDDEN_TEXT:
        dp.add_handler(MessageHandler(Filters.regex(r"(?i)" + i), remove_message))

    # General
    dp.add_handler(CommandHandler("cleaners", cleaners))
    dp.add_handler(CommandHandler("cool", cool))
    dp.add_handler(CommandHandler("gcam", gcam))
    dp.add_handler(CommandHandler("polls", polls))
    dp.add_handler(CommandHandler("about", about))
    dp.add_handler(CommandHandler("rules", rules))
    dp.add_handler(MessageHandler(Filters.regex(r"(?i)(?:(?!/)rmp\d{4})"), rmp))
    dp.add_handler(MessageHandler(Filters.regex(r"(?i)(?:(?!/)rmx\d{4})"), rmx))

    # Support
    dp.add_handler(CommandHandler("android11", android11, Filters.chat(config.SUPPORT_GROUP)))
    dp.add_handler(CommandHandler("android12", android12, Filters.chat(config.SUPPORT_GROUP)))
    dp.add_handler(CommandHandler("aod", aod, Filters.chat(config.SUPPORT_GROUP)))
    dp.add_handler(CommandHandler("apk", apk, Filters.chat(config.SUPPORT_GROUP)))
    dp.add_handler(CommandHandler("ask", ask, Filters.chat(config.SUPPORT_GROUP)))
    dp.add_handler(CommandHandler("battery", battery, Filters.chat(config.SUPPORT_GROUP)))
    dp.add_handler(CommandHandler("benchmark", benchmark, Filters.chat(config.SUPPORT_GROUP)))
    dp.add_handler(CommandHandler("bug", bug, Filters.chat(config.SUPPORT_GROUP)))
    dp.add_handler(CommandHandler("debloat", debloat, Filters.chat(config.SUPPORT_GROUP)))
    dp.add_handler(CommandHandler("form", form, Filters.chat(config.SUPPORT_GROUP)))
    dp.add_handler(CommandHandler("help", commands, Filters.chat(config.SUPPORT_GROUP)))
    dp.add_handler(CommandHandler("manual", manual, Filters.chat(config.SUPPORT_GROUP)))
    dp.add_handler(
        CommandHandler("offtopic", move_to_offtopic, Filters.chat(config.SUPPORT_GROUP))
    )
    dp.add_handler(CommandHandler("push", push, Filters.chat(config.SUPPORT_GROUP)))
    dp.add_handler(CommandHandler("stable", stable, Filters.chat(config.SUPPORT_GROUP)))
    dp.add_handler(CommandHandler("fooview", fooview, Filters.chat(config.SUPPORT_GROUP)))
    dp.add_handler(CommandHandler("swap", swap, Filters.chat(config.SUPPORT_GROUP)))
    dp.add_handler(CommandHandler("charge", charge, Filters.chat(config.SUPPORT_GROUP)))
    dp.add_handler(
        CommandHandler("whatsapp", whatsapp, Filters.chat(config.SUPPORT_GROUP))
    )
    dp.add_handler(
        CommandHandler("miss", miss, Filters.chat(config.SUPPORT_GROUP))
    )

    # Personal opinion
    dp.add_handler(CommandHandler("fps", fps, Filters.chat(config.SUPPORT_GROUP)))
    dp.add_handler(CommandHandler("ram", ram, Filters.chat(config.SUPPORT_GROUP)))
    dp.add_handler(CommandHandler("rant", rant, Filters.chat(config.SUPPORT_GROUP)))

    # Offtopic
    dp.add_handler(
        CommandHandler("support", move_to_support, Filters.chat(config.OFFTOPIC_GROUP))
    )

    # Control
    dp.add_handler(
        CommandHandler(
            "clear",
            clear,
            Filters.chat(config.CONTROL_GROUP) & Filters.user(config.ADMINS),
        )
    )

    dp.add_handler(
        CommandHandler(
            "reset",
            reset,
            Filters.chat(config.CONTROL_GROUP) & Filters.user(config.ADMINS),
        )
    )

    # Private
    dp.add_handler(MessageHandler(Filters.chat_type.private, private_not_available))

    # Crap
    dp.add_handler(CommandHandler("banana", banana))
    dp.add_handler(CommandHandler("realistic", realistic))

    # Commands have to be added above
    # dp.add_error_handler(error)  # comment this one out for full stacktrace

    updater.start_webhook(
        "0.0.0.0",
        config.PORT,
        config.TOKEN,
        webhook_url=f"https://ptb-realme.herokuapp.com/{config.TOKEN}",
    )
    updater.idle()
