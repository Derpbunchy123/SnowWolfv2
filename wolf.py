import discord
from discord.ext import commands

import sys
import os

import configparser

desc = """
SnowWolf Rewritten - Since 23 May 2017
"""
prefix = ["\\"]

bot = commands.Bot(command_prefix=prefix, description=desc)

@bot.event
async def on_command_error(error, ctx):
	await bot.add_reaction(ctx.message, "\N{NEGATIVE SQUARED CROSS MARK}")

@bot.event
async def on_ready():
	print("Logged into Discord: ")
	print("Username: " + bot.user.name)
	print("ID: " + bot.user.id)
	print("========")
	oauthData = bot.application_info()
	print("Invite Me: " + discord.utils.oauth_url(bot.user.id) + "&permissions=8")

	await bot.change_presence(game=discord.Game(name="with really bad code // \help"))

# this is crap
def getToken():
	Config = configparser.ConfigParser()
	try:
		Config.read("info.ini")
		return Config["login"]["token"]
	except:
		tokenCFG = open("info.ini", "w+")
		Config["owner"] = {}
		Config["login"] = {}
		Config["owner"]["id"] = input("Owner ID: ")
		Config["login"]["token"] = input("Token: ")
		Config.write(tokenCFG)
		#Config.read("token.ini")
		#print(Config["login"]["token"])
		tokenCFG.close()
		Config.read("info.ini")
		return Config["login"]["token"]

if __name__ == "__main__":
	# print("Logging in with Token: " + getToken())
	token = getToken()
	bot.client_id = token
	#bot.run(token)

	active_extensions = []
	for file in os.listdir("extensions"):
		if(file.endswith(".py")):
			bot.load_extension("extensions.{}".format(file.split(".")[0]))
			active_extensions.append(file)
			print("Found and Loaded Extension: " + file)
	print("All Extensions Loaded.")
	print(active_extensions)

	bot.run(token)
