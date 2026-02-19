import re
from os import environ

# Bot Session Name
SESSION = environ.get('SESSION', 'TechVJBot')

# Your Telegram Account Api Id And Api Hash
API_ID = int(environ.get('API_ID', '37387930'))
API_HASH = environ.get('API_HASH', '9215731aac5c36bc32c7cfe9b28a7833')

# Bot Token, This Is Main Bot
BOT_TOKEN = environ.get('BOT_TOKEN', "8549013218:AAEZp8rftAh49zSK2OfeNvcnClaCNs623Nk")

# Admin Telegram Account Id For Withdraw Notification Or Anything Else
ADMIN = int(environ.get('ADMIN', '5977820427'))

# Back Up Bot Token For Fetching Message When Floodwait Comes
BACKUP_BOT_TOKEN = environ.get('BACKUP_BOT_TOKEN', "8500855417:AAEVsvVf6eO-JAt9Eb7-e76D7BSOAQbJGv4")

# Log Channel, In This Channel Your All File Stored.
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1003873059858'))

# Mongodb Database For User Link Click Count Etc Data Store.
MONGODB_URI = environ.get("MONGODB_URI", "mongodb+srv://suman001:<db_password>@cluster0.tt60lwz.mongodb.net/?appName=Cluster0")

# Stream Url Means Your Deploy Server App Url, Here You Media Will Be Stream And Ads Will Be Shown.
STREAM_URL = environ.get("STREAM_URL", "https://vj-video-player-2mt4.onrender.com")

# This Link Used As Permanent Link That If Your Deploy App Deleted Then You Change Stream Url, So This Link Will Redirect To Stream Url.
LINK_URL = environ.get("LINK_URL", "https://download.taazainsurance.in/")

# Others, Not Usefull
PORT = environ.get("PORT", "8080")
MULTI_CLIENT = False
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
if 'DYNO' in environ:
    ON_HEROKU = True
else:
    ON_HEROKU = False
