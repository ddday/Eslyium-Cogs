import discord
from discord.ext import commands
from __main__ import send_cmd_help
import aiohttp
from bs4 import BeautifulSoup

class Pug:
    """Pug commands."""

    def __init__(self, bot):
        self.bot = bot
		
    @commands.command(pass_context=True)
    async def pugs(self, ctx):
        search = "http://pugme.herokuapp.com/random"
        try:
            async with aiohttp.get(search) as r:
                result = await r.json()
            await self.bot.say(result['pug'])
        except:
            await self.bot.say("Somehow something went wrong.")
			
def setup(bot):
    n = Pug(bot)
    bot.add_cog(n)
