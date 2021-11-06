import os

discord_settings = {
    'token':  os.environ['DISCORD_BOT_TOKEN'],
    'bot':    os.environ['DISCORD_BOT_NAME'],
    'id':     os.environ['DISCORD_BOT_ID'],
    'prefix': os.environ['DISCORD_BOT_PREFIX'],
}

yandex_settings = {
    "login":    os.environ['YANDEX_LOGIN'],
    "password": os.environ['YANDEX_PASSWORD'],
}
