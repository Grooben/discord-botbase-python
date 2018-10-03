import discord
import asyncio
import json
from pprint import pprint

with open('config.json') as file:
    config = json.load(file)

pprint(config)

