from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ParseMode
from telegram.ext import CallbackContext

from config import ADMINS, OFFTOPIC_GROUP
from utils import delay_group, message_button_url, delete, delay_group_quote, delay_group_button_url, \
    delay_group_preview


##########################################
# These messages are meant to be sent in support group (@realme_support) only.
##########################################

def admins(update: Update, context: CallbackContext):
    delay_group(update, context,
                "<u>Group's staff</u>"
                "\n\n<b>Organization</b>"
                "\n@aakaah00001"
                "\n@Prashant_Choudhary"
                "\n@PacificPC"
                "\n\n<b>Moderators</b>"
                "\n@darkphoenix_6969"
                "\n@blue_beettle69")


def ask(update: Update, context: CallbackContext):
    delay_group(update, context,
                "<u>How to ask</u>"
                "\n\n<b>1. Formulate the question</b>"
                "\nMake sure to include:"
                "\n· The device you use"
                "\n· The latest software installed"
                "\n· What you want to do"
                "\n· What you have tried already"
                "\n· Why you want to do that"
                "\n· What benefits you expected"
                "\n· The output you got"
                "\n\n<b>2. Wait for a response</b>"
                "\nGive the community 48h to answer your question. The needed expert might not be available all the "
                "time, so receiving an answer might take a bit. "
                "\n\n<b>3. No answer yet</b>"
                "\nUse /experts and tag the experts, whose segment fits your issue."
                "\nIf you didn't receive an answer after a week, use /form and fill out the linked form."
                "\n\nThese suggestions enable us to provide you with better answers quicker and will keep this chat "
                "more focused.")


def commands(update: Update, context: CallbackContext):
    delay_group(update, context,
                "<u>My Commands</u>"
                "\n\n<i>Please note that I delete my responses after 10 minutes to keep this chat clear. If you quote "
                "another message and then use a command, the response will stay.</i>"
                "\n\n<b>/help</b>"
                "\nDisplay this message"
                "\n\n<b>/admins</b>"
                "\nShow this group\'s staff"
                "\n\n<b>/rules</b>"
                "\nShow this group\'s rules"
                "\n\n<b>/experts</b>"
                "\nList experts for different segments"
                "\n\n<b>/gcam</b>"
                "\nLatest GCam release and configurations"
                "\n\n<b>/cleaners</b>"
                "\nCleaners to keep your storage free and more"
                "\n\n<b>/bug</b>"
                "\nHow to report a bug or give feedback about RUI2.0"
                "\n\n<b>/stable</b>"
                "\nHow to estimate the stable release date"
                "\n\n<b>/push</b>"
                "\nHow long it takes for an update to arrive on your device after it got pushed."
                "\n\n<b>/debloat</b>"
                "\nHow to remove unwanted Apps"
                "\n\n<b>/android11</b>"
                "\nOfficial roadmap for the Early Access of RealmeUI 2.0"
                "\n\n<b>/battery</b>"
                "\nTips to keep your battery healthy"
                "\n\n<b>/ask</b>"
                "\nHow to ask questions properly"
                "\n\n<b>rmx{modelnumber}</b>"
                "\nGet the device to a supplied model number, eg. <code>rmx1931</code> (can also be part of a message "
                "and is case-insensitive) "
                "\n\npersonal opinion:"
                "\n/rant - quality over quantitiy"
                "\n/ram - virtual ram is not amazing"
                "\n\n\n\n<b>Who am I?</b>"
                "\n\nI'm a bot with purpose is to answer frequently asked questions and help the admins doing their "
                "job. "
                "\n\nOh.. I'm open source by the way: <a href='https://github.com/PXNX/ptb-realme'>Github</a> 💗"
                "\n\nPlease join @realme_offtopic to suggest new features or improvements."
                "\n\nMessage @nyx69, if you face any issues with me 🤖")


def experts(update: Update, context: CallbackContext):
    delay_group(update, context,
                "<u>Community experts</u>"
                "\n\n<b>Software issues</b>"
                "\n@NoobOf2021"
                "\n\n<b>Hardware issues</b>"
                "\n- no expert yet -"
                "\n\n<b>Updates and apps</b>"
                "\n@NoobOf2021"
                "\n\n<b>Phone recommendations</b>"
                "\n@pentexnyx"
                "\n\n<b>Flashing</b>"
                "\n- no expert yet -"
                "\n\n<b>Android development</b>"
                "\n@pentexnyx"
                "\n\n<b>Realme ecosystem</b>"
                "\n- no expert yet -"
                "\n\nIf you want to be listed here, please join @realme_offtopic and ask for it. We'll then decide "
                "whether you're worthy.")


