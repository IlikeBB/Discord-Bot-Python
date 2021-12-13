import discord, json, random, asyncio
from discord.ext import commands
from core.classes import Cog_Extension
from random import randint
import time
import datetime

class Main(Cog_Extension):
    @commands.command()
    async def 指令(self, ctx):
        embed=discord.Embed(title='指令大全', 
                            description='',color=0xecce8b)
        embed.add_field(name = f"Game指令 (賭盤或是投票使用)", inline=False, value="請直接打「$game」開啟Game help")
        embed.add_field(name = f"LuckyDraw指令 (抽獎使用)", inline=False, value="請直接打「$draw」開啟LuckyDraw help")
        embed.add_field(name = "噁心部份人指令1(尚未實裝)", inline=False, value="請直接打「${會員名字}」e.g. $阿布")
        embed.add_field(name = "相親相愛image(尚未實裝)", inline=False, value="請直接打「${user}x{user}」e.g. $阿布x右手")
        embed.add_field(name = "噁心部份人指令2", inline=False, value="請直接打「{會員名字}尊容」e.g. 阿布尊容")
        embed.add_field(name = "呼叫煞氣幫", inline=False, value="請直接打「煞氣幫」送出keyword指令\n也可以輸入「我要加入煞氣幫」加入煞氣幫")
        embed.add_field(name = "呼叫倒讚幫", inline=False, value="請直接打「倒讚幫」送出keyword指令")
        embed.add_field(name = "peko警告", inline=False, value="只要聊天內容裡面包含「peko」字眼就會出發很油警告")

        command_msg = await ctx.send(embed=embed)


    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"本機器人大約延遲 {round(self.bot.latency,5)} (ms)")

    @commands.command()
    async def 巴哈(self, ctx):
        await ctx.send(f"https://forum.gamer.com.tw/B.php?bsn=7650")

    @commands.command()
    async def dcard(self, ctx):
        await ctx.send(f"https://www.dcard.tw/topics/%E6%96%B0%E6%A5%93%E4%B9%8B%E8%B0%B7")

def setup(bot):
    bot.add_cog(Main(bot))