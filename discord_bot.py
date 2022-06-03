import discord
import logging


client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author.bot:
        return

    if message.content.startswith('$hello'):
        await message.channel.send(f'Hello!')

client.run('')