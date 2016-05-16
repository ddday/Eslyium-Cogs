import discord
from discord.ext import commands
import aiohttp
from .utils import checks
from __main__ import send_cmd_help

class Ntools:
    """Network Tools (Pings/traceroutes/etc)"""

    def __init__(self, bot):
        self.bot = bot

    @commands.group(pass_context=True)
    @checks.is_owner()
    async def ntools(self, ctx):
        """Network Tools (Pings/traceroutes/etc)"""
        if ctx.invoked_subcommand is None:
            await send_cmd_help(ctx)
            return
			
    @ntools.command()
    async def nping(self, user_input: str):
        """Check to see if a website is responsive."""

        async with aiohttp.request('GET', "http://api.hackertarget.com/nping/?q="+user_input) as resp:
            await self.bot.say(await resp.text())

    @ntools.command()
    async def mtr(self, user_input: str):
        """Checks the routing of a hostname or IP."""

        async with aiohttp.request('GET', "http://api.hackertarget.com/mtr/?q="+user_input) as resp:
            await self.bot.say(await resp.text())

    @ntools.command()
    async def geoip(self, user_input: str):
        """Checks the location of an IP."""
		
        async with aiohttp.request('GET', "http://api.hackertarget.com/geoip/?q="+user_input) as resp:
            await self.bot.say("The location of that IP is:\n" + await resp.text())

    @ntools.command()
    async def upordown(self, user_input: str):
        """Checks to see if a website is online or not."""

        async with aiohttp.request('GET', "http://api.predator.wtf/upordown/?arguments="+user_input) as resp:
            await self.bot.say(await resp.text())
			
    @ntools.command()
    async def dnslookup(self, user_input: str):
        """Checks the DNS records of a hostname."""

        async with aiohttp.request('GET', "http://api.hackertarget.com/dnslookup/?q="+user_input) as resp:
            await self.bot.say(await resp.text())
			
    @ntools.command()
    async def reversedns(self, user_input: str):
        """Checks the DNS hostname."""

        async with aiohttp.request('GET', "http://api.hackertarget.com/reversedns/?q="+user_input) as resp:
            await self.bot.say(await resp.text())
			
    @ntools.command()
    async def headers(self, user_input: str):
        """Returns header information of a hostname."""

        async with aiohttp.request('GET', "http://api.hackertarget.com/httpheaders/?q="+user_input) as resp:
            await self.bot.say(await resp.text())
			
    @ntools.command()
    async def pagelinks(self, user_input: str):
        """Displays all the links within a web page."""

        async with aiohttp.request('GET', "http://api.hackertarget.com/pagelinks/?q="+user_input) as resp:
            await self.bot.say(await resp.text())
			
    @ntools.command()
    async def reverseip(self, user_input: str):
        """Searches the data finding all records."""

        async with aiohttp.request('GET', "http://api.hackertarget.com/reverseiplookup/?q="+user_input) as resp:
            await self.bot.say(await resp.text())
				
    @ntools.command()
    async def whois(self, user_input: str):
        """Find the ISP, Hosting provider."""

        async with aiohttp.request('GET', "http://api.hackertarget.com/whois/?q="+user_input) as resp:
            await self.bot.say(await resp.text())


def setup(bot):
    n = Ntools(bot)
    bot.add_cog(n)