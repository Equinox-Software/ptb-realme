from telegram import BotCommandScopeChat, Update, BotCommandScopeChatAdministrators
from telegram.ext import CallbackContext

from config import CONTROL_GROUP, SUPPORT_GROUP, OFFTOPIC_GROUP


##########################################
# These messages are meant to be sent in control group only.
##########################################

def clear(update: Update, context: CallbackContext):
    context.chat_data.clear()  # TODO ask Starry to add that

    context.bot.delete_my_commands(BotCommandScopeChat(SUPPORT_GROUP))
    context.bot.delete_my_commands(BotCommandScopeChat(OFFTOPIC_GROUP))

    context.bot.set_my_commands([
        ('clear', 'Clears commands and temporary user data.'),
        ('reset', 'Resets commands. Use if after clearing.')],
        scope=BotCommandScopeChat(CONTROL_GROUP)
    )

    update.message.reply_text("User dicts and commands were cleared.")


def reset(update: Update, context: CallbackContext):
    context.bot.set_my_commands([
        ('android12', 'Official 3.0 roadmap 📲'),
        ('gcam', 'Latest release and configurations 📷'),
        ('cleaners', 'The recommended cleaning apps ♻️'),
        ('whatsapp', 'Message the support directly 💬'),
        ('bug', 'How to report a bug ⚠️'),
        ('stable', 'Estimate the stable release date 📆'),
        ('push', 'How an update is pushed 🅿️'),
        ('android11', 'Official 2.0 roadmap 📲'),
        ('debloat', 'Guide to remove unwanted apps 🚫'),
        ('battery', 'Keep your battery healthy 🔋'),
        ('polls', 'Take a look at our current polls 📊'),
        ('benchmark', 'How to benchmark your device 💪🏼'),
        ('cool', 'Cool and useful Apps 😎'),
        ('aod', 'Why there is no Customization or AOD 🎨'),
        ('ram', 'Virtual Ram performance 💾'),
        ('manual', 'Manual updates may be worse 😟'),
        ('apk', 'Why an Apk fails to install 🚫'),
        ('rules', 'Show this group\'s rules 📜'),
        ('experts', 'List experts for different segments 🎓'),
        ('admins', 'Show this group\'s staff 👷‍♂️'),
        ('ask', 'How to ask questions properly ❓'),
        ('help', 'Show commands 🆘'), ],
        scope=BotCommandScopeChat(SUPPORT_GROUP))

    context.bot.set_my_commands([
        ('android12', 'Official 3.0 roadmap 📲'),
        ('gcam', 'Latest release and configurations 📷'),
        ('cleaners', 'The recommended cleaning apps ♻️'),
        ('whatsapp', 'Message the support directly 💬'),
        ('bug', 'How to report a bug ⚠️'),
        ('stable', 'Estimate the stable release date 📆'),
        ('push', 'How an update is pushed 🅿️'),
        ('android11', 'Official 2.0 roadmap 📲'),
        ('debloat', 'Guide to remove unwanted apps 🚫'),
        ('battery', 'Keep your battery healthy 🔋'),
        ('polls', 'Take a look at our current polls 📊'),
        ('benchmark', 'How to benchmark your device 💪🏼'),
        ('cool', 'Cool and useful Apps 😎'),
        ('aod', 'Why there is no Customization or AOD 🎨'),
        ('ram', 'Virtual Ram performance 💾'),
        ('manual', 'Manual updates may be worse 😟'),
        ('apk', 'Why an Apk fails to install 🚫'),
        ('rules', 'Show this group\'s rules 📜'),
        ('experts', 'List experts for different segments 🎓'),
        ('admins', 'Show this group\'s staff 👷‍♂️'),
        ('ask', 'How to ask questions properly ❓'),
        ('help', 'Show commands 🆘'),
        ('realistic', 'If people expect to much'),
        ('fps', 'Games are demanding'),
        ('banana', 'Where update?'),
        ('rant', 'Why updates don\'t have dates'),
        ('offtopic', 'Move messages to Off-Topic ➡️')],
        scope=BotCommandScopeChatAdministrators(SUPPORT_GROUP))

    context.bot.set_my_commands([
        ('rules', 'Show this group\'s rules 📜'),
        ('cool', 'Cool and useful Apps 😎'),
        ('gcam', 'Latest release and configurations 📷'),
        ('cleaners', 'The recommended cleaning apps ♻️')],
        scope=BotCommandScopeChat(OFFTOPIC_GROUP))

    context.bot.set_my_commands([
        ('rules', 'Show this group\'s rules 📜'),
        ('cool', 'Cool and useful Apps 😎'),
        ('gcam', 'Latest release and configurations 📷'),
        ('cleaners', 'The recommended cleaning apps ♻️'),
        ('banana', 'Where update?'),
        ('support', 'Move messages to the Support-Group ➡️')],
        scope=BotCommandScopeChatAdministrators(OFFTOPIC_GROUP))

    # add Contribute/About and a specific message to join the groups here
    #  context.bot.set_my_commands([
    #  ('rules', 'Show this group\'s rules 📜')],
    #  scope=BotCommandScope.ALL_PRIVATE_CHATS)

    update.message.reply_text("Command list was updated.")
