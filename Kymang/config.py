#Kymang

import os

from dotenv import load_dotenv

load_dotenv(".env")


BOT_TOKEN = os.environ.get("BOT_TOKEN", "7190064")
API_ID = int(os.environ.get("API_ID", ""))
API_HASH = os.environ.get("API_HASH", "")
MONGO_URL = os.environ.get("MONGO_URL", "mongodb+srv://retryWrites=t")
ADMINS = [int(x) for x in (os.environ.get("ADMINS", "1666845").split())]
MEMBER = [int(x) for x in (os.environ.get("MEMBER", "160").split())]
LOG_GRP = int(os.environ.get("LOG_GRP", "-"))
BOT_ID = int(os.environ.get("BOT_ID", "7190064"))

KITA = [int(x) for x in (os.environ.get("KITA", "7182827").split())]
