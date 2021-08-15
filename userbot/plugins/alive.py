from userbot import ALIVE_NAME
from userbot.utils import admin_cmd

name = str(ALIVE_NAME)
INDIANBOT_IS_ALIVE = (
    "**Apun Zinda He Sarr ^.^** \n`🇮🇳BOT Status : ` **☣Hot**\n\n"
    f"`My peru owner`: {name}\n\n"
    "`Indian Bot Version:` **0.1**\n`Python:` **3.9.6**\n"
    "     [🇮🇳Deploy This IndianBot🇮🇳](https://heroku.com/deploy?template=https://github.com/INDIAN-USERBOT/indian)"
)


@borg.on(admin_cmd(pattern="alive"))
async def amireallyalive(alive):
    chat = await alive.get_chat()
    await alive.delete()
    await borg.send_message(chat, INDIANBOT_IS_ALIVE, link_preview=False)
