import discord, random, json, datetime, asyncio
from discord.ext import commands
from core.classes import Cog_Extension
from random import randint
import time
import datetime
with open('./setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)
class Task(Cog_Extension):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.counter = 0
        self.counter2 = 0
        async def time_msg_send():
            await self.bot.wait_until_ready()
            while not self.bot.is_closed():
                await asyncio.sleep(5)
                now_time = datetime.datetime.now().strftime("%H%M")
                try:#跳旗幟command
                    if ((now_time =='2055') or (now_time=='1855') or (now_time=='1155')) and (self.counter==0):
                        if self.counter==1:
                            break
                        self.counter = 1
                        self.channel = self.bot.get_channel(406283404221612054)
                        await self.channel.send(f"<@&854675831548936212> <@&854676138772660226> <@&911040145698979872><@&911040436922097725>各位乖寶寶們已經 {now_time[0:2]} : {now_time[2::]}了！！！！準備跳棋囉！！！！")
                        await asyncio.sleep(5)
                    elif  ((now_time =='2101') or (now_time=='1901') or (now_time=='1201')) and (self.counter!=0):
                        self.counter = 0
                        await asyncio.sleep(5)
                except:
                    pass
                try:#carriage command
                    end_time = datetime.datetime.now().strftime("%m%d")
                    now_time = datetime.datetime.now().strftime("%H%M")
                    if ((now_time =='2115')) and (end_time!="0112") and (bool(jdata['carriage_status']) == True) and (self.counter2!=1):
                        if self.counter2==1:
                            break
                        self.counter2 = 1
                        self.channel = self.bot.get_channel(406283404221612054)
                        await self.channel.send("各位寶寶們要記得黃金馬車的點名喔！！！！！")
                        await asyncio.sleep(5)

                    elif  (now_time =='2116') and (self.counter2!=0):
                        self.counter2 = 0
                        await asyncio.sleep(5)
                    elif end_time=="0112":
                        jdata['carriage_status'] = "False"
                        with open('./setting.json', 'w', encoding='utf8') as jfile:
                            json.dump(jdata, jfile, indent=4)
                        await asyncio.sleep(5)
                except:
                    pass
        self.flag_ = self.bot.loop.create_task(time_msg_send())


def setup(bot):
    bot.add_cog(Task(bot))