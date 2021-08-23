from discord import FFmpegOpusAudio
import threading

def add(bot, isValidUrl, urlToPlaylist, play):
    @bot.command(
        name='play',
        pass_context=True,
        description="Play the playlist with link.",
        usage="[https://music.yandex.ru/album/xxxxx|https://music.yandex.ru/users/xxxxx/playlists/xxxxx]",
    )
    async def botPlay(ctx, *args):
        if len(args) != 1:
            await ctx.send('Invalid play command, see help.')
            return
        else:
            url = args[0]
        if not isValidUrl(url):
            await ctx.send("Wrong url format, see help.")
            return
        try:
            playlist = urlToPlaylist(url)
        except Exception as e:
            await ctx.send("Invalid url.")
            return
        if not ctx.author.voice:
            await ctx.send('You have to be connected to any voice channel.')
            return
        if ctx.voice_client:
            await ctx.voice_client.disconnect()
        try:
            voice = await ctx.author.voice.channel.connect()
        except Exception as e:
            await ctx.voice_client.disconnect()
            voice = await ctx.author.voice.channel.connect()
    
        if not voice.is_playing():
            bot.playlists[ctx.message.guild.id] = playlist
            threading.Thread(name=str(ctx.message.guild.id) + "Player", target=play, args=(ctx.message.guild.id, voice,)).start()
        else:
            await ctx.send("Already playing audio.")
            return
