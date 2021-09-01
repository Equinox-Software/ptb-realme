from telegram import ReplyKeyboardMarkup, KeyboardButtonPollType, KeyboardButton, Update, InlineKeyboardMarkup, \
    InlineKeyboardButton, Message
from telegram.ext import CallbackContext

from config import SUPPORT_GROUP, ADMINS
from utils import message_button_url, delay_group

BAN = "BanUser"
WARN = "WarnUser"


##########################################
# These messages are meant to be sent in off-topic group (@realme_offtopic) only.
##########################################

def warn(update: Update, context: CallbackContext):
    if update.message.reply_to_message:
        update.message.reply_to_message.reply_text(
            "This user has currently 3 warnings.", reply_markup=ReplyKeyboardMarkup(
                [
                    [KeyboardButton("Create Quiz", request_poll=KeyboardButtonPollType("quiz"))],
                    [KeyboardButton("Create Poll", request_poll=KeyboardButtonPollType("regular"))]
                ],
                resize_keyboard=True,
                one_time_keyboard=True,
                selective=True)
        )

    else:
        update.message.delete()


def button_click(update: Update, context: CallbackContext):
    query = update.callback_query

    query.answer()

    choice = query.data

    if WARN in choice:
        update.message.reply_text("Choose how long to remove this user:" + choice)

    elif BAN in choice:
        update.message.reply_text("Choose how long to remove this user:" + choice)

    elif choice == "BAN_1h":
        context.bot.send_message(chat_id=update.message.chat_id, text="choice: " + choice)


def remove_click(update: Update, context: CallbackContext):
    query = update.callback_query
    msg: Message = query.data[1]

    msg.delete()

    if msg.from_user.id in ADMINS:
        query.answer()

        context.bot.send_message(msg.chat_id,
                                 "you're verified TEST::: " + str(query.data.reply_to_message.from_user.username))

    else:
        query.answer("You're not an Admin.")


def ban(update: Update, context: CallbackContext):
    if update.message.reply_to_message:

        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("1 hour (test)", callback_data="BAN_1h")],
            [InlineKeyboardButton("1 day", callback_data="BAN_1d")],
            [InlineKeyboardButton("remove", callback_data=("BAN_remove", update.message.reply_to_message))]
        ])

        update.message.reply_to_message.reply_text("Choose how long to remove this user:", reply_markup=keyboard)

    else:
        update.message.delete()


def move_to_support(update: Update, context: CallbackContext):
    if update.message.reply_to_message is not None and update.message.from_user.id in ADMINS:
        update.message.delete()
        original_msg = update.message.reply_to_message.copy(SUPPORT_GROUP, reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton(text="Original Message ➡️",
                                   url=update.message.reply_to_message.link)]]))

        moved_link = "https://t.me/realme_support/" + str(original_msg.message_id)

        message_button_url(update, context,
                           "Hey {} 🤖"
                           "\n\nThose things belong in the Support-Group."
                           "\n\nI moved the message to @realme_support"
                           "\n\nPlease continue the discussion there."
                           .format(update.message.reply_to_message.from_user.name)
                           , "Continue here 😉", moved_link)

    else:
        delay_group(update, context,
                    "Hey guys 🤖"
                    "\n\nIf you need any support regarding your Realme device, please join @realme_support")
