from .. import Zaid
from telethon import events, Button

@Zaid.on(events.NewMessage(incoming=True, pattern="/start"))
async def start(event):
    await event.reply("Hello! Welcome To Music Bot Based On Telethon",
                    buttons=[
                        [Button.url("ButtonUrl", url="https://t.me/itz_Shekhar")],
                        [Button.url("ButtonUrl", url="https://t.me/pipinstallshekhar")],
                    ])
