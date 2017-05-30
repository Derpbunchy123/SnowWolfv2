# Inspired by PaddoInWonderland PaddoCogs away Cog for Twentysix26 Red

from discord.ext import commands
import discord
import configparser

class Away:
	global status

	def __init__(self, bot):
		self.bot = bot

	@commands.command(pass_context=True)
	async def away(self, ctx, *message: str):
		Config = configparser.ConfigParser()
		try:
			Config.read("away.ini")
			status = Config["away"][str(ctx.message.author.id)]
			if status == "False":
				Config["away"][str(ctx.message.author.id)] = "True"
				if message:
					Config["messages"][str(ctx.message.author.id)] = " ".join(ctx.message.clean_content.split()[1:])
				Config.write(open("away.ini", "w"))
			else:
				Config["away"][str(ctx.message.author.id)] = "False"
				Config["messages"][str(ctx.message.author.id)] = ""
				Config.write(open("away.ini", "w"))
		except:
			awayCFG = open("away.ini", "w+")
			Config["away"] = {}
			Config["messages"] = {}
			Config["away"][str(ctx.message.author.id)] = "True"
			if message:
				Config["messages"][str(ctx.message.author.id)] = " ".join(ctx.message.clean_content.split()[1:])
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
							pic = author.avatar_url if author.avatar else author.default_avatar_url
							if not Config["messages"][str(author.id)] == "":
								e = discord.Embed(description=Config["messages"][str(author.id)], color=discord.Color.red())
								e.set_author(name="{} is away".format(author.display_name), icon_url=pic)
							else:
								e = discord.Embed(color=discord.Color.red())
								e.set_author(name="{} is away with no message".format(author.display_name), icon_url=pic)
							await self.bot.send_message(message.channel, embed=e)
				except:
					pass

def setup(bot):
	bot.add_cog(Away(bot))
