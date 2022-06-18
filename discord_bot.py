import discord
from discord.ext import tasks
from discord.channel import TextChannel
from datetime import datetime
import time
import random

# 本番環境用
# user_list = []
test_user_list = []
level = {'1': 10, '2': 20, '3': 30, '4': 40, '5':50}


TOKEN = ""
CHANNEL_ID = 

intents = discord.Intents.default()

client = discord.Client()

@tasks.loop(seconds=1)
async def loop():
    now = datetime.now()
    now = now.strftime('%H:%M')
    if now == '05:31':
        channel = TextChannel._get_channel()
        # user = client.get_user(test_user_list[random.randint(1)])
        number = level[str(random.randint(1, 5))]
        await channel.send('hello')

loop.start()


# @client.event
# async def on_ready():
#     print(f'We have logged in as {client.user}')

# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return
    
#     if now == '3:56:00':
#         for x in range(level[str(random.randint(1, 5))]):
#             await message.channel.send("custom stamp")
#             time.sleep(2)

    
client.run(TOKEN)
