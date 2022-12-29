import json
import os
import requests

# load the config from the config.json file
with open('config.json', 'r') as f:
    config = json.load(f)

# build the URL using the config values
import json
import os

import discord
from discord.ext import commands

with open('config.json') as f:
    data = json.load(f)
    TOKEN = data["DISCORD_TOKEN"]

intents = discord.Intents.default()
intents.message_content = True


class Bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", intents=intents)

    async def startup(self):
        await bot.wait_until_ready()
        await bot.tree.sync()
        await bot.change_presence(status=discord.Status.online, activity=discord.Game(name="I smell some sales"))
        print('Sucessfully synced applications commands')
        print(f'Connected as {bot.user}')

    async def setup_hook(self):
        for filename in os.listdir("./cogs"):
            if filename.endswith(".py"):
                try:
                    await bot.load_extension(f"cogs.{filename[:-3]}")
                    print("{0} is online".format(filename[:-3]))
                except Exception as e:
                    print("{0} was not loaded".format(filename))
                    print(f"[ERROR] {e}")

        self.loop.create_task(self.startup())


bot = Bot()
# get string from config file
bot.run(TOKEN)
