# Below are imports! These allow for you to expand the Python Standard Library
# with things that wouldn't usually be included. Also, this text is a comment and 
# isn't seen by the interpreter.
import discord
import random
import asyncio
import json
from discord.ext.commands import Bot
from discord.ext import commands
from discord.voice_client import VoiceClient

# This is a try, except clause. It tries to open a JSON file,
# and, if it fails, rather than crashing messily, it shows a friendly message
# and gracefully quits the script.
try:
    # 'with' allows us to temporarily open a file and use it, once we're done, it is removed from memory but any variables
    # we make stay.
    with open("config.json") as file:
        config = json.load(file)
except:
    # 'print' prints stuff to the console. In this case, it's showing us a friendly error 
    # rather than a traceback...
    print("There was an error reading from the config file, please ensure you have one!")
    # exit() gracefully exits the program, and dumps us back into Powershell/CMD
    exit()

# If statements in Python are very easy to implement, and as with the rest of the Python
# language, ensure you are mindful with your indentation!
if not discord.opus.is_loaded():
    try:
        discord.opus.load_opus('opus')
    except:
        print("There was an error loading Opus, ignoring...")

# These are variables, as you may have noticed, there isn't an 'int' or 
# 'string' in front of the names. Python doesn't need them, as it dynamically typed.
prefix = config["prefix"]
token = config["token"]
client = commands.Bot(command_prefix = prefix)

# This is a listener, as it is listening out for an event to happen!
# In this case, it's waiting for the bot to finish loading and connecting.
@client.event
async def on_ready():
	print("Bot is a GO!!")
	print("Name: {}".format(client.user.name))
	
# These are commands. You can see that the name of the command is based off of whatever you call the method below
@client.command(pass_context=True)
async def test(ctx):
	await client.say("AHA! I AM ALIVE!")

@client.command(pass_context=True)
async def whoami(ctx):
	await client.say("You are: " +ctx.message.author.mention)

@client.command(pass_context=True)
async def doubleUp(ctx, arg):
    await client.say("{} doubled is: {}".format(arg, arg * 2))

#Run the bot and connect with the token!	
client.run(token)