def gcam(update: Update, context: CallbackContext):
    delay_group(update, context,
                "<u>Google Camera</u>"
                "\n\n<b>Releases</b>"
                "\nPXv8.1_GCam · <a href='https://t.me/realme_offtopic/4177'>1.2 ⬇️ </a>"
                "\n\nUrnyx05 · <a href='https://t.me/realme_offtopic/4176'>2.5 ⬇️ </a>"
                "\n\n\nUrnyx05's releases work well on most Realme devices. Take a look at @googlecameraport "
                "for other releases. "
                "\n\n\n<b>Configurations</b>"
                "\nTaken from <a href='https://www.celsoazevedo.com/files/android/google-camera/f/configs"
                "-urnyx-02/'>Urnyx05's page</a>. These configurations are optimized for a specific device, "
                "but may work for other devices aswell. Just give them a try 😊 "
                "\n\n· <a href='https://t.me/realme_support/113610'>Realme 5 & 5 Pro</a>"
                "\n· <a href='https://t.me/realme_support/113612'>Realme X2 Pro</a>"
                "\n· <a href='https://t.me/realme_support/113614'>Realme X50 & X50 Pro</a>"
                "\n· <a href='https://t.me/realme_support/113616'>Realme 6 & 6 Pro</a>"
                "\n\nTo enable these configurations, place them in <b>Internal Storage > GCam > Configs7</b>."
                "\n\nThen go to your GCam and press on the bottom left (next to the camera switch button) a "
                "few times. A dialog should appear where your can select the desired configuration. "
                "\n\nFeel free to fiddle around with LibPatcher (in GCam's settings) a little to shape the "
                "image output so that it fits your needs.")


def cleaners(update: Update, context: CallbackContext):
    delay_group(update, context,
                "<u>Cleaners</u>"
                "\n\n<b>SD Maid</b> · <a href='https://t.me/realme_offtopic/8103'>5.1.6 ⬇️</a>"
                "\nThis is an excellent cleaning app, which also takes care of databases, duplicates, "
                "caches etc. and enables you to freeze the apps you don't need. Oh yes.. and it's open-source 💗"
                "\n\n<b>Phone Manager</b> · <a href='https://t.me/realme_support/126160'>8.6.1 ⬇️</a>"
                "\nOfficial Cleaner by Realme (requires Android 11).")


def aod(update: Update, context: CallbackContext):
    delay_group_quote(update, context,
                      "Hey {} 🤖"
                      "\n\n<u>Always-On-Display</u>"
                      "\n\n<i>Be aware that the upcoming paragraphs are simplified and won't go over the actual "
                      "complexity behind those subjects.</i>"
                      "\n\n\n<b>Why don't I have an Always-On-Display?</b>"
                      "\n\nIf your device has an LCD, AODs are pointless as the backlight of the LCD will be "
                      "on - no matter what's been shown on screen."
                      "\n\nAODs make more sense on an AMOLED, where individual pixels can turn off entirely, "
                      "thus saving battery. "
                      "\n\n\n<b>Why can't I customize my AOD?</b>"
                      "\n\nThis is due to something that's often referred to as a \"ram-less display\", meaning that "
                      "your display only uses the device's Ram, which limits its capabilities a bit. "
                      "This isn't something bad at all. It's just the conventional way displays are made."
                      "\n\nYour phone's display quite likely simply doesn't support this additional feature. "
                      "Currently it's only working on the GT, GT Neo, X50 Pro, X2, X2 Pro, X, XT and X7 Max.")


def manual(update: Update, context: CallbackContext):
    delay_group(update, context,
                "<u>Updating System-Apps manually</u>"
                "\n\nUpdating your System-Apps via Apks you find somewhere on the Internet or here on Telegram "
                "is often pointless, as you quite likely have the latest proper and optimized version of these "
                "Apps installed on your device anyway. "
                "\n\nYou should therefore not really be in need of flashing them manually. "
                "\n\n⚠️ Installing these Apps yourself may actually be worse, as those files are very "
                "often not explicitly for your device and may therefore lack specific optimization or may not "
                "even work as they should. "
                "\n\nBe very careful with what you install. It's better to wait for the next automatic "
                "software-update 😉")


def form(update: Update, context: CallbackContext):
    delay_group_button_url(update, context,
                           "If your issue is not resolved by the community after a week, you can also contact the "
                           "developers."
                           "\n\nWe Admins collect those entries and will forward them to the developers."
                           "\n\nPlease don't abuse this possibility, so that Realme developers can focus on developing.",
                           "Access form 📝",
                           "https://docs.google.com/forms/d/e/1FAIpQLSceGI9ZaNOIb4NN-3UdJ-mbzvbRwulAh2"
                           "-VGJasy8VU_BLsFA/viewform")


