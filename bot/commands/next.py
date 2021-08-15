def add(bot):
    @bot.command(
        name='next',
        pass_context=True,
        description="Next composition in the playlist.",
    )
    async def botNext(ctx):
        if ctx.author.voice and ctx.voice_client and ctx.author.voice.channel == ctx.voice_client.channel:
            ctx.voice_client.stop()
        else:
            await ctx.send('You have to be connected to the same voice channel to next.')
