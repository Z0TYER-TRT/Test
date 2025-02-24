import os
import json

def get_user_list(config, key):
    file_path = os.path.join(os.getcwd(), "NekoRobot", config)
    if not os.path.exists(file_path):
        print(f"Warning: {file_path} not found. Using empty list.")
        return []  # Return an empty list instead of crashing

    with open(file_path, "r") as json_file:
        return json.load(json_file).get(key, [])


def get_user_list(config, key):
    with open("{}/NekoRobot/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]


class Config(object):
    LOGGER = True

    API_ID = "20658929"
    API_HASH = "d0ddf4f6a90d1782e0cb16c01a319cc5"
    TOKEN = "7230167851:AAFGoVG8Xenx-F9ffPZTOY23EZ3jcWX-Ys4"
    OWNER_ID = "5702598840"
    OWNER_USERNAME = "TheRyoman"
    SUPPORT_CHAT = "Flex_support_Chat"
    JOIN_LOGGER = "-1002100475470"
    EVENT_LOGS = "-1002100475470"

    SQLALCHEMY_DATABASE_URI = "postgres://uf3vmdktbh0r1n:pcb8071af4eaf1e040dad0a46e211165f0d851d1091948d1389df18494affb762@cfls9h51f4i86c.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com:5432/d3sta0c87hlqc8"
    MONGO_DB_URI = "mongodb+srv://bankaiaizen891:eC-1654-xGQS-tnm-4iIqpq1@cluster0.dxkqk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    LOAD = []
    NO_LOAD = ["rss"]
    WEBHOOK = False
    INFOPIC = True
    URL = None

    # OPTIONAL
    ##List of id's -  (not usernames) for users which have sudo access to the bot.
    DRAGONS = get_user_list("elevated_users.json", "sudos")
    ##List of id's - (not usernames) for developers who will have the same perms as the owner
    DEV_USERS = get_user_list("elevated_users.json", "devs")
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    DEMONS = get_user_list("elevated_users.json", "supports")
    # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    TIGERS = get_user_list("elevated_users.json", "tigers")
    WOLVES = get_user_list("elevated_users.json", "whitelists")

    DONATION_LINK = ""
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True
    STRICT_GBAN = True
    WORKERS = (
        8  # Number of subthreads to use. Set as number of threads your processor uses
    )
    BAN_STICKER = (
        "CAACAgUAAxkBAAEDafNhq5Z0DegqVzauwSighMw5cPWp8QACVgQAAuUG0FRXfCEuBziNzCIE"
    )
    ALLOW_EXCL = True
    CASH_API_KEY = ""
    TIME_API_KEY = ""
    BL_CHATS = []
    SPAMMERS = None
    ALLOW_CHATS = True
    START_IMG = ""
    HEROKU_API_KEY = None
    HEROKU_APP_NAME = None
    TEMP_DOWNLOAD_DIRECTORY = "./"
    ARQ_API_KEY = "LJMETG-DPHBCX-DGHJCD-TMFIGB-ARQ"
    ARQ_API_URL = "https://arq.hamker.in"
    ALLOW_EXCL = None
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
