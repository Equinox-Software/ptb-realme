"""
This file contains the actions that will happen once a command is called.
These are messages that can appear in both groups or in private.
"""

import re
import time

from telegram import Update, ParseMode, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import CallbackContext

from config import VERIFIED_USERS, CONTROL_GROUP, OFFTOPIC_GROUP, SUPPORT_GROUP, ADMINS
from constants import PHONES, TABLETS, DEVICES, WARNINGS
from utils import delay_group, now, message_button_url, delay_html, check_admin_quote, get_user_info, set_user_info, \
    check_quote, check_admin_quote_not_admin


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
    delay_html(update, context, "cool")


def rules(update: Update, context: CallbackContext):
    """Handle for /rules."""
    if update.message.chat_id == OFFTOPIC_GROUP:
        delay_html(update, context, "otrules")

    elif update.message.chat_id == SUPPORT_GROUP:
        delay_html(update, context, "onrules")

    else:
        update.message.delete()


def resolve_model(update: Update, context: CallbackContext):
    """Handle for resolving a device model from message texts."""

    model = str(re.search(r"rm[xp]\d{4}", update.message.text, re.IGNORECASE).group(0)).upper()

    device_type = model[0:3]

    if device_type == "RMX":
        devices = PHONES
    elif device_type == "RMP":
        devices = TABLETS
    else:
        update.message.reply_text(f"Sorry. The model <b>{model}</b> is invalid.")
        return

    model_number = int(model[3:7])

    if model_number in devices:

        result: list = devices.get(model_number)

        if len(result) > 1:
            text = f"Depending on the region there's multiple devices known as <b>{model}</b>.\n"

            for device_entry in result:
                text += f"\n· Realme {device_entry}"

        else:
            text = f"The mentioned model <b>{model}</b> corresponds to the <b>Realme {result[0]}</b>."

        if (
                update.message.reply_to_message
                and update.message.from_user.id in VERIFIED_USERS
        ):

            if len(update.message.text) == 7:
                update.message.delete()

            update.message.reply_to_message.reply_text(
                f"Hey {update.message.reply_to_message.from_user.name} 🤖\n\n{text}")

        else:
            update.message.reply_text(text)

    else:
        context.bot.send_message(
            CONTROL_GROUP,
            f"#TODO - from user: {update.message.from_user.name}\n\nAdd model <b>{model}</b> to list of devices‼️"
        )

        update.message.reply_text(
            f"Sorry {update.message.from_user.name} 🤖\n\nA device with model <b>{model}</b> does not exist in this Bot's database!\n\nPlease quote this "
            f"message and tell me what this device is supposed to be called like.\n\nThe Maintainers of this "
            f"Community-Bot will verify it and add it to the Bot soon - tap /about for more 😊"
        )


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


def banana(update: Update, _: CallbackContext):
    """Handle for /banana."""
    if check_quote(update):
        update.message.reply_to_message.reply_photo(
            open("resources/where_update.png", "rb")
        )


def realistic(update: Update, context: CallbackContext):
    """Handle for /realistic."""
    delay_html(update, context, "realistic")


def polls(update: Update, context: CallbackContext):
    """Handle for /polls."""
    update.message.delete()
    current_time = now()

    previous_timestamp = context.bot_data.get("previous_timestamp", current_time)
    previous_link = context.bot_data.get(
        "previous_link", "https://t.me/realme_support/263211"
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
    if check_admin_quote(update):
        if len(context.args) == 0:

            user_devices = get_user_info(update, context, DEVICES)

            # TODO: maybe deprecate it in favor of /info
            if user_devices is None:
                update.message.reply_to_message.reply_text(
                    "This user has no devices saved."
                )

            else:
                result = "This user has the following devices: \n"

                result += "· ".join(user_devices)

                update.message.reply_to_message.reply_text(result)

        else:
            set_user_info(update, context, DEVICES, context.args)


def about(update: Update, context: CallbackContext):
    """Handle for /about."""
    delay_html(update, context, "about")


def warn(update: Update, context: CallbackContext):
    if check_admin_quote_not_admin(update):
        warnings = get_user_info(update, context, WARNINGS) + 1

        if warnings <= 3:
            set_user_info(update, context, warnings, WARNINGS)
        else:
            warnings = 'maximum'

        update.message.reply_to_message.reply_text(f"This user has {warnings} warnings.")


def unwarn(update: Update, context: CallbackContext):
    if check_admin_quote_not_admin(update):
        warnings = get_user_info(update, context, WARNINGS) - 1

        if warnings >= 1:
            set_user_info(update, context, warnings, WARNINGS)
        else:
            warnings = 'no'

        update.message.reply_to_message.reply_text(f"This user has {warnings} warnings.")


def ban(update: Update, context: CallbackContext):
    if check_admin_quote_not_admin(update):
        update.message.reply_to_message.reply_text("Banning will be implemented later ;)")


def info(update: Update, context: CallbackContext):
    if check_admin_quote(update):
        info_dict = get_user_info(update, context)

        if len(info_dict) == 0:
            update.message.reply_to_message.reply_text("There is no information for this user saved.")
            return

        response = f"Information about this user:\n\n"

        if DEVICES in info_dict:
            response += "Devices:\n"

            for d in info_dict[DEVICES]:
                response += f"\n· {d}"

            response += "\n"

        if WARNINGS in info_dict:
            response += "Warnings: "

            if info_dict[WARNINGS] == 0:
                response += "None"
            else:
                response += str(info_dict[WARNINGS])

        # maybe also add user's region?

        update.message.reply_to_message.reply_text(response)
