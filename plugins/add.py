from pyrogram import Client, filters
from pyrogram.enums import SentCodeType
from pyrogram.errors import SessionPasswordNeeded
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrolistener import Listener
from mmllm.her import listener
from random import randint
import asyncio
import json

try:
    with open('accounts.json', 'r') as file:
        accounts_data = json.load(file)
except FileNotFoundError:
    accounts_data = []

@Client.on_callback_query(filters.regex("zuue"))
async def zuue(c: Client, m: CallbackQuery):  
    msg = await listener.listen_to(m, "يعممم رقم", filters=["text"])
    phone_number = msg.text
    user = Client(f"user:{randint(1, 9999)}", 27786450, '1fb7b1af2837205d7ce8d77cefc0acbd', device_model="Collect")
    await user.connect()
    code = await user.send_code(phone_number)
    msg = await listener.listen_to(m, "يعممم كود", filters=["text"])
    phone_code = msg.text
    try:
        await user.sign_in(phone_number, code.phone_code_hash, phone_code)
    except SessionPasswordNeeded:
        msg = await listener.listen_to(m, "يعممم باسس", filters=["text"])
        password = msg.text
        try:
            await user.check_password(password)
        except:
            await m.message.reply(f"باس غلط")
    session = await user.export_session_string()
    await user.disconnect()
    await m.message.reply(f"𝐃𝐨𝐧𝐞 {session}✨")
    new_account = {
        "phone_number": phone_number,
        "session": session
    }
    accounts_data.append(new_account)

    with open('accounts.json', 'w') as file:
        json.dump(accounts_data, file)    

@Client.on_callback_query(filters.regex("DamKombot"))
async def DamKombot(c: Client, m: CallbackQuery): 
    await m.message.reply(f"𝐃𝐨𝐧𝐞 ✨")
    try:
        with open('accounts.json', 'r') as file:
            accounts_data = json.load(file)
    except FileNotFoundError:
        await m.message.reply("لم يتم العثور على ملف الحسابات.")
        return

    if not accounts_data:
        await m.message.reply("لا توجد حسابات مخزنة حاليًا.")
        return

    for account in accounts_data:
        try:
            userbot = Client("name_session", session_string=account['session'], api_id=17765175, api_hash="e77878aa96e80375b1272e60f746bbf2",plugins=dict(root="stitch"))  
            try:
                await userbot.start()
                await userbot.send_message("DamKombot", "/start")
            except Exception as e:
                print(e)   
        except Exception as e:
            print(e)

@Client.on_callback_query(filters.regex("delete_account"))
async def delete_account(c: Client, m: CallbackQuery): 
    msg = await listener.listen_to(m, "يعممم رقم", filters=["text"])
    phone_number = msg.text
    try:
        with open('accounts.json', 'r') as file:
            accounts_data = json.load(file)
    except FileNotFoundError:
        await m.message.reply("لم يتم العثور على ملف الحسابات.")
        return

    if not accounts_data:
        await m.message.reply("لا توجد حسابات مخزنة حاليًا.")
        return

    deleted_account = None
    for account in accounts_data:
        if account.get("phone_number") == phone_number:
            deleted_account = account
            accounts_data.remove(account)
            break

    if deleted_account is None:
        await m.message.reply("لم يتم العثور على حساب يحمل هذا الرقم.")
        return

    with open('accounts.json', 'w') as file:
        json.dump(accounts_data, file)

    await m.message.reply(f"تم حذف الحساب رقم {phone_number} بنجاح.")

@Client.on_callback_query(filters.regex("show_accounts"))
async def show_accounts(c: Client, m: CallbackQuery): 
    try:
        with open('accounts.json', 'r') as file:
            accounts_data = json.load(file)
    except FileNotFoundError:
        await m.message.reply("لم يتم العثور على ملف الحسابات.")
        return

    if not accounts_data:
        await m.message.reply("لا توجد حسابات مخزنة حاليًا.")
        return

    response = "قائمة الحسابات:\n"
    for idx, account in enumerate(accounts_data, start=1):
        response += f"الحساب رقم {idx}:\n"
        response += f"رقم الهاتف: {account['phone_number']}\n"
        response += f"جلسة: {account['session']}\n\n"

    await m.message.reply(response)