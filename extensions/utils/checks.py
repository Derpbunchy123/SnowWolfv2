from discord.ext import commands
import discord.utils

import configparser

def is_owner_check(message):
	Config = configparser.ConfigParser()
	try:
		Config.read("info.ini")
		id = Config["owner"]["id"]
	except:
		idCFG = open("info.ini", "w+")
		Config["owner"] = {}
		Config["owner"]["id"] = input("Owner ID: ")
		Config.write(idCFG)
		idCFG.close()
		Config.read("info.ini")
		id = Config["owner"]["id"]
	return message.author.id == id

def is_owner():
	return commands.check(lambda ctx: is_owner_check(ctx.message))
