import asyncio
import random

from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.enums import ChatType

from config import STICKER, FSUB, IMG
from ChatBot import app
from ChatBot.database import add_user, add_chat, get_fsub


@app.on_message(filters.command("start") & ~filters.bot)
async def start(client, m: Message):
    if FSUB and not await get_fsub(client, m):
        return

    bot_name = app.name

    if m.chat.type == ChatType.PRIVATE:
        user_id = m.from_user.id
        await add_user(user_id, m.from_user.username or None)

        if STICKER and isinstance(STICKER, list):
            sticker_to_send = random.choice(STICKER)
            umm = await m.reply_sticker(sticker=sticker_to_send)
            await asyncio.sleep(2)
            await umm.delete()

        await m.reply_photo(
            photo=random.choice(IMG),
            caption=f"""
<b>Hey {m.from_user.mention}. 💖</b>  

Welcome to <b>{bot_name}</b>. ✨  
I'm here to chat, vibe, and bring some fun to your day.  

💌 Add me to your group for even more excitement.  
""",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton(text="ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ", url=f"https://t.me/{app.username}?startgroup=true")],
                [
                    InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ", url="https://t.me/CodeSearchDev"),
                    InlineKeyboardButton(text="sᴜᴘᴘᴏʀᴛ", url="https://t.me/ChatWithDevRobot")
                ],
                [InlineKeyboardButton(text="ᴍʏ ᴄᴏᴍᴍᴀɴᴅs", callback_data="help")]
            ])
        )
    elif m.chat.type in {ChatType.GROUP, ChatType.SUPERGROUP}:
        chat_id = m.chat.id
        await add_chat(chat_id, m.chat.title)
        await m.reply_text(f"Hey {m.from_user.mention}, I’m {bot_name}, here to keep the energy high. Use /help to see what I can do!")

@app.on_chat_member_updated()
async def chat_updates(client, m):
    """
    When the bot is added to a new group, store its data in the database.
    If the bot is removed from the group, delete its data from the database.
    """
    bot_id = (await client.get_me()).id

    if m.new_chat_member and m.new_chat_member.user.id == bot_id:
        chat_id = m.chat.id
        await add_chat(chat_id, m.chat.title)

    elif m.old_chat_member and m.old_chat_member.user.id == bot_id and not m.new_chat_member:
        chat_id = m.chat.id
        await remove_chat(chat_id)

@app.on_message(filters.command("help") & filters.group)
async def help(client, m: Message):
    await m.reply(
        "Need help? Click below to see all my commands.",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("📜 ᴄᴏᴍᴍᴀɴᴅs ᴀɴᴅ ɢᴜɪᴅᴇ", url="http://t.me/MissAaru_Robot?start=help")]
        ])
    )


@app.on_callback_query()
async def callback(client, query: CallbackQuery):
    bot_name = app.name

    if query.data == "start":
        if query.message.chat.type == ChatType.PRIVATE:
            new_text = f"""
<b>Hey {query.from_user.mention}. 💖</b>  

Welcome to <b>{bot_name}</b>. ✨  
I'm here to chat, vibe, and bring some fun to your day.  

💌 Add me to your group for even more excitement.  
"""

            if query.message.text != new_text:
                await query.message.edit_text(
                    new_text,
                    reply_markup=InlineKeyboardMarkup([
                        [InlineKeyboardButton(text="ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ", url="https://t.me/MissAaru_Robot?startgroup=true")],
                        [
                            InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ", url="https://t.me/CodeSearchDev"),
                            InlineKeyboardButton(text="sᴜᴘᴘᴏʀᴛ", url="https://t.me/ChatWithDevRobot")
                        ],
                        [InlineKeyboardButton(text="ᴍʏ ᴄᴏᴍᴍᴀɴᴅs", callback_data="help")]
                    ])
                )

    elif query.data == "help":
        if query.message.chat.type == ChatType.PRIVATE:
            help_message = f"""
❖ Available Commands.

⬤ /start ➥ Start me.  
⬤ /ping ➥ Check if I'm online.  
⬤ /stats ➥ Get chat stats.  
⬤ /chatbot ➥ Toggle AI replies (only works in groups).

Stay sharp, stay awesome. ✨  
"""

            if query.message.text != help_message:
                await query.message.edit_text(
                    help_message,
                    reply_markup=InlineKeyboardMarkup([
                        [
                            InlineKeyboardButton(text="ʙᴀᴄᴋ", callback_data="start"),
                            InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ", url="https://t.me/CodeSearchDev")
                        ]
                    ])
                )