import time

from telegram import InlineKeyboardMarkup, InlineKeyboardButton, ParseMode, Update
from telegram.ext import CallbackContext


##########################################
# feel free to ignore this file.
# it only contains some functions to simplify the rest of the code a bit.
##########################################

def message_button_url(update: Update, context: CallbackContext, text, button_text, button_url):
    if update.message.reply_to_message:
        return update.message.reply_to_message.reply_text(
            text,
            ParseMode.HTML,
            reply_markup=InlineKeyboardMarkup.from_button(
                InlineKeyboardButton(button_text, button_url)))

    return context.bot.send_message(update.message.chat_id,
                                    text,
                                    ParseMode.HTML,
                                    reply_markup=InlineKeyboardMarkup.from_button(
                                        InlineKeyboardButton(button_text, button_url)))


def message_html(update: Update, context: CallbackContext, text):
    if update.message.reply_to_message:
        return update.message.reply_to_message.reply_text(
            text,
            ParseMode.HTML)

    return context.bot.send_message(
        update.message.chat_id,
        text,
        ParseMode.HTML)


def delay_group_button_url(update: Update, context: CallbackContext, text: str, button_text, button_url):
    update.message.delete()

    reply_message = message_button_url(update, context, text, button_text, button_url)
    context.job_queue.run_once(delete, 600, update.message.chat_id, str(reply_message.message_id))


# check if some messages should migrate to it
def delay_group_preview(update: Update, context: CallbackContext, text: str):
    update.message.delete()

    if update.message.reply_to_message:
        update.message.reply_to_message.reply_text(text, ParseMode.HTML)
    else:
        reply_message = context.bot.send_message(update.message.chat_id, text, ParseMode.HTML)
        context.job_queue.run_once(delete, 600, reply_message.chat_id, str(reply_message.message_id))


def delay_group(update: Update, context: CallbackContext, text: str):
    update.message.delete()

    if update.message.reply_to_message:
        update.message.reply_to_message.reply_text(text, ParseMode.HTML, True)
    else:
        reply_message = context.bot.send_message(update.message.chat_id, text, ParseMode.HTML, True)
        context.job_queue.run_once(delete, 600, reply_message.chat_id, str(reply_message.message_id))


def delay_group_quote(update: Update, context: CallbackContext, text: str):
    update.message.delete()

    if update.message.reply_to_message:
        update.message.reply_to_message.reply_text(text.format(update.message.reply_to_message.from_user.name),
                                                   ParseMode.HTML, True)
    else:
        reply_message = context.bot.send_message(update.message.chat_id, text.format(update.message.from_user.name),
                                                 ParseMode.HTML, True)
        context.job_queue.run_once(delete, 600, reply_message.chat_id, str(reply_message.message_id))


def delete(context: CallbackContext):
    context.bot.delete_message(str(context.job.context), context.job.name)


def remove_message(update: Update, _: CallbackContext):
    if update.message is not None:
        update.message.delete()


def now():
    return int(round(time.time() * 1000))
