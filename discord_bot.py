import discord
from discord.ext import tasks
from datetime import datetime

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
        await message.channel.send(message.content)
client.run(TOKEN)
