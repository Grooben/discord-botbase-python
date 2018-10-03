import discord
import asyncio
import json
from pprint import pprint

try:
	with open('config.json') as file:
		config = json.load(file)
		pprint(config)
except: 
	print("There was an error reading from the config file, please ensure you have one!")

token = config["token"]
prefix = config["prefix"]

bot = discord.Client()

@bot.event
async def on_ready():
	print("Logged in as ", bot.user.name)

@bot.event
async def on_message(message):
	if message.content.startswith(prefix):
		if "ping" in message.content:
			pong = await bot.send_message(message.channel, "Pong!")

bot.run(token)