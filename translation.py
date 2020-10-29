from sample_config import Config

class Translation(object):
    START_TEXT = """Hello <b>{}</b>,

This Is A Telegram Rename By {}

I Can Rename ✍ With Custom Thumbnail And Upload As Video/File

Type /help For More Details."""
    RENAME_403_ERR = "Sorry. You Are Not Permitted To Rename This File."
    ABS_TEXT = " Please Don't Be Selfish."
    UPGRADE_TEXT = "There is no upgrade plan till now it will be added in future"
    DOWNLOAD_START_VIDEO = "🔴 Downloading To My Server..."
    DOWNLOAD_START = "🔴 Downloading To My Server..."
    UPLOAD_START_VIDEO = "🟢 Uploading As video..."
    UPLOAD_START = "🟢 Uploading As File..."
    RCHD_TG_API_LIMIT = "Downloaded In {} Seconds.\nDetected File Size: {}\nSorry. But, I Cannot Upload Files Greater Than 1.95GB Due To Telegram API Limitations.I Can't Do Anything For That 🤷‍♂️."
    AFTER_SUCCESSFUL_UPLOAD_MSG = "**❤ Thank You For Using [Amine Soukara](https://t.me/AmineSoukara)'s Bot ❤**"
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "Downloaded In {} Seconds.\nUploaded In {} Seconds."
    NOT_AUTH_USER_TEXT = "Please /Upgrade Your Subscription."
    NOT_AUTH_USER_TEXT_FILE_SIZE = "Detected File Size: {}. Free Users Can Only Upload: {}\nPlease /upgrade Your Subscription.\nIf You Think This Is A Bug, Please Contact <a href='https://t.me/damienHelp'>Damien Help</a>"
    SAVED_CUSTOM_THUMB_NAIL = "Custom File Thumbnail Saved ✅️. This Image Will Be Deleted Within 24hr"
    DEL_ETED_CUSTOM_THUMB_NAIL = "🚫 Custom Thumbnail Cleared Succesfully."
    FF_MPEG_DEL_ETED_CUSTOM_MEDIA = "🚫 Media Cleared Succesfully."
    SAVED_RECVD_DOC_FILE = "✅ Document Downloaded Successfully."
    CUSTOM_CAPTION_UL_FILE = "@DamienSoukara"
    NO_CUSTOM_THUMB_NAIL_FOUND = "⛔ No Custom ThumbNail Found."
    USER_ADDED_TO_DB = "User <a href='tg://user?id={}'>{}</a> Added To {} Till {}."
    HELP_USER = """Hey <b>{}</b>, 

I Am Renamer Bot ✍ By : <a href='https://t.me/{}'>Damien Soukara</a>
    
● Send Me A Thumbnail.

● Send me the file to be Renamed.

● Reply to that message with <code>/rename new name.extension</code>. with custom thumbnail support.\n(upload as file)

● Reply to that message with <code>/rename_vidoe new name.extension</code>. with custom thumbnail support.\n(uploading as Video)

Support Group : @DamienHelp"""
    REPLY_TO_DOC_FOR_RENAME_FILE = "🤦‍♂️ Reply To A Telegram Media To `/rename New Name.extension` with custom thumbnail support.\n\n(For uploading as file).\n\nSee /help for mor information. "
    REPLY_TO_DOC_FOR_RENAME_VIDEO = "🤦‍♂️ Reply To A Telegram Media To `/rename_video New Name.extension` with custom thumbnail support.\n\n(For uploading as video).\n\nSee /help for mor information."
    ABUSIVE_USERS = "You are not allowed to use this bot. If you think this is a mistake, please check /me to remove this restriction."
    FREE_USER_LIMIT_Q_SZE = """Cannot Process.
Free users only 1 request per 30 minutes.
/upgrade or Try 1800 seconds later."""
    IFLONG_FILE_NAME = """File Name limit allowed by Telegram is {alimit} characters.
The given file name has {num} characters.

<b>Essays Not allowed in Telegram file name!</b>
©️ <code>@ReFileRobot</code>
Please short your file name and try again!"""

    About = """Hi {},

**📝 Language:** Python 3

**🧰 Framework:** Pyrogram

**👨‍💻 Developer:** [AmineSoukara](t.me/AmineSoukara)

**📮 Channel:** [DAMIEN BOT UPDATES](https://t.me/DAMIENSOUKARA)

**👥 Group:** [DAMIEN BOT SUPPOTERS](https://t.me/DamienHelp)"""
