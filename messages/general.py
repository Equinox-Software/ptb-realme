import re
import time

from telegram import Update, ParseMode, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import CallbackContext

from config import VERIFIED_USERS, CONTROL_GROUP
from constants import MODELS
from main import SUPPORT_GROUP, OFFTOPIC_GROUP, ADMINS
from utils import delay_group, now, message_button_url


##########################################
# This file contains the actions that will happen once a command is called.
# These are messages that can appear in both groups or in private.
##########################################

def private_not_available(update: Update, _: CallbackContext):
    update.message.reply_text(
        "My commands work in @realme_support only."
        "\nYou can submit some Feedback here though."
        "\n\nDo you like me? Is there any missing feature?"
        "\n\nPlease tell me 🤖")


def cool(update: Update, context: CallbackContext):
    delay_group(update, context,
                "<u>Cool and useful Apps</u>"
                "\n\n<b>Moment Pro</b> · <a href='https://t.me/realme_offtopic/5344'>3.2.2 ⬇️</a>"
                "\nSolid camera for professionals."
                "\n\n<b>Aida64</b> · <a href='https://t.me/realme_offtopic/9346'>179 ⬇️</a>"
                "\nAll the data about your device."
                "\n\n<b>Videoder</b> · <a href='https://t.me/realme_offtopic/12457'>14.4.2 ⬇️</a>"
                "\nDownload videos and music from YouTube or any other website."
                "\n\nMore at /gcam and /cleaners.")


def rules(update: Update, context: CallbackContext):
    if update.message.chat_id == OFFTOPIC_GROUP:
        delay_group(update, context,
                    "<u>Group's rules</u>"
                    "\n\n<i>Off-topic, but not chaotic 😉</i>"
                    "\n\n<b>1. Language</b>"
                    "\nPlease use English only. Staff is not affected by this rule."
                    "\n\n<b>2. Respect</b>"
                    "\nWe're all one big community. Don't be rude."
                    "\n\n<b>3. Spam</b>"
                    "\nAvoid sending stuff multiple times. Flooding the chat won't give you more attention."
                    "\n\n<b>4. Content</b>"
                    "\nGore, porn and anything alike is absolutely prohibited. Also be aware that this group is no "
                    "support group. "
                    "\n\n<b>5. Privacy</b>"
                    "\nPlease contact members of this group only if they explicitly permit it. Staff does not require "
                    "to ask for permission.")

    else:
        delay_group(update, context,
                    "<u>Group's rules</u>"
                    "\n\n<b>1. Language</b>"
                    "\nPlease use English whenever possible or Hindi as an alternative."
                    "\n\n<b>2. Links</b>"
                    "\nSending links is not permitted and will get you banned for a day to avoid scammers."
                    "\n\n<b>3. Forwarding</b>"
                    "\nForwarding messages from other channels is not permitted."
                    "\n\n<b>4. Respect</b>"
                    "\nWe're all one big community. Don't be rude."
                    "\n\n<b>5. Spam</b>"
                    "\nAvoid sending stuff multiple times. Flooding the chat won't give you more attention."
                    "\n\n<b>6. Files</b>"
                    "\nAvoid sending files over 50Mb, if not ultimately needed."
                    "\n\n<b>7. Advertisements</b>"
                    "\nSelf-promotion is not permitted."
                    "\n\n<b>8. Content</b>"
                    "\nGore, porn and anything alike is absolutely prohibited."
                    "\n\n<b>9. Privacy</b>"
                    "\nPlease contact members of this group only if they explicitly permit it. Staff does not require "
                    "to ask for permission.")


