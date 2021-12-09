import discord, json, random
from discord.ext import commands
from core.classes import Cog_Extension
from random import randint
import time
import datetime

class MSG(Cog_Extension):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.stack
    # @commands.command()
    # async def 綿羊(self, ctx):
    #     random_pic = random.choice(["綿羊跟謎樣貼貼", "好耶 30cm", "%%綿羊"])
    #     await ctx.send(random_pic)

    # @commands.command()
    # async def 數字人(self, ctx):
    #     # await ctx.send(file = pic)
    #     random_pic = random.choice(["ㄩㄇ", "信數字人得永生", "數字人我婆", "數字人我公", "%%數字人"])
    #     await ctx.send(random_pic)

    # @commands.command()
    # async def 阿布(self, ctx):
    #     # await ctx.send(file = pic)
    #     random_pic = random.choice(["倒讚布 甘蔗布 翹班布 <@395199000640225281>"])
    #     await ctx.send(random_pic)

    @commands.Cog.listener()
    async def  on_message(self, msg):
        await self.bot.wait_until_ready()
        if 'reply' == msg.content and msg.author!=self.bot.user:
            await msg.reply("Check Msg = " + msg.content )

        if '$7414' == msg.content and msg.author!=self.bot.user:
            await msg.reply("你才7414" )


def setup(bot):
    bot.add_cog(MSG(bot))