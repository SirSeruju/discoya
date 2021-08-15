from discord.ext import commands
from config import discord_settings, yandex_settings
from yandex_music import Client
from bot.bot import initBot


def isValidUrl(url):
    prefix = '/'.join(url.split('/')[:-1])
    if (prefix == "https://music.yandex.ru/album"):
        try:
            int(url.split('/')[-1])
        except Exception as e:
            return False
        else:
            return True
    else:
        return False

if __name__ == "__main__":
    yandexClient = Client.from_credentials(yandex_settings["login"], yandex_settings["password"])
    print("Yandex - ok")
    def urlToPlaylist(url):
        playlist = []
        tracks = []
        albumId = int(url.split('/')[-1])
        album = yandexClient.albums_with_tracks(albumId)
        for volume in album.volumes:
            tracks += volume

        for track in tracks:
            for info in track.get_download_info():
                if info.codec == "mp3" and info.bitrate_in_kbps == 192:
                    playlist.append(info.get_direct_link())
                    break
        return playlist

    bot = commands.Bot(command_prefix = discord_settings['prefix'])
    initBot(bot, isValidUrl, urlToPlaylist)
    bot.run(discord_settings['token'])
