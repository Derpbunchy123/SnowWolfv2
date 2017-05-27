from discord.ext import commands
import discord

from .utils import checks

class Ping:
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	@checks.is_owner()
	async def ping(self):
		embed = discord.Embed(color=discord.Color.blue())
		embed.add_field(name="Ping.", value="Pong.")
		await self.bot.say(embed=embed)

def setup(bot):
	bot.add_cog(Ping(bot))
