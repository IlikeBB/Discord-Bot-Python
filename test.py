import discord
import json, asyncio, datetime, random, os
from discord.ext import commands

with open('./setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)


bot = commands.Bot(command_prefix='$') #build bot parameters
    

@bot.event
async def on_ready():
    print(">> Bot is online <<")

if __name__ == '__main__':
    bot.run(jdata["TOKEN"])
    # bot.run('token')