from asyncio.tasks import sleep
import discord, json, random, asyncio
from discord.ext import commands
from core.classes import Cog_Extension
from random import randint
import time
import datetime

class Main(Cog_Extension):
    @commands.command()
    async def 指令(self, ctx):
        embed=discord.Embed(title='機器人功能字典', 
                            description='',color=0xecce8b)
        embed.add_field(name = "機器人指令", inline=False, 
                                            value="{0}{1}{2}{3}{4}{5}{6}".format("Game指令 (賭盤或是投票使用)  ```請直接打「$game」開啟Game help```",
                                                                                                                                    "LuckyDraw指令 (抽獎使用) ```請直接打「$draw」開啟LuckyDraw help```",
                                                                                                                                    "查詢瑟瑟幣指令[1] ```請直接打「$pt」開啟瑟瑟幣狀態列```",
                                                                                                                                    "贈送瑟瑟幣指令[2] ```請直接打「$gpt {tage某人}, {要送多少瑟瑟幣}」贈送瑟瑟幣\n e.g: $gpt @布里愛, 100```",
                                                                                                                                    "瑟瑟幣排行指令[3] ```請直接打「$prank」```",
                                                                                                                                    "噁心部份人指令[1] (尚未實裝) ```請直接打「${會員名字}」e.g. $阿布```",
                                                                                                                                    "噁心部份人指令[2] ```請直接打「{@會員名字}尊容」e.g. @布理愛尊容```",
                                                                                                                                    "相親相愛image(尚未實裝) ```請直接打「${user}x{user}」e.g. $阿布x右手```"
                                                                                                                                    )
                                            )
        embed.add_field(name = "幫會指令", inline=False, 
                                            value="{0}{1}{2}".format("呼叫煞氣幫  ```請直接打「煞氣幫」送出keyword指令\n也可以輸入「我要加入煞氣幫」加入煞氣幫```",
                                                                                                                                                "呼叫倒讚幫 ```請直接打「倒讚幫」送出keyword指令```",
                                                                                                                                                "加入中指幫 ```請直接打「我要加入中指幫」送出keyword指令```"
                                                                                                                                                )
                                            )                   
        embed.add_field(name = "關鍵字觸發", inline=False, 
                                            value="{0}".format("peko警告  ```只要聊天內容裡面包含「peko」字眼就會出發很油警告```"
                                                                                    )
                                            )   
        embed.add_field(name = "========機器人功能========", inline=False, 
                                            value="-")
        embed.add_field(name = "釘選功能", inline=False, 
                                            value="只要對任一聊天訊息點擊「📌」即可釘選訊息\n再次點擊「📌」收回即可收回釘選")
        embed.add_field(name = "=====第三方機器人指令=====", inline=False, 
                                            value="「#rank」查詢現在等級 「#top」查詢排行榜")

        command_msg = await ctx.send(embed=embed)
        await asyncio.sleep(60)
        await command_msg.delete()

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