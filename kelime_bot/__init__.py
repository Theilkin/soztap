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
API_ID = getenv("API_ID", "29341839")
API_HASH = getenv("API_HASH", "557d3180ae884c8d59a28c1ed9fe4004")
TOKEN = getenv("TOKEN", "7034840004:AAHTnm0IqLVM4tBLkwEZDn6i5fa-7k72JZI")
USERNAME = getenv("USERNAME", "ismayilofh")
OWNER_ID = getenv("OWNER_ID", "6671958102")

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
