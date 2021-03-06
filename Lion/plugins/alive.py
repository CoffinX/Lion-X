# For @LionHelp
"""Check if your userbot is working."""
import time
from datetime import datetime
from io import BytesIO

import requests
from PIL import Image

from Lion import ALIVE_NAME, CMD_HELP, lionver
from Lion.__init__ import StartTime
from Lion.LionConfig import Config, Var

# ======CONSTANTS=========#
CUSTOM_ALIVE = (
    Var.CUSTOM_ALIVE
    if Var.CUSTOM_ALIVE
    else "ππΎπΎ!! ππΎππ π»πΈπΎπ½ ππ± πΈπ π°π»πΈππ΄"
)
ALV_PIC = Var.ALIVE_PIC if Var.ALIVE_PIC else None
lionmoji = Var.CUSTOM_ALIVE_EMOJI if Var.CUSTOM_ALIVE_EMOJI else "**β**"
if Config.SUDO_USERS:
    sudo = "Enabled"
else:
    sudo = "Disabled"
# ======CONSTANTS=========#


def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "@LionXsupport"


@Lion.on(admin_cmd(outgoing=True, pattern="alive"))
@Lion.on(sudo_cmd(outgoing=True, pattern="alive", allow_sudo=True))
async def amireallyalive(alive):
    start = datetime.now()
    myid = bot.uid
    """ For .alive command, check if the bot is running.  """
    end = datetime.now()
    (end - start).microseconds / 1000
    uptime = get_readable_time((time.time() - StartTime))
    if ALV_PIC:
        lion = f"**Welcome To Lion **\n\n"
        lion += f"`{CUSTOM_ALIVE}`\n\n"
        lion += (
            f"{telemoji} **ππ΄π»π΄ππ·πΎπ½ ππ΄πππΈπΎπ½**: `1.17`\n{lionemoji} **Python**: `3.8.3`\n"
        )
        lion += f"{lionemoji} **π»πΈπΎπ½ ππ± ππ΄πππΈπΎπ½**: `{lionver}`\n"
        lion += f"{lionemoji} **π»πΈπΎπ½ πππΏπΏπΎππ**: @LionXsupport\n"
        lion += f"{lionemoji} **πππ³πΎ** : `{sudo}`\n"
        lion += f"{lionemoji} **π»πΈπΎπ½ ππΏππΈπΌπ΄**: `{uptime}`\n"
        lion += f"{lionemoji} **π³π°ππ°π±π°ππ΄ πππ°πππ**: `π°π»π» πΎπΊ π!`\n"
        lion += (
            f"{lionemoji} **πΌπ πΏπ΄ππΎ πΌπ°πππ΄π** : [{DEFAULTUSER}](tg://user?id={myid})\n\n"
        )
        lion += "    [β¨ GΙͺα΄Κα΄Κ Rα΄α΄α΄sΙͺα΄α΄ΚΚ β¨](https://github.com/Mdnoor786/Lion-X)"
        await alive.get_chat()
        await alive.delete()
        """ For .alive command, check if the bot is running.  """
        await borg.send_file(alive.chat_id, ALV_PIC, caption=lion, link_preview=False)
        await alive.delete()
        return
    req = requests.get("https://telegra.ph/file/bfa06df35913425dbcbc1.jpg")
    req.raise_for_status()
    file = BytesIO(req.content)
    file.seek(0)
    img = Image.open(file)
    with BytesIO() as sticker:
        img.save(sticker, "webp")
        sticker.name = "sticker.webp"
        sticker.seek(0)
        await borg.send_message(
            alive.chat_id,
            f"**πππ!! ππππ ππ πππππ **\n\n"
            f"`{CUSTOM_ALIVE}`\n\n"
            f"{lionemoji} **ππ΄π»π΄ππ·πΎπ½ ππ΄πππΈπΎπ½**: `1.17`\n{lionemoji} **Python**: `3.8.3`\n"
            f"{lionemoji} **π»πΈπΎπ½ ππ± ππ΄πππΈπΎπ½**: `{lionver}`\n"
            f"{lionemoji} **π»πΈπΎπ½ πππΏπΏπΎππ**: @LionXsupport\n"
            f"{lionemoji} **πππ³πΎ** : `{sudo}`\n"
            f"{lionemoji} **π»πΈπΎπ½ ππΏππΈπΌπ΄**: `{uptime}`\n"
            f"{lionemoji} **π³π°ππ°π±π°ππ΄ πππ°πππ**: `All OK π!`\n"
            f"{lionemoji} **πΌπ πΏπ΄ππΎ πΌπ°πππ΄π** : [{DEFAULTUSER}](tg://user?id={myid})\n\n"
            "[β¨ gΞΉΡΠ½ΟΠ² ΡΡΟΟΡΞΉΡΟΡΡ β¨](https://github.com/Mdnoor786/Lion-X)",
            link_preview=False,
        )
        await borg.send_file(alive.chat_id, file=sticker)
        await alive.delete()


CMD_HELP.update({"alive": "β `.alive`\nUse - Check if your bot is working."})
