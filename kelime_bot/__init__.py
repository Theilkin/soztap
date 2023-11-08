from time import sleep
from pyrogram import Client
import logging
from dotenv import load_dotenv, set_key, unset_key
from os import getenv

load_dotenv('config.env')

# THE LOGGING
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger("pyrogram").setLevel(logging.WARNING)
LOGGER = logging.getLogger(__name__)


# Hesap
API_ID = getenv("API_ID", "26090016")
API_HASH = getenv("API_HASH", "5b842f9801712684f2b98d70ead6538d")
TOKEN = getenv("TOKEN", "6965819675:AAFw1MFvsw2MkR5ELF1lX-xKNDo0fELvF5Q")
USERNAME = getenv("USERNAME", "The_ferid")
OWNER_ID = getenv("OWNER_ID", "6297494131")

if OWNER_ID and len(OWNER_ID) and OWNER_ID.isdigit():
    OWNER_ID = int(OWNER_ID)  # type: ignore
else:
    OWNER_ID = None  # type: ignore

# BOT CLIENTİ
bot = Client(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=TOKEN,
    plugins=dict(root="kelime_bot/plugins/"),
    workers=16
)


# Oyun Verileri
oyun = {}  # type: ignore


# rating
rating = {}  # type: ignore
