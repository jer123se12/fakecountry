import discord
from discord.ext import commands
import json
import datetime

TOKEN=""

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
async def pingReply(ctx):
    timeSent = msg.created_at.strftime("%S.%f")
    timeNow = datetime.datetime.utcnow().strftime("%S.%f")
    timeDiff = float(timeNow) - float(timeSent)
    response  = str(timeDiff*1000).replace(".", "")
    response = "Ping: **" + response[:3] + "ms" +"**"
    await ctx.channel.send(response)

bot.run(TOKEN)