def rmx(update: Update, context: CallbackContext):
    # will do extra /device to display device info

    model = int(str(re.search(r"rmx\d{4}", update.message.text, re.IGNORECASE).group(0))[3:7])

    if model in MODELS:

        result: list = MODELS.get(model)

        if len(result) > 1:
            text = "\n\nDepending on the region there's multiple devices known as RMX{}:\n".format(model)

            for device in result:
                text += "\n· realme {}".format(device)

        else:
            text = "\n\nThe phone you mentioned is the <b>realme {}</b>.".format(result[0])

        if update.message.reply_to_message and update.message.from_user.id in VERIFIED_USERS:
            update.message.delete()
            update.message.reply_to_message.reply_text(
                "Hey {} 🤖".format(update.message.reply_to_message.from_user.name) + text,
                parse_mode=ParseMode.HTML)

        else:
            update.message.reply_text(text, parse_mode=ParseMode.HTML)

    else:
        context.bot.send_message(CONTROL_GROUP, "#TODO - from user: {}"
                                                "\n\nAdd RMX {} to list of devices‼️"
                                 .format(update.message.from_user.name, model))

        update.message.reply_text("Sorry {} 🤖"
                                  "\n\nModel <b>RMX{}</b> was not found."
                                  "\n\nMy human will add it later 😊".format(update.message.from_user.name, model),
                                  parse_mode=ParseMode.HTML)


def benchmark(update: Update, context: CallbackContext):
    # TODO save those apps to channel
    text = "\n\n<b>Benchmark your device 💪</b>" \
           "\n\nFor reference we're using two different benchmarks to compare devices in this group. Please install " \
           "them via the below links. " \
           "\n\n· CPU Performance:\n<a href='https://play.google.com/store/apps/details?id=com.primatelabs.geekbench5" \
           "'>Geekbench 5 ⬇️</a> " \
           "\n\n· Gaming Performance:\n<a href='https://play.google.com/store/apps/details?id=com.futuremark" \
           ".dmandroid.application'>3DMark (Wild Life) ⬇️</a> " \
           "\n\n\nNow open them and see if they need anything downloaded first. After that switch your phone to " \
           "maximum performance: " \
           "\n\n· Disable any energy saving option that's currently active." \
           "\n\n· Set your phone to performance mode." \
           "\n\n· Close all open Apps via your launchers 'clear all' button" \
           "\n\n· Set your phone to airplane mode." \
           "\n\nLet your phone run Geekbench first and take a screenshot of the score at the end." \
           "\n\n\nRepeat this process three more times. Also take screenshots after each run. This is to test " \
           "sustained performance. (#TODO might add heat check app here) " \
           "\n\n\nClose all applications again, let your device cool down for a few minutes. Then repeat the process " \
           "for 3DMark (Wild Life). " \
           "\n\n\nOnce you're done with all the screenshots, upload your first and last score of each benchmark (so " \
           "four images in total) as an album in @realme_offtopic and put #Benchmark the Android-Version, for example " \
           "#Android11 and your device model, for example #RMX1931 in the caption of this album. "

    if update.message.reply_to_message and update.message.from_user.id in VERIFIED_USERS:
        delay_group(update, context,
                    "Hey {} 🤖"
                    "\n\nPretty cool that you got the latest Update, huh?"
                    "\n\nBefore you update to a newer version, please do some benchmarks first to be able to compare "
                    "what the update really changed in terms of performance.\n"
                    .format(update.message.reply_to_message.from_user.name) + text)

    else:
        delay_group(update, context,
                    "Hey {} 🤖".format(update.message.from_user.name) + text)


def admin(update: Update, context: CallbackContext):
    update.message.delete()

    if update.message.reply_to_message:
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("1 hour (test)", callback_data="BAN_1h")],
            [InlineKeyboardButton("1 day", callback_data="BAN_1d")],
            [InlineKeyboardButton("remove", callback_data="BAN_remove")]
        ])

        update.message.reply_to_message.reply_text("Choose how long to remove this user:", reply_markup=keyboard)


