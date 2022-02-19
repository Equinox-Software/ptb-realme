"""These messages are meant to be sent in off-topic group (@realme_offtopic) only."""

from telegram import (
    Update,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
from telegram.ext import CallbackContext

from config import SUPPORT_GROUP, ADMINS
from utils import message_button_url, delay_group


def move_to_support(update: Update, context: CallbackContext):
    """Handle to move to support."""
    if (
            update.message.reply_to_message is not None
            and update.message.from_user.id in ADMINS
    ):
        update.message.delete()
        original_msg = update.message.reply_to_message.copy(
            SUPPORT_GROUP,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="Original Message ➡️",
                            url=update.message.reply_to_message.link,
                        )
                    ]
                ]
            ),
        )

        moved_link = "https://t.me/realme_support/" + str(original_msg.message_id)

        message_button_url(
            update,
            context,
            "Hey {} 🤖"
            "\n\nThose things belong in the Support-Group."
            "\n\nI moved the message to @realme_support"
            "\n\nPlease continue the discussion there.".format(
                update.message.reply_to_message.from_user.name
            ),
            "Continue here 😉",
            moved_link,
        )

    else:
        delay_group(
            update,
            context,
            "Hey guys 🤖"
            "\n\nIf you need any support regarding your Realme device, "
            "please join @realme_support",
        )
