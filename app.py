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