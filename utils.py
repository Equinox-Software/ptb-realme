"""
Feel free to ignore this file.

It only contains some functions to simplify the rest of the code a bit.
"""

import time

from telegram import InlineKeyboardMarkup, InlineKeyboardButton, ParseMode, Update
from telegram.ext import CallbackContext

from config import ADMINS
from constants import WARNINGS, DEVICES


def message_button_url(
        update: Update, context: CallbackContext, text, button_text, button_url
):
    """Send a message with URL."""
    if update.message.reply_to_message:
        return update.message.reply_to_message.reply_text(
            text,
            reply_markup=InlineKeyboardMarkup.from_button(
                InlineKeyboardButton(button_text, button_url)
            ),
        )

    return context.bot.send_message(
        update.message.chat_id,
        text,
        reply_markup=InlineKeyboardMarkup.from_button(
            InlineKeyboardButton(button_text, button_url)
        ),
    )


def delay_group_button_url(
        update: Update, context: CallbackContext, text: str, button_text, button_url
):
    """Send a delayed message to group with URL."""
    update.message.delete()

    reply_message = message_button_url(update, context, text, button_text, button_url)
    context.job_queue.run_once(
        delete, 600, update.message.chat_id, str(reply_message.message_id)
    )


def delay_group_preview(update: Update, context: CallbackContext, text: str):
    """Send a delayed message with preview."""
    update.message.delete()

    if update.message.reply_to_message:
        update.message.reply_to_message.reply_text(text)
    else:
        reply_message = context.bot.send_message(
            update.message.chat_id, text)
        context.job_queue.run_once(
            delete, 600, reply_message.chat_id, str(reply_message.message_id)
        )


def delay_group(update: Update, context: CallbackContext, text: str):
    """Send a delayed message to group."""
    update.message.delete()

    if update.message.reply_to_message:
        update.message.reply_to_message.reply_text(text, disable_web_page_preview=True)
    else:
        reply_message = context.bot.send_message(
            update.message.chat_id, text, disable_web_page_preview=True
        )
        context.job_queue.run_once(
            delete, 600, reply_message.chat_id, str(reply_message.message_id)
        )


def delay_group_quote(update: Update, context: CallbackContext, text: str):
    """Send a delayed quoted message."""
    update.message.delete()

    if update.message.reply_to_message:
        update.message.reply_to_message.reply_text(
            text.format(update.message.reply_to_message.from_user.name),
            ParseMode.HTML,
            True,
        )
    else:
        reply_message = context.bot.send_message(
            update.message.chat_id,
            text.format(update.message.from_user.name),
            ParseMode.HTML,
            True,
        )
        context.job_queue.run_once(
            delete, 600, reply_message.chat_id, str(reply_message.message_id)
        )


def delay_html(update: Update, context: CallbackContext, path: str):
    if update.message.reply_to_message is not None and update.message.reply_to_message.from_user.name != "Telegram":
        delay_group(update, context, f"Hey {update.message.reply_to_message.from_user.name} 🤖\n\n" + open(
            f"strings/{path}.html").read())
        return

    delay_group(update, context, open(f"strings/{path}.html").read())


def delete(context: CallbackContext):
    """Delete given message from job."""
    context.bot.delete_message(str(context.job.context), context.job.name)


def remove_message(update: Update, _: CallbackContext):
    """Remove the message."""
    if update.message is not None:
        update.message.delete()


def now():
    """Return current timestamp."""
    return int(round(time.time() * 1000))


def check_admin_quote(update: Update) -> bool:
    update.message.delete()

    return update.message.from_user.id in ADMINS and update.message.reply_to_message is not None


def check_quote(update: Update) -> bool:
    update.message.delete()

    return update.message.reply_to_message is not None


def get_user_info(update: Update, context: CallbackContext, key: str = None) -> any:
    info = context.bot_data.get(update.message.reply_to_message.from_user.id, {WARNINGS: 0, DEVICES: []})

    if key is None:
        return info

    return info.get(key)


def set_user_info(update: Update, context: CallbackContext, value: any, key: str = None):
    if key is None:
        context.bot_data[update.message.reply_to_message.from_user.id, {WARNINGS: 0, DEVICES: []}] = value
    else:
        context.bot_data.get(update.message.reply_to_message.from_user.id, {WARNINGS: 0, DEVICES: []})[key] = value
