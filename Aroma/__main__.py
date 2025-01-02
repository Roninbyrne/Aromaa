import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from Aroma import LOGGER, app, userbot
from Aroma.core.call import Anony
from Aroma.misc import sudo
from Aroma.plugins import ALL_MODULES
from Aroma.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("Assistant client variables not defined, exiting...")
        exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("Aroma.plugins" + all_module)
    LOGGER("Aroma.plugins").info("Successfully Imported Modules...")
    await userbot.start()
    await Anony.start()
    try:
        await Anony.stream_call("https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4")
    except NoActiveGroupCall:
        LOGGER("Aroma").error(
            "Please turn on the videochat of your log group\channel.\n\nStopping Bot..."
        )
        exit()
    except:
        pass
    await Anony.decorators()
    LOGGER("Aroma").info(
        "\x4d\x41\x44\x45\x20\x42\x59\x20\x53\x41\x52\x4b\x41\x52\x2e\x20\x46\x4f\x4c\x4c\x4f\x57\x20\x40\x54\x47\x5f\x4e\x41\x4d\x45\x5f\x53\x54\x59\x4c\x45"
    )
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("Aroma").info("Stopping Aroma Music Bot...")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
