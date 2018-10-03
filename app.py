import json
from pprint import pprint

from discord.ext import commands

try:
    with open("config.json") as file:
        config = json.load(file)
        pprint(config)
except:
    print("There was an error reading from the config file, please ensure you have one!")

prefix = config["prefix"]
token = config["token"]
bot = commands.Bot(command_prefix = prefix)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")


@bot.command(name="ping")
async def ping(ctx):
    await ctx.send(f"Pong! {round(bot.latency, 1)}")

@bot.command()
async def test(ctx):
	await ctx.send("REEEEEEE")

bot.run(token)