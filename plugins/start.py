from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from pyrolistener import Listener
from mmllm.her import listener

keyboard = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("𝐀𝐝𝐝 𝐀𝐜𝐜𝐨𝐮𝐧𝐭", callback_data="zuue"),
            InlineKeyboardButton("𝐃𝐞𝐥𝐞𝐭𝐞 𝐀𝐜𝐜𝐨𝐮𝐧𝐭", callback_data="delete_account")
        ],
        [
            
            InlineKeyboardButton("𝐍𝐮𝐦𝐛𝐞𝐫 𝐨𝐟 𝐚𝐜𝐜𝐨𝐮𝐧𝐭𝐬", callback_data="show_accounts")
        ],
        [
            InlineKeyboardButton("𝐂𝐨𝐥𝐥𝐞𝐜𝐭 𝐏𝐨𝐢𝐧𝐭𝐬 DamKombot", callback_data="DamKombot"),
        ],
        [
            InlineKeyboardButton("𝐎𝐖𝐍𝐄𝐑", url="https://t.me/iii_cvc")
        ]
    ]
)

@Client.on_message(filters.command("start"))
async def start_command(client, message):
    username = message.from_user.first_name
    welcome_message = f"- اهلا بك عزيزي {username} ♥ \n \n - مرحبا بك في بوت تحكم في الحسابات الخاصه بك وتجميع النقاط 🌼🌹 \n \n - قناه البوت @xxStitch ✅"
    await message.reply_text(welcome_message, reply_markup=keyboard)