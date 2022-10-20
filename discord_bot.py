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
level = level[str(random.randint(1, 5))]

TOKEN = "<token>"
CHANNEL_ID = "<channel_id>"
SERVER_ID = "<server_id>"

client = discord.Client()

@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")

@tasks.loop(seconds=1)
async def loop():

    # start client
    await client.wait_until_ready()

    # get channel
    channel = client.get_channel(CHANNEL_ID)

    now = datetime.now()
    now = now.strftime('%H:%M')

    if now == now:
        # user = discord.Member()
        await channel.send(f"{level}このスタンプ")
        guild = client.get_guild(SERVER_ID)
        
        # check
        print(guild.members)
        
        # for x in range(1):
        #     await channel.send('<a:parot:987402234595803217>')
        #     time.sleep(1)

        #     if x == x :
        #         await channel.send("送信完了('◇')ゞ")
        #         break
        #     else:
        #         x += 1
            
loop.start()
loop.stop()

client.run(TOKEN)