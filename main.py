from discord.ext import commands
from config import discord_settings, yandex_settings
from yandex_music import Client
from bot.bot import initBot
from pyparsing import *

parses = {
    "General album": "https://music.yandex.ru/album/" + Word(nums),
    "User album": "https://music.yandex.ru/users/" +\
                  Word(str(list(filter(lambda x: x != "/", list(printables))))) +\
                  "/playlists/" + Word(nums)
}

if __name__ == "__main__":
    yandexClient = Client.from_credentials(yandex_settings["login"], yandex_settings["password"])
    print("Yandex - ok")
    def isValidUrl(url):
        isParsed = False
        for parser in parses.values():
            try:
                parser.parseString(url)
                isParsed = True
                break
            except Exception as e:
                pass
        return isParsed

    def urlToPlaylist(url):
        try:
            tracks = []
            albumId = int(parses["General album"].parseString(url)[1])
            album = yandexClient.albums_with_tracks(albumId)
            for volume in album.volumes:
                tracks += volume
            def getDirectLink(track):
                def f():
                    for info in track.get_download_info():
                        if info.codec == "mp3" and info.bitrate_in_kbps == 192:
                            return info.get_direct_link()
                return f
            return list(map(getDirectLink, tracks))
        except Exception as e:
            pass

        try:
            _, user_id, _, kind = parses["User album"].parseString(url)
            album = yandexClient.users_playlists(user_id=user_id, kind=kind)
            assert(not album is None)
            def getDirectLink(trackShort):
                def f():
                    for info in trackShort.fetch_track().get_download_info():
                        if info.codec == "mp3" and info.bitrate_in_kbps == 192:
                            return info.get_direct_link()
                return f
            return list(map(getDirectLink, album.fetch_tracks()))
        except Exception as e:
            pass

    bot = commands.Bot(command_prefix = discord_settings['prefix'])
    initBot(bot, isValidUrl, urlToPlaylist)
    bot.run(discord_settings['token'])
