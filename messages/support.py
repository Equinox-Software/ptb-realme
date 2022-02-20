"""These messages are meant to be sent in support group (@realme_support) only."""

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ParseMode
from telegram.ext import CallbackContext

from config import ADMINS, OFFTOPIC_GROUP
from utils import (
    delay_group,
    message_button_url,
    delete,
    delay_group_quote,
    delay_group_button_url,
    delay_group_preview, delay_html,
)


def ask(update: Update, context: CallbackContext):
    """Handle for /ask."""
    delay_group(update, context, open("strings/ask.html").read())


def commands(update: Update, context: CallbackContext):
    """Handle for /commands."""
    delay_group(update, context, open("strings/commands.html").read())


def gcam(update: Update, context: CallbackContext):
    """Handle for /gcam."""
    delay_group(update, context, open("strings/gcam.html").read())


def cleaners(update: Update, context: CallbackContext):
    """Handle for /cleaners."""
    delay_group(update, context, open("strings/cleaners.html").read())


def aod(update: Update, context: CallbackContext):
    """Handle for /aod."""
    delay_group_quote(update, context, open("strings/aod.html").read())


def manual(update: Update, context: CallbackContext):
    """Handle for /manual."""
    delay_group(update, context, open("strings/manual.html").read())


def apk(update: Update, context: CallbackContext):
    """Handle for /apk."""
    delay_group_quote(update, context, open("strings/apk.html").read())


def form(update: Update, context: CallbackContext):
    """Handle for /form."""
    delay_group_button_url(update, context, open("strings/form.html").read(), button_text="Access form 📝",
                           button_url="https://docs.google.com/forms/d/e/1FAIpQLSceGI9ZaNOIb4NN-3UdJ-mbzvbRwulAh2-VGJasy8VU_BLsFA/viewform")


def bug(update: Update, context: CallbackContext):
    """Handle for /bug."""
    delay_group(update, context, open("strings/bug.html").read())


def battery(update: Update, context: CallbackContext):
    """Handle for /battery."""
    delay_group_quote(update, context, open("strings/battery.html").read())


def stable(update: Update, context: CallbackContext):
    """Handle for /stable."""
    delay_group_quote(update, context, open("strings/stable.html").read())


def push(update: Update, context: CallbackContext):
    """Handle for /push."""
    delay_group_quote(update, context, open("strings/push.html").read())


def ram(update: Update, context: CallbackContext):
    """Handle for /ram."""
    delay_group(update, context, open("strings/ram.html").read())


def rant(update: Update, context: CallbackContext):
    """Handle for /rant."""
    delay_group(update, context, open("strings/ram.html").read())


def whatsapp(update: Update, context: CallbackContext):
    """Handle for /whatsapp."""
    update.message.delete()

    text = (
        "You can contact the official support directly on WhatsApp:"
        "\n\n+919711012312 🆕"
    )

    button_text = "Message Support 💬"
    button_url = "https://wa.me/+919711012312"

    if update.message.reply_to_message:
        update.message.reply_to_message.reply_text(
            "Hey {} 🤖\n\n".format(update.message.reply_to_message.from_user.name)
            + text,
            ParseMode.HTML,
            reply_markup=InlineKeyboardMarkup.from_button(
                InlineKeyboardButton(button_text, button_url)
            ),
        )
    else:
        reply_message = context.bot.send_message(
            update.message.chat_id,
            text,
            ParseMode.HTML,
            reply_markup=InlineKeyboardMarkup.from_button(
                InlineKeyboardButton(button_text, button_url)
            ),
        )
        context.job_queue.run_once(
            delete, 600, reply_message.chat_id, str(reply_message.message_id)
        )


def move_to_offtopic(update: Update, context: CallbackContext):
    """Handle for move to offtopic."""
    if (
            update.message.reply_to_message is not None
            and update.message.from_user.id in ADMINS
    ):
        update.message.delete()
        original_msg = update.message.reply_to_message.copy(
            OFFTOPIC_GROUP,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="Original Message ➡️",
                            url=update.message.reply_to_message.link
                        )
                    ]
                ]
            ),
        )

        moved_link = "https://t.me/realme_offtopic/" + str(original_msg.message_id)

        message_button_url(
            update,
            context,
            "Hey {} 🤖"
            "\n\nThis is getting pretty off-topic now."
            "\n\nI moved the message to @realme_offtopic"
            "\n\nPlease continue the discussion there.".format(
                update.message.reply_to_message.from_user.name
            ),
            "Continue here 😉",
            moved_link
        )

    else:
        delay_group(
            update,
            context,
            "Hey guys 🤖"
            "\n\nFeel free to join @realme_offtopic to discuss topics "
            "not related to Realme or Android."
            "\n\nYou can also send Links and Stickers there 🥳"
        )


def android11(update: Update, context: CallbackContext):
    """Handle for /android11."""
    delay_group_preview(update, context, open("strings/android11.html").read())


def android12(update: Update, context: CallbackContext):
    """Handle for /android12."""
    # what about Italian and French roadmap?
    delay_group_preview(update, context, open("strings/android12.html").read())


def debloat(update: Update, context: CallbackContext):
    """Handle for /debloat."""
    delay_group(update, context, open("strings/debloat.html").read())


def fps(update: Update, context: CallbackContext):
    """Handle for /fps."""
    delay_group(update, context, open("strings/fps.html").read())


def fooview(update: Update, context: CallbackContext):
    """Handle for /fooview."""
    delay_group(update, context, open("strings/fooview.html").read())


def swap(update: Update, context: CallbackContext):
    """Handle for /swap."""
    delay_group(update, context, open("strings/swap.html").read())


def charge(update: Update, context: CallbackContext):
    """Handle for /charge."""
    delay_group(update, context, open("strings/charge.html").read())


def miss(update: Update, context: CallbackContext):
    """Handle for /miss."""
    delay_html(update, context, "miss")
