import discord, random, json, datetime, asyncio
from discord.ext import commands
from core.classes import Cog_Extension
from random import randint
import time
import datetime

client_dict = {
    "阿水沝水水": 527396560116383761,
    "綿羊": 916549421653721118,
    "右手": 539792067245768704,
    "阿布布里": 395199000640225281,
    "微微":480388351166382124,
    "龐克":859450432480608267,
    "赤冥":541279740414263308

}
class Compose_photo(Cog_Extension):
    pass



def setup(bot):
    bot.add_cog(Compose_photo(bot))