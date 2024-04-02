import asyncio
import re
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from mmllm.her import print_id
from pyrogram.enums import ChatType, ChatMemberStatus

@Client.on_message(filters.regex("مرحبا بك"))
async def start_1(client, message):
        await asyncio.sleep(3)
        match = re.search(r'👥] نقاطك : (\d+)', message.text)
        points = int(match.group(1))
        if points >= 200:
            await asyncio.sleep(3)
            await c.request_callback_answer(
                        chat_id=message.chat.id,
                        message_id=message.id,
                        callback_data=message.reply_markup.inline_keyboard[2][1].callback_data
                    )
            await asyncio.sleep(4)
            await message.reply(print_id)
            await asyncio.sleep(1)
            await message.reply(points)
        await client.request_callback_answer(
                    chat_id=message.chat.id,
                    message_id=message.id,
                    callback_data=message.reply_markup.inline_keyboard[1][0].callback_data
                )
@Client.on_edited_message(filters.regex("✳️ تجميع نقاط"))
async def start_2(client, message):                
        await asyncio.sleep(3)                
        await client.request_callback_answer(
                    chat_id=message.chat.id,
                    message_id=message.id,
                    callback_data=message.reply_markup.inline_keyboard[0][0].callback_data
                )
@Client.on_edited_message(filters.regex('اشترك فالقناة'))
async def start_3(client, message): 
    await asyncio.sleep(3)
    ay = ''
    for lin in message.text.split('\n'):
        if '@' in lin:
            ay = lin
            break
    if not ay:
        return
    link = '@' + ay.split('@')[1]
    if ' ' in link:
        link = link.split(' ')[0]
    await client.join_chat(link)
    await asyncio.sleep(0.5)
    try:
        await client.request_callback_answer(
            chat_id=message.chat.id,
            message_id=message.id,
            callback_data=message.reply_markup.inline_keyboard[0][0].callback_data
        )
    except:
        pass
@Client.on_message(filters.regex('يجب عليك الاشتراك بقناة البوت اولاً'))
async def ctc1dbot(c, msg):
    ay = ''
    for lin in msg.text.split('\n'):
        if '@' in lin:
            ay = lin
            break
    if not ay:
        return
    link = '@' + ay.split('@')[1]
    if ' ' in link:
        link = link.split(' ')[0]
    await c.join_chat(link)
@Client.on_edited_message(filters.regex('اختر طريقة التحويل'))
async def prinst(c, m):
    await asyncio.sleep(3) 
    try:
        await c.request_callback_answer(chat_id=m.chat.id,message_id=m.id,callback_data=m.reply_markup.inline_keyboard[0][0].callback_data)
    except:
        pass
@Client.on_message(filters.regex("👤 تم ارسال"))
async def block_and_leave_all(c, msg):
    await c.block_user(msg.chat.id)
    async for dialog in c.get_dialogs():
        if dialog.chat.type != ChatType.PRIVATE:    
            try:
                await c.leave_chat(dialog.chat.id, delete=True)
            except:
                pass

async def auto():
    while not await asyncio.sleep(120):
        await Client.send_message("DamKombot", "/start")

asyncio.create_task(auto())
  