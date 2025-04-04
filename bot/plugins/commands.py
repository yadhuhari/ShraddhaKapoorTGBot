from pyrogram import filters, Client, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram.errors import UserNotParticipant
import random

from bot import Translation, LOGGER # pylint: disable=import-error
from bot.database import Database # pylint: disable=import-error

db = Database()

force_channel = "MalluXLinkzz"

PICS = [
 "http://postimg.cc/5HK6dFb2"
]

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
                text="Sᴏʀʀy Dᴜᴅᴇ Yᴏᴜ'ʀᴇ Nᴏᴛ Jᴏɪɴᴇᴅ My Cʜᴀɴɴᴇʟ 😐. Sᴏ Pʟᴇᴀꜱᴇ Jᴏɪɴ Oᴜʀ Uᴩᴅᴀᴛᴇ Cʜᴀɴɴᴇʟ Tᴏ Cᴄᴏɴᴛɪɴᴜᴇ",
                reply_markup=InlineKeyboardMarkup( [[
                 InlineKeyboardButton("🔊 𝗝𝗼𝗶𝗻 𝗢𝘂𝗿 𝗠𝗮𝗶𝗻 𝗰𝗵𝗮𝗻𝗻𝗲𝗹", url=f"t.me/{force_channel}")
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
        caption = f"""<code> {file_name} </code>
       
<b> ✨ Jᴏɪɴ Nᴏᴡ [Mallu Linkzz ✨](t.me/MalluXLinkzz) </b>"""
        
        try:
            await update.reply_cached_media(
                file_id,
                quote=True,
                caption = caption,
                thumb="http://postimg.cc/DJW3LD97",
                parse_mode=enums.ParseMode.HTML,
                reply_markup=InlineKeyboardMarkup(
                        [[
                            InlineKeyboardButton('𝖩𝗈𝗂𝗇 𝖿𝗈𝗋 𝖬𝗈𝗏𝗂𝖾𝗌 🌀', url="https://t.me/MalluXLinkzz")
                        ]]
                ))
        except Exception as e:
            await update.reply_text(f"<b>Error:</b>\n<code>{e}</code>", True, parse_mode=enums.ParseMode.HTML)
            LOGGER(__name__).error(e)
        return
    await update.reply_photo(
        photo=random.choice(PICS),
        caption=f"""
<b> Hᴇʏ ᴛʜᴇʀᴇ {update.from_user.first_name} 👋,
    
Mʏ Nᴀᴍᴇ Is [Rᴀsʜᴍɪᴋᴀ Mᴀɴᴅᴀɴɴᴀ ✨](t.me/MalluRashmikaRobot)

I Aᴍ ᴀ Mᴏᴠɪᴇ Pʀᴏᴠɪᴅɪɴɢ Mᴀᴄʜɪɴᴇ Fᴏʀ [Mᴀʟʟᴜ Lɪɴᴋᴢᴢ Gʀᴏᴜᴘs](t.me/MalluXLinkzz), Oɴʟʏ Aᴜᴛʜᴏʀɪᴢᴇᴅ Aᴅᴍɪɴs Cᴀɴ Usᴇ Mᴇ Sᴏ Dᴏɴ'ᴛ Wᴀsᴛᴇ Yᴏᴜʀ Tɪᴍᴇ 😁 

Mᴀɪɴᴛᴀɪɴᴇᴅ Bʏ :- @MR_TONY_99 </b>""",
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton("Uᴘᴅᴀᴛᴇs Cʜᴀɴɴᴇʟ ✨", url="t.me/MalluXLinkzz"),
            ],[
            InlineKeyboardButton("Hᴇʟᴘ ⚙️", callback_data="help"),
            InlineKeyboardButton("Aʙᴏᴜᴛ 🤠", callback_data="about"),
            ],[
            InlineKeyboardButton("Dᴇᴠᴇʟᴏᴘᴇʀ 💀", url="t.me/MR_TONY_99")
            ]]
            ),
        parse_mode=enums.ParseMode.HTML,
        reply_to_message_id=update.id
    )


@Client.on_message(filters.command(["help"]), group=1)
async def help(bot, update):
    buttons = [[
            InlineKeyboardButton('🏡 Hᴏᴍᴇ', callback_data='start'),
            InlineKeyboardButton('Aʙᴏᴜᴛ 🖥', callback_data='about')
        ],[
            InlineKeyboardButton('⛔ Cʟᴏsᴇ', callback_data='close')
        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await update.reply_photo(
        photo=random.choice(PICS),
        caption=f"""
<b> Hᴇʏ 👋,

Sᴇᴇ Yᴏᴜ Iɴ [Mᴀʟʟᴜ Lɪɴᴋᴢᴢ](t.me/MalluXLinkzz) കുട്ടാ..😁 </b>
""",
        reply_markup=reply_markup,
        parse_mode=enums.ParseMode.HTML,
        reply_to_message_id=update.id
    )


@Client.on_message(filters.command(["about"]) & filters.private, group=1)
async def about(bot, update):
    
    buttons = [[
            InlineKeyboardButton('👨‍💻 𝖣𝖾𝗏𝖾𝗅𝗈𝗉𝖾𝗋', url='https://t.me/MR_TONY_99')
        ], [
            InlineKeyboardButton('🏡ʜᴏᴍᴇ', callback_data='start'),
            InlineKeyboardButton('ʙᴀᴄᴋ👈', callback_data='start')
        ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await update.reply_photo(
        photo=random.choice(PICS),
        caption=f"""<b>
✯ Mʏ Nᴀᴍᴇ : [Rᴀsʜᴍɪᴋᴀ Mᴀɴᴅᴀɴɴᴀ ✨](t.me/MalluRashmikaRobot)
✯ Dᴇᴠᴇʟᴏᴘᴇʀ : [Tᴏɴʏ Sᴛᴀʀᴋ](t.me/MR_TONY_99)
✯ Lᴀɴɢᴜᴀɢᴇ : [Pʏᴛʜᴏɴ 3.13.0](www.python.org)
✯ Lɪʙʀᴀʀʏ : [Pʏʀᴏɢʀᴀᴍ](https://docs.pyrogram.org/)
✯ Sᴇʀᴠᴇʀ : [Sᴏᴍᴇᴡʜᴇʀᴇ](www.goandlearn.com)
✯ Dᴀᴛᴀʙᴀsᴇ : [Mᴏɴɢᴏ DB](www.mongodb.com) </b>""",
        reply_markup=reply_markup,
        parse_mode=enums.ParseMode.HTML,
        reply_to_message_id=update.id
    )
