import discord
from discord.ext import commands
from decouple import config
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

def load_cogs(bot):
    for file in os.path.dirname(os.path.dirname(os.path.abspath("commands"))):
        if file.endswith(".py"):
            cog = file[-3]
            bot.load_extension(f"commands.{cog}")
            
load_cogs(bot=bot)

TOKEN = config("TOKEN")
bot.run(TOKEN)