def bug(update: Update, context: CallbackContext):
    delay_group(update, context,
                "<u>Bug report</u>\n\n"
                "<i>If you face an issue that is clearly a bug and can't be resolved by the community after some time, "
                "you can also let the developers know. Don't abuse this functionality, so that the devs can focus on "
                "developing.</i> "
                "\n\nPlease provide as much useful information as possible."
                "\n\nJust go to your dialer and dial <code>*#800#</code> in."
                "\n\nAlternatively you can also do that in the feedback section of the toolkit app.")


def battery(update: Update, context: CallbackContext):
    delay_group_quote(update, context,
                      "Hey {} 🤖"
                      "\n\n<b>Some tips for a healthy battery 🔋</b>"
                      "\n\n1. Maintain a charge between 20 and 85%"
                      "\n\n2. Give at least 15 minutes break before and after charging"
                      "\n\n3. Restart your device every 3 days"
                      "\n\n4. Don't play on higher settings")


def stable(update: Update, context: CallbackContext):
    delay_group_quote(update, context,
                      "Hey {} 🤖"
                      "\n\n<i>Realme rolls out an Update, if it works as expected - not if a certain date is met. "
                      "Therefore an exact date for when you will receive an update doesn't exist.</i> "
                      "\n\n<b>Estimating the stable release date</b>"
                      "\nUse /android11 and add a minimum of 6 months after the Early Access date. This is the "
                      "timeframe developers currently need to go from Beta to Stable. "
                      "\n\nDevelopers are working very hard currently, but it may still take some time. Please stand "
                      "by.")


def push(update: Update, context: CallbackContext):
    delay_group_quote(update, context,
                      "Don't worry {} 🤖"
                      "\n\nTo ensure the stability of updates, they have staged rollouts."
                      "\n\nThe update will be randomly pushed to a small number of users first."
                      "\n\nIf no critical bugs appear within the next days, the full rollout begins.")


def ram(update: Update, context: CallbackContext):
    delay_group(update, context,
                "<u>Virtual Ram</u>"
                "\n\n<i>This is based on personal experience by @nyx69</i>"
                "\n\nAs 2GB of Ram are not much, I tested a comparable principle on my J7 2016 with even less Ram."
                "\n\nIt worked, but the performance increase was barely noticeable. It created a swap-file on my "
                "storage, which is not as blazing fast as Ram."
                "\n\nThe current Realme devices come with UFS2.0 storage, some even UFS3.1, and more processing power."
                "\n\nFor Virtual Ram I only expect a very slight performance increase, so please don't hype it up "
                "that much 😉")


def rant(update: Update, context: CallbackContext):
    delay_group(update, context, "<b>A bird in the hand is worth two in the bush 🕊️</b>"
                                 "\n\n<i>A small rant by me, @nyx69 (I made this bot by the way). The following is "
                                 "not affiliated with Realme. These are my own personal thoughts as a developer for a "
                                 "rather big German company myself.</i> "
                                 "\n\n\nActually it's better to not have some actual date. So that Realme can release "
                                 "things, if they meet their requirements."
                                 "\n\nTake Cyberpunk for instance. They had to release an unfinished crap full of "
                                 "bugs, because moving the release date yet another time would have caused big "
                                 "trouble with investors and public."
                                 "\n\n\nAdditionally, just too many members of this group don't seem to understand the "
                                 "concept of announcements and plans. All the dates given are estimates, "
                                 "not exact ones at all. I'll therefore dive a bit deeper in the following paragraphs."
                                 "\n\nRealme's few developers are working very hard to bring out updates and fixes "
                                 "for all these devices they threw on the market. Obviously those updates we see take "
                                 "some time and testing. They won't just do all that in five minutes straight. "
                                 "\n\nTheir developers focus on important things for the company itself as mentioned "
                                 "already. Especially as Realme has a very limited capacity when it comes to "
                                 "developers. So simply wait as those minor fixes aren't a huge game changer anyway."
                                 "\n\n\nI get it. You pay the company for a device and you already own this device. "
                                 "The company itself offers free updates as a bonus on top of that. The have to earn "
                                 "more money from advertising those updates and selling devices than what maintenance "
                                 "and development costs. "
                                 "\n\nTherefore it's better for them to pack a few updates together and release them "
                                 "all at once rather than doing every single bit and piece individually. A company "
                                 "will always act in a way that they profit as much as possible. That's just natural. "
                                 "That's how economy works. "
                                 "\n\nCrying, shouting, anger and whatsoever won't bring any benefit into this game. "
                                 "So it's better to just relax and focus on the actually important things in life. "
                                 "Those minor improvements are not worth all the panic you tend to create. You won't "
                                 "die just because you receive something rather unimportant a few more days later. "
                                 "\n\nThanks for reading ☺️")


