import discord
import os
from discord.ext import commands
import json
import datetime
import math
from dotenv import load_dotenv

load_dotenv()
TOKEN=os.getenv("TOKEN")

prefix = "$"
bot = commands.Bot(command_prefix=prefix)

@bot.event
async def on_message(message):
    global msg
    msg = message
    await bot.process_commands(message)

@bot.command(
    name="ping",
    help = "Sends the ping of the bot back"
    )
async def pingReply(ctx, *args):
    timeSent = msg.created_at.strftime("%S.%f")
    timeNow = datetime.datetime.utcnow().strftime("%S.%f")
    timeDiff = float(timeNow) - float(timeSent)
    response  = math.floor(timeDiff*1000000)/1000
    response = "Ping: **" + str(response) + "ms" +"**"
    await ctx.channel.send(response)
@bot.command(
    name="sort",
    help = "sorts an array seperated by ','"
    )
async def sorting(ctx, message):
    message=message.split(',')
    l=[]
    for i in message:
        if i.isdigit():
            l.append(int(i))
    await ctx.channel.send(','.join([str(a) for a in sorted(l)]))



bot.run(TOKEN)
