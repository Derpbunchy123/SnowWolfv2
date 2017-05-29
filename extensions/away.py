from discord.ext import commands
import discord
import configparser

class Away:
	global status

	def __init__(self, bot):
		self.bot = bot

	@commands.command(pass_context=True)
	async def away(self, ctx):
		Config = configparser.ConfigParser()
		try:
			Config.read("away.ini")
			status = Config["away"][str(ctx.message.author.id)]
			if status == "False":
				Config["away"][str(ctx.message.author.id)] = "True"
				Config.write(open("away.ini", "w"))
			else:
				Config["away"][str(ctx.message.author.id)] = "False"
				Config.write(open("away.ini", "w"))
		except:
			awayCFG = open("away.ini", "w+")
			Config["away"] = {}
			Config["away"][str(ctx.message.author.id)] = "True"
			Config.write(awayCFG)

	async def on_message(self, message):
		Config = configparser.ConfigParser()
		mtn = {}
		for mention in message.mentions:
			mtn[mention] = True
		if message.author.id != self.bot.user.id:
			for author in mtn:
				try:
					Config.read("away.ini")
					if isinstance(Config["away"][str(author.id)], str):
						if Config["away"][str(author.id)] == "True":
							await self.bot.send_message(message.channel, "{} is away".format(author.id))
				except:
					pass

def setup(bot):
	bot.add_cog(Away(bot))