def polls(update: Update, context: CallbackContext):
    update.message.delete()
    current_time = now()

    previous_timestamp = context.bot_data.get("previous_timestamp", 1000)
    previous_link = context.bot_data.get("previous_link", "https://t.me/realme_support/135222")

    if update.message.from_user.id in ADMINS and int(previous_timestamp) + 3628800000 <= current_time:
        start_message = context.bot.send_message(SUPPORT_GROUP,
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
                                                     InlineKeyboardButton("📊 Previous Poll 📊", previous_link)))

        context.bot_data['previous_link'] = start_message.link
        context.bot_data['previous_timestamp'] = current_time

        question_0 = "How old are you? 🎂"
        answers_0 = ["below 15", "15-18", "19-21", "22-26", "27-32",
                     "33-37", "38-45", "46-53", "54-62", "older than 63"]

        question_1 = "How old is your current phone? 📱"
        answers_1 = ["3 months", "6 months", "9 months", "1 year", "1.5 years",
                     "2 years", "2.5 years", "3 years", "3.5 years", "4 years or older"]

        question_2 = "How much money would you spend on a good value phone? 💰"
        answers_2 = ["80-120$", "121-150$", "151-200$", "201-250$", "251-300$",
                     "301-350$", "351-420$", "421-500$", "501-650$", "more than 650$"]

        question_3 = "How many different phones have you owned over the last 5 years? 🎁"
        answers_3 = ["1", "2", "3", "4", "more than 4"]

        question_4 = "What's the most important thing when buying a brandnew phone? 🔥"
        answers_4 = ["Camera", "Display", "Audio", "Haptics/Design", "Storage space",
                     "Connectivity", "Multitasking capability/Ram", "Processing power", "Battery/Endurance",
                     "Durability/Protection"]

        questions = [question_0, question_1, question_2, question_3]
        answers = [answers_0, answers_1, answers_2, answers_3]

        for i in range(4):
            context.bot.send_poll(SUPPORT_GROUP, "[Poll {} of 5] · {}".format(i + 1, questions[i]), answers[i])
            time.sleep(1)

        context.bot.send_poll(SUPPORT_GROUP, "[Poll 5 of 5] · {}".format(question_4), answers_4,
                              allows_multiple_answers=True)

        start_message.pin()

    else:
        print("--- sending poll message")

        message_button_url(update, context,
                           "<b>Poll-Five</b> 🖐️"
                           "\n\nThis idea came up in @realme_offtopic. We thought it could just be "
                           "interesting to see what the community thinks about certain topics. "
                           "\n\nCredits go to all the ones who brought up the questions.",
                           "📊 Current Poll 📊", previous_link)


def translate(update: Update, context: CallbackContext):
    if update.message.reply_to_message is not None:

        if len(context.args) == 0 or len(context.args) > 2:
            context.bot.send_message(
                update.message.chat_id,
                "Please supply a language-code, for example <code>/translate de</code> to translate from German "
                "to English or <code>/translate en it</code> to translate from English to Italian.", ParseMode.HTML)
        else:
            from_language = context.args[0].lower()

            if len(context.args) == 2:
                to_language = context.args[1].lower()
            else:
                to_language = 'en'  # update.message.from_user.language_code

            if update.message.reply_to_message.caption is not None:
                text_translation = update.message.reply_to_message.caption
            elif update.message.reply_to_message.text is not None:
                text_translation = update.message.reply_to_message.text
            else:
                context.bot.send_message(
                    update.message.chat_id,
                    "The quoted media has no caption. Please quote a text message or a message with caption, "
                    "for example <code>/translate de</code> to translate from German to English or "
                    "<code>/translate en it</code> to translate from English to Italian.", ParseMode.HTML)
                return

            update.message.reply_to_message.reply_text(
                "Translation ({} ➜ {})\n\n{}".format(from_language, to_language, translator.translate(text_translation, src=from_language,dest=to_language)["text"],
                ParseMode.HTML))

    else:
        context.bot.send_message(
            update.message.chat_id,
            "Quote the message you want to translate and the use this command, for example <code>/translate de</code> "
            "to translate from German to English or <code>/translate en it</code> to translate from English to Italian.",
            ParseMode.HTML)