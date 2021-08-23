def add(bot, isValidUrl, urlToPlaylist):
    @bot.command(
        name='add',
        pass_context=True,
        description="Add the playlist to the queue.",
        usage="[https://music.yandex.ru/album/xxxxx|https://music.yandex.ru/users/xxxxx/playlists/xxxxx]",
    )
    async def botAdd(ctx, *args):
        if len(args) != 1:
            await ctx.send('Invalid add command, see help.')
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

        if not ctx.message.guild.id in bot.playlists.keys():
            await ctx.send('Current playlist is empty, use play command instead.')
            return
        if not ctx.author.voice:
            await ctx.send('You have to be connected to same voice channel.')
            return
        if not ctx.voice_client:
            await ctx.send('I have to be connected to same voice channel.')
            return
        bot.playlists[ctx.message.guild.id] += playlist
