from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "34446649"))
    API_HASH = getenv("API_HASH", "8dc570c08d8e35e88fb9bfc73c65d7fa")
    BOT_TOKEN = getenv("BOT_TOKEN", "8591083411:AAH1phm791rkKiByG4kgkFB7gBhSCIjgv4Y")
    CHID = int(getenv("CHID", "-1003515041061"))
    SUDO = list(map(int, getenv("SUDO").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://Anujedit:Anujedit@cluster0.7cs2nhd.mongodb.net/?appName=Cluster0")
    LOGCHID = int(getenv("LOGCHID", "-1003515041061"))
    API = getenv("API", "8591083411:AAH1phm791rkKiByG4kgkFB7gBhSCIjgv4Y")
cfg = Config()
