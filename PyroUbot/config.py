import os
from dotenv import load_dotenv

load_dotenv(".env")

MAX_BOT = int(os.getenv("MAX_BOT", "100"))

DEVS = list(map(int, os.getenv("DEVS", "6615675254").split()))

API_ID = int(os.getenv("API_ID", "23226782"))

API_HASH = os.getenv("API_HASH", "50a8a9ca1b1bd90c81f9acc36da2f511")

BOT_TOKEN = os.getenv("BOT_TOKEN", "8482482651:AAGyR55eduojEZNgWWufJoatZgB_1U6F_Hs")

OWNER_ID = int(os.getenv("OWNER_ID", "6615675254"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1002125842026 -1002053287763").split()))

RMBG_API = os.getenv("RMBG_API", "9JhGsK6DJBxx5i3TQAiAqF4s")

MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://fizzpamell:fizzpamell@cluster0.9nmhi5m.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "-4912568273"))
