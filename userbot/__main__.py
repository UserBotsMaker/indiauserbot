from pathlib import Path
from sys import argv

import telethon.utils
from telethon import TelegramClient
import os

from userbot import bot
from userbot.utils import load_module as load_plugins
from var import Var


async def add_bot(bot_token):
    await bot.start(bot_token)
    bot.me = await bot.get_me()
    bot.uid = telethon.utils.get_peer_id(bot.me)


if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    if Var.TG_BOT_USER_NAME_BF_HER is not None:
        print("Initiating Inline Bot")
        # ForTheGreatrerGood of beautification
        bot.tgbot = TelegramClient(
            "TG_BOT_TOKEN", api_id=Var.APP_ID, api_hash=Var.API_HASH
        ).start(bot_token=Var.TG_BOT_TOKEN_BF_HER)
        print("Initialisation finished with no errors")
        print("Starting Userbot")
        bot.loop.run_until_complete(add_bot(Var.TG_BOT_USER_NAME_BF_HER))
        print("Startup Completed")
    else:
        bot.start()


import glob
# for userbot
files = sorted(os.listdir("userbot.plugins"))
for plugin_name in files:
    try:
        if plugin_name.endswith(".py"):
            load_plugins(plugin_name[:-3])
            if not plugin_name.startswith("__") or plugin_name.startswith("_"):
                LOGS.info(f"ExtremeProUserbot - Official -  Installed - {plugin_name}")
    except Exception:
        LOGS.info(f"Indian Userbot - Official - ERROR - {plugin_name}")
        LOGS.info(str(traceback.print_exc()))




print("Yay your userbot is officially working. You should owe @pureindialover")

if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
