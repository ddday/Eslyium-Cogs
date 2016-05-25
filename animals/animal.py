import discord
from discord.ext import commands
from __main__ import send_cmd_help
import aiohttp

class Animal:
    """Animal commands."""

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
            await self.bot.say("Couldnt Get An Image")

    @commands.command(pass_context=True)
    async def pugs(self, ctx):
        search = "http://pugme.herokuapp.com/random"
        try:
            async with aiohttp.get(search) as r:
                result = await r.json()
            await self.bot.say(result['pug'])
        except:
            await self.bot.say("Could Not Get An Image")

def setup(bot):
    n = Animal(bot)
    bot.add_cog(n)