from pyrogram import Client
from pyrogram import filters
from pyrolistener import Listener

api_id = 20220894
api_hash = "87b472b166bd80d7420df36147783a37"  
bot_token = "6514720098:AAFUZpODkmNUpEihEBhylmd4-YLWkImmqHM"
print_id = 5207032121 ##ايدي تحويل نقاط

app = Client(
    "MyApp",
    api_id=api_id,
    api_hash=api_hash,
    bot_token=bot_token,
    plugins=dict(root="plugins")
)


listener = Listener(client=app, show_output=True)