def whatsapp(update: Update, context: CallbackContext):
    update.message.delete()

    text = "You can contact the official support directly on WhatsApp:" \
           "\n\n+919711012312 🆕"

    button_text = "Message Support 💬"
    button_url = "https://wa.me/+919711012312"

    if update.message.reply_to_message:
        update.message.reply_to_message.reply_text(
            "Hey {} 🤖\n\n".format(update.message.reply_to_message.from_user.name) + text,
            ParseMode.HTML,
            reply_markup=InlineKeyboardMarkup.from_button(
                InlineKeyboardButton(button_text, button_url)))
    else:
        reply_message = context.bot.send_message(update.message.chat_id,
                                                 text,
                                                 ParseMode.HTML,
                                                 reply_markup=InlineKeyboardMarkup.from_button(
                                                     InlineKeyboardButton(button_text, button_url)))
        context.job_queue.run_once(delete, 600, reply_message.chat_id, str(reply_message.message_id))


def move_to_offtopic(update: Update, context: CallbackContext):
    if update.message.reply_to_message and update.message.from_user in ADMINS:
        update.message.delete()
        original_msg = update.message.reply_to_message.copy(OFFTOPIC_GROUP, reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton(text="Original Message ➡️",
                                   url=update.message.reply_to_message.link)]]))

        moved_link = "https://t.me/realme_offtopic/" + str(original_msg.message_id)

        message_button_url(update, context,
                           "Hey {} 🤖"
                           "\n\nThis is getting pretty off-topic now."
                           "\n\nI moved the message to @realme_offtopic"
                           "\n\nPlease continue the discussion there."
                           .format(update.message.reply_to_message.from_user.name)
                           , "Continue here 😉", moved_link)

    else:
        delay_group(update, context,
                    "Hey guys 🤖"
                    "\n\nFeel free to join @realme_offtopic to discuss topics not related to Realme or Android."
                    "\n\nYou can also send Links and Stickers there 🥳")


def android11(update: Update, context: CallbackContext):
    delay_group_preview(update, context,
                        "<u>Realme UI 2.0</u>"
                        "\n\n<i>Early Access is there to test stuff. Testing is easier with a reduced userbase. "
                        "Therefore it will be rolled out to a limited number of people only 😉</i> "
                        "\n\n· <a href='https://static.c.realme.com/IN/wm-thread/1374937652238790656.png'>Current "
                        "Roadmap</a> "
                        "\n\n· <a href='https://static.c.realme.com/IN/wm-thread/1369542731847704576.jpg'>Previous "
                        "Roadmap</a> "
                        "\n\n<b>Early Access</b>"
                        "\nThe timeline is for the first wave of early access rollout only. The version for the "
                        "corresponding model will be released within the above mentioned month in batches, "
                        "not at the beginning of the month. "
                        "\n\n<b>Stable release</b>"
                        "\nWill be pushed to all users over a period of time, a few months after early access."
                        "\n\nRelax and wait what happens 😎")


def debloat(update: Update, context: CallbackContext):
    delay_group(update, context,
                "<u>Debloat</u>"
                "<i>\n\nThere's two major ways of having a device debloated: flashing a debloated Rom or rooting your "
                "device and uninstalling things yourself. These methods void your warranty and can be risky!</i> "
                "\n\nIf you just want some free space or block apps from running, try /cleaners"
                "\n\n\n<b>The alternative solution</b>"
                "\n\n1. Install ADB on your Computer"
                "\n<a href='https://www.xda-developers.com/install-adb-windows-macos-linux/'>XDA's Guide</a> "
                "\n\n2. Enable USB-Debugging on your device, plug your phone into the Computer"
                "\n\n3. Open the command prompt and type in <code>adb shell</code> and then <code>adb devices</code> "
                "and make sure yours is listed there. "
                "\n\n<b>Make sure you know exactly what Application you want to remove! Some are required by the "
                "system and might make it unstable or result in a crash.</b>"
                "\n\n4. To uninstall apps type in <code>pm uninstall -k --user 0 PACKAGE-NAME</code> - for example: "
                "<code>pm uninstall -k --user 0 com.facebook.katana</code>")
