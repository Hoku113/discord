import discord
from discord.ext import tasks
from datetime import datetime
from discord.ext import commands
import time

bot = commands.Bot(command_prefix='$')

TOKEN = ""
CHANNEL_ID = 

intents = discord.Intents.default()

client = discord.Client()

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('$'):
        for x in range(10):
            await message.channel.send("custom stamp")
            time.sleep(0.25)
client.run(TOKEN)