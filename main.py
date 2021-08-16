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


#Join event
@bot.event
async def on_member_join(member):
    print(f'{member} has joined the country.')

#kick command
re = 'Reason:'
@bot.command()
async def kick(ctx, member : discord.Member, *, re, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'{member} has been deported from this country.')

#Leave event
@bot.event
async def on_member_remove(member):
    print(f'{member} has left this country')

#Ban/Unban command
@bot.command()
async def ban(ctx, member : discord.Member, *, reason=''):
    await member.ban(reason=reason)
    if reason == '':
       await ctx.send(f'{member} has been exiled from this country for being treason.') 
    else:
        await ctx.send(f'{member} has been exiled from this country for being {reason}.')

@bot.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) ==  (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'{user.mention} has been accepted back into the country.')
            return




bot.run(TOKEN)
