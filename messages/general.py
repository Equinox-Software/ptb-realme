"""
This file contains the actions that will happen once a command is called.
These are messages that can appear in both groups or in private.
"""

import re
import time

from telegram import Update, ParseMode, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import CallbackContext

from config import VERIFIED_USERS, CONTROL_GROUP, OFFTOPIC_GROUP, SUPPORT_GROUP, ADMINS
from constants import PHONES, TABLETS
from utils import delay_group, now, message_button_url, delay_html


def private_not_available(update: Update, _: CallbackContext):
    """Handle private message."""
    update.message.reply_text(
        "My commands work in @realme_support only."
        "\nYou can submit some Feedback here though."
        "\n\nDo you like me? Is there any missing feature?"
        "\n\nPlease tell me 🤖"
    )


def cool(update: Update, context: CallbackContext):
    """Handle for /cool."""
    delay_group(update, context, open("strings/cool.html").read())


def rules(update: Update, context: CallbackContext):
    """Handle for /rules."""
    if update.message.chat_id == OFFTOPIC_GROUP:
        delay_group(update, context, open("strings/otrules.html").read())

    elif update.message.chat_id == SUPPORT_GROUP:
        delay_group(update, context, open("strings/onrules.html").read())

    else:
        update.message.delete()


def rmx(update: Update, context: CallbackContext):
    """Handle for /rmx."""

    model = int(
        str(re.search(r"rmx\d{4}", update.message.text, re.IGNORECASE).group(0))[3:7]
    )

    if model in PHONES:

        result: list = PHONES.get(model)

        if len(result) > 1:
            text = "\n\nDepending on the region there's multiple devices known as RMX{}:\n".format(
                model
            )

            for device in result:
                text += "\n· realme {}".format(device)

        else:
            text = "\n\nThe phone you mentioned is the <b>realme {}</b>.".format(
                result[0]
            )

        if (
                update.message.reply_to_message
                and update.message.from_user.id in VERIFIED_USERS
        ):

            if len(update.message.text) == 7:
                update.message.delete()

            update.message.reply_to_message.reply_text(
                "Hey {} 🤖".format(update.message.reply_to_message.from_user.name) + text)

        else:
            update.message.reply_text(text)

    else:
        context.bot.send_message(
            CONTROL_GROUP,
            "#TODO - from user: {}"
            "\n\nAdd RMX {} to list of devices‼️".format(
                update.message.from_user.name, model
            )
        )

        update.message.reply_text(
            "Sorry {} 🤖"
            "\n\nModel <b>RMX{}</b> was not found."
            "\n\nMy human will add it later 😊".format(
                update.message.from_user.name, model
            )
        )


def rmp(update: Update, context: CallbackContext):
    """Handle for /rmp."""

    model = int(
        str(re.search(r"rmp\d{4}", update.message.text, re.IGNORECASE).group(0))[3:7]
    )

    if model in TABLETS:

        result: list = TABLETS.get(
            model
        )  # will leave it as a list.. who knows what Realme may do in the future lel

        if len(result) > 1:
            text = "\n\nDepending on the region there's multiple devices known as RMP{}:\n".format(
                model
            )

            for device in result:
                text += "\n· realme {}".format(device)

        else:
            text = "\n\nThe phone you mentioned is the <b>realme {}</b>.".format(
                result[0]
            )

        if (
                update.message.reply_to_message
                and update.message.from_user.id in VERIFIED_USERS
        ):

            if len(update.message.text) == 7:
                update.message.delete()

            update.message.reply_to_message.reply_text(
                "Hey {} 🤖".format(update.message.reply_to_message.from_user.name) + text)

        else:
            update.message.reply_text(text)

    else:
        context.bot.send_message(
            CONTROL_GROUP,
            "#TODO - from user: {}"
            "\n\nAdd RMP {} to list of devices‼️".format(
                update.message.from_user.name, model
            ),
        )

        update.message.reply_text(
            "Sorry {} 🤖"
            "\n\nModel <b>RMP{}</b> was not found."
            "\n\nMy human will add it later 😊".format(
                update.message.from_user.name, model
            ))


def benchmark(update: Update, context: CallbackContext):
    """Handle for /benchmark."""
    # TODO save those apps to channel

    text = open("strings/benchmark.html").read()
    norm_text = """Hey {} 🤖\n{}"""
    veri_text = (
        "Hey {} 🤖\n"
        "Pretty cool that you got the latest Update!"
        "\nBefore you update to a newer version, please do "
        "some benchmarks first to be able to compare what "
        "the update really changed in terms of performance."
        "\n{}"
    )
    if (
            update.message.reply_to_message
            and update.message.from_user.id in VERIFIED_USERS
    ):
        delay_group(
            update,
            context,
            veri_text.format(update.message.reply_to_message.from_user.name, text),
        )

    else:
        delay_group(
            update, context, norm_text.format(update.message.from_user.name, text)
        )


