# Thanks For: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/ramadhani892/RamPyro-Bot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/SharingUserbot & t.me/GzSupport

from base64 import b64decode as kodenya
from distutils.util import strtobool
from os import getenv

from dotenv import load_dotenv

load_dotenv("config.env")


ALIVE_EMOJI = getenv("ALIVE_EMOJI", "🦋")
ALIVE_LOGO = getenv("ALIVE_LOGO", "https://graph.org/file/1e53a14e6a70757d1d736.jpg")
ALIVE_TEKS_CUSTOM = getenv("ALIVE_TEKS_CUSTOM", "Hey bro, I am Gz.")
API_HASH = getenv("API_HASH")
API_ID = getenv("API_ID")
BLACKLIST_CHAT = getenv("BLACKLIST_CHAT", None)
if not BLACKLIST_CHAT:
    BLACKLIST_CHAT = [-1001692751821]
BLACKLIST_GCAST = {int(x) for x in getenv("BLACKLIST_GCAST", "").split()}
BOTLOG_CHATID = int(getenv("BOTLOG_CHATID") or 0)
BOT_VER = "0.3.1@dragons"
BRANCH = "dragons"
CH_SFS = getenv("CH_SFS", "GzSupport")
IG_ALIVE = getenv("IG_ALIVE", "alvrnxz")
CHANNEL = getenv("CHANNEL", "userbotch")
CMD_HANDLER = getenv("CMD_HANDLER", ".")
DB_URL = getenv("DATABASE_URL", "")
GIT_TOKEN = getenv(
    "GIT_TOKEN",
    kodenya("Z2hwX1E4SVdRWVFkeWNRd2RWMzBMdENIQ1M3Rm9KM2tTUzJlaGh1OA==").decode(
        "utf-8"
    ),
)
GROUP = getenv("GROUP", "GzSupport")
HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)
PMPERMIT_PIC = getenv("PMPERMIT_PIC", None)
PM_AUTO_BAN = strtobool(getenv("PM_AUTO_BAN", "True"))
REPO_URL = getenv(
    "REPO_URL",
    kodenya("aHR0cHM6Ly9naXRodWIuY29tL3JhbWtheTEzMi9weXJvcmFtMQ==").decode("utf-8"),
)
STRING_SESSION1 = getenv("STRING_SESSION1", "")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
