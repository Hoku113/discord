import discord
from discord.ext import tasks
from datetime import datetime

TOKEN = ""
CHANNEL_ID = 

client = discord.Client()

@tasks.loop(seconds=1123200)
async def loop():
    now = datetime.now().strftime('%H:%M')
    if now == '21:45':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send("15分後に会議があります。参加することを忘れないように")

loop.start()
client.run(TOKEN)