def admin(update: Update, context: CallbackContext):
    """Handle for /admin."""
    update.message.delete()

    if update.message.reply_to_message:
        keyboard = InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("1 hour (test)", callback_data="BAN_1h")],
                [InlineKeyboardButton("1 day", callback_data="BAN_1d")],
                [InlineKeyboardButton("remove", callback_data="BAN_remove")],
            ]
        )

        update.message.reply_to_message.reply_text(
            "Choose how long to remove this user:", reply_markup=keyboard
        )


def banana(update: Update, _: CallbackContext):
    """Handle for /banana."""
    update.message.delete()

    if update.message.reply_to_message is not None:
        update.message.reply_to_message.reply_photo(
            open("resources/where_update.png", "rb")
        )


def realistic(update: Update, _: CallbackContext):
    """Handle for /realistic."""
    update.message.delete()

    if update.message.reply_to_message is not None:
        update.message.reply_to_message.reply_text(
            open("strings/realistic.html").read()
        )


def polls(update: Update, context: CallbackContext):
    """Handle for /polls."""
    update.message.delete()
    current_time = now()

    previous_timestamp = context.bot_data.get("previous_timestamp", current_time)
    previous_link = context.bot_data.get(
        "previous_link", "https://t.me/realme_support/135222"
    )

    if (
            update.message.from_user.id in ADMINS
            and int(previous_timestamp) + 3628800000 <= current_time
    ):
        start_message = context.bot.send_message(
            SUPPORT_GROUP,
            "Hey Realme Fans!"
            "\n\n<b>It's once again time for Poll-Five 🖐️</b> "
            "\n\nThis idea came up in @realme_offtopic a few days ago and I "
            "immediately implemented it. It could just be interesting to see what "
            "the community thinks about certain topics. "
            "\n\nCredits go to all the ones who brought up the following "
            "questions. "
            "\n\nHope you enjoy it!",
            ParseMode.HTML,
            reply_markup=InlineKeyboardMarkup.from_button(
                InlineKeyboardButton("📊 Previous Poll 📊", previous_link)
            ),
        )

        context.bot_data["previous_link"] = start_message.link
        context.bot_data["previous_timestamp"] = current_time

        question_0 = "How old are you? 🎂"
        answers_0 = [
            "below 15",
            "15-18",
            "19-21",
            "22-26",
            "27-32",
            "33-37",
            "38-45",
            "46-53",
            "54-62",
            "older than 63",
        ]

        question_1 = "How old is your current phone? 📱"
        answers_1 = [
            "3 months",
            "6 months",
            "9 months",
            "1 year",
            "1.5 years",
            "2 years",
            "2.5 years",
            "3 years",
            "3.5 years",
            "4 years or older",
        ]

        question_2 = "How much money would you spend on a good value phone? 💰"
        answers_2 = [
            "80-120$",
            "121-150$",
            "151-200$",
            "201-250$",
            "251-300$",
            "301-350$",
            "351-420$",
            "421-500$",
            "501-650$",
            "more than 650$",
        ]

        question_3 = "How many different phones have you owned over the last 5 years? 🎁"
        answers_3 = ["1", "2", "3", "4", "more than 4"]

        question_4 = "What's the most important thing when buying a brandnew phone? 🔥"
        answers_4 = [
            "Camera",
            "Display",
            "Audio",
            "Haptics/Design",
            "Storage space",
            "Connectivity",
            "Multitasking capability/Ram",
            "Processing power",
            "Battery/Endurance",
            "Durability/Protection",
        ]

        questions = [question_0, question_1, question_2, question_3]
        answers = [answers_0, answers_1, answers_2, answers_3]

        for i in range(4):
            context.bot.send_poll(
                SUPPORT_GROUP,
                "[Poll {} of 5] · {}".format(i + 1, questions[i]),
                answers[i],
            )
            time.sleep(1)

        context.bot.send_poll(
            SUPPORT_GROUP,
            "[Poll 5 of 5] · {}".format(question_4),
            answers_4,
            allows_multiple_answers=True,
        )

        start_message.pin()

    else:
        print("--- sending poll message")

        message_button_url(
            update,
            context,
            "<b>Poll-Five</b> 🖐️"
            "\n\nThis idea came up in @realme_offtopic. We thought it could just be "
            "interesting to see what the community thinks about certain topics. "
            "\n\nCredits go to all the ones who brought up the questions.",
            "📊 Current Poll 📊",
            previous_link,
        )


def device(update: Update, context: CallbackContext):
    """Handle for /device."""
    update.message.delete()

    if (
            update.message.from_user.id in ADMINS
            and update.message.reply_to_message is not None
    ):

        if len(context.args) == 0:

            if len(context.bot_data[update.message.reply_to_message.from_user.id]) == 0:
                update.message.reply_to_message.reply_text(
                    "This user has no devices saved."
                )

            else:
                result = "This user has the following devices: \n"

                result += "· ".join(
                    context.bot_data[update.message.reply_to_message.from_user.id]
                )

                update.message.reply_to_message.reply_text(result)

        else:
            context.bot_data[update.message.reply_to_message.from_user.id] = context.args


def about(update: Update, context: CallbackContext):
    """Handle for /about."""
    delay_html(update, context, "about")
