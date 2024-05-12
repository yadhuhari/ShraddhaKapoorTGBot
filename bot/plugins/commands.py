from pyrogram import filters, Client, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram.errors import UserNotParticipant
import random

from bot import Translation, LOGGER # pylint: disable=import-error
from bot.database import Database # pylint: disable=import-error

db = Database()

force_channel = "CC_LinkzzTG"

PICS = [
 "https://telegra.ph/file/aa3ad8175457f8100aae9.jpg",
 "https://telegra.ph/file/4097b118f1d4bc42c3132.jpg",
 "https://telegra.ph/file/60722fcd75b589584c300.jpg"
]

ADMINS = "6979830303"

@Client.on_message(filters.command(["start"]) & filters.private, group=1)
async def start(bot, update):
    if force_channel:
        try:
            user = await bot.get_chat_member(force_channel, update.from_user.id)
            if user.status == "kicked out":
                await update.reply_text("You Are Banned")
                return
        except UserNotParticipant :
            await update.reply_text(
                text="🔊 𝗝𝗼𝗶𝗻 𝗢𝘂𝗿 𝗠𝗮𝗶𝗻 𝗰𝗵𝗮𝗻𝗻𝗲𝗹 🤭.\n\nനിങ്ങൾക്ക് മൂവീസ് വേണോ? എങ്കിൽ തായെ കാണുന്ന ഞങ്ങളുടെ മെയിൻ ചാനലിൽ ജോയിൻ ചെയ്യുക.😂\nഎന്നിട്ട് ഗ്രൂപ്പിൽ പോയി വീണ്ടും മൂവിയിൽ ക്ലിക് ചെയ്ത് start കൊടുത്തു നോക്കൂ..!😁",
                reply_markup=InlineKeyboardMarkup( [[
                 InlineKeyboardButton("🔊 𝗝𝗼𝗶𝗻 𝗢𝘂𝗿 𝗠𝗮𝗶𝗻 𝗰𝗵𝗮𝗻𝗻𝗲𝗹 🤭", url=f"t.me/{force_channel}")
                 ]]
                 )
            )
            return
   
    try:
        file_uid = update.command[1]
    except IndexError:
        file_uid = False
    
    if file_uid:
        file_id, file_name, file_caption, file_type, file_size = await db.get_file(file_uid)
        
        if (file_id or file_type) == None:
            return
     #CUSTOM FILE CAPTION   
        caption = f""" 📂 <em>File Name</em>: <code>HRZ TG | {file_name} </code> \n\n🖇 <em>File Size</em>: <code> {file_size} </code>"""
        
        try:
            await update.reply_cached_media(
                file_id,
                quote=True,
                caption = caption,
                parse_mode=enums.ParseMode.HTML,
                reply_markup=InlineKeyboardMarkup(
                        [[
                            InlineKeyboardButton('𝖩𝗈𝗂𝗇 𝖿𝗈𝗋 𝖬𝗈𝗏𝗂𝖾𝗌 🌀', url="https://t.me/CCGroupOfficial")
                        ]]
                ))
        except Exception as e:
            await update.reply_text(f"<b>Error:</b>\n<code>{e}</code>", True, parse_mode=enums.ParseMode.HTML)
            LOGGER(__name__).error(e)
        return
    await update.reply_photo(
        photo=random.choice(PICS),
        caption=Translation.START_TEXT.format(update.from_user.first_name),
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton("𝖠𝖽𝖽 𝗆𝖾 𝗍𝗈 𝗒𝗈𝗎𝗋 𝖦𝗋𝗈𝗎𝗉 🎗", url="http://t.me/CCResmiBot?startgroup=true"),
            ],[
            InlineKeyboardButton("👨‍💻 𝖣𝖾𝗏𝖾𝗅𝗈𝗉𝖾𝗋", url="t.me/MR_HKZ_TG"),
            InlineKeyboardButton("𝖩𝗈𝗂𝗇 𝖿𝗈𝗋 𝖬𝗈𝗏𝗂𝖾𝗌 🌀", url="https://t.me/CCGroupOfficial"),
            ],[
            InlineKeyboardButton("𝖠𝖻𝗈𝗎𝗍 🤠", callback_data="about")
            ]]
            ),
        parse_mode=enums.ParseMode.HTML,
        reply_to_message_id=update.id
    )


@Client.on_message(filters.command(["help"]) & filters.user(ADMINS), group=1)
async def help(bot, update):
    buttons = [[
            InlineKeyboardButton('🏡ʜᴏᴍᴇ', callback_data='start'),
            InlineKeyboardButton('Aʙᴏᴜᴛ🖥', callback_data='about')
        ],[
            InlineKeyboardButton('🔐ᴄʟᴏsᴇ', callback_data='close')
        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await update.reply_photo(
        photo=random.choice(PICS),
        caption=Translation.HELP_TEXT,
        reply_markup=reply_markup,
        parse_mode=enums.ParseMode.HTML,
        reply_to_message_id=update.id
    )


@Client.on_message(filters.command(["about"]) & filters.private, group=1)
async def about(bot, update):
    
    buttons = [[
            InlineKeyboardButton('👨‍💻 𝖣𝖾𝗏𝖾𝗅𝗈𝗉𝖾𝗋', url='https://t.me/MR_HKZ_TG')
        ], [
            InlineKeyboardButton('🏡ʜᴏᴍᴇ', callback_data='start'),
            InlineKeyboardButton('ʙᴀᴄᴋ👈', callback_data='start')
        ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await update.reply_photo(
        photo=random.choice(PICS),
        caption=Translation.ABOUT_TEXT,
        reply_markup=reply_markup,
        parse_mode=enums.ParseMode.HTML,
        reply_to_message_id=update.id
    )
