import discord
from discord.ext import commands
from __main__ import send_cmd_help
import aiohttp

class Cat:
    """Cat commands."""

    def __init__(self, bot):
        self.bot = bot
		
    @commands.command(pass_context=True)
    async def cats(self, ctx):
        search = "http://random.cat/meow"
        try:
            async with aiohttp.get(search) as r:
                result = await r.json()
            await self.bot.say(result['file'])
        except:
            await self.bot.say("Somehow something went wrong.")
			
def setup(bot):
    n = Cat(bot)
    bot.add_cog(n)
