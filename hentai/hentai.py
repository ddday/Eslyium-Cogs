import discord
from discord.ext import commands
import aiohttp
from __main__ import send_cmd_help

class Hentai:
    """Hentai commands."""

    def __init__(self, bot):
        self.bot = bot

    @commands.group(pass_context=True)
    async def hentai(self, ctx):
        """Hentai commands"""
        if ctx.invoked_subcommand is None:
            await send_cmd_help(ctx)

    @hentai.command(no_pm=True)
    async def shm(self):
        """Sends a random hentai"""
        url = "http://streamhentaimovies.com/?orderby=rand"
        async with aiohttp.get(url) as r:
            await self.bot.say(r.url)
			
    @hentai.command(no_pm=True)
    async def hd(self):
        """Sends a random hentai"""
        url = "http://hentaidream.me/random"
        async with aiohttp.get(url) as r:
            await self.bot.say(r.url)
			
def setup(bot):
    bot.add_cog(Hentai(bot))