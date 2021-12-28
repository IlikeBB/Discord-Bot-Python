import discord, random, json, datetime, asyncio, os
from discord.ext import commands
from core.classes import Cog_Extension
from random import randint
import time
import datetime
with open('./setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

class MeMe(Cog_Extension):

    @commands.Cog.listener()
    async def  on_message(self, msg):
        await self.bot.wait_until_ready()
        user = msg.author
        user_id = msg.author.id
        message_id = msg.id
        content = msg.content
        message_channel = msg.channel.id
        #check onedrive
        try:
            if (msg.content.startswith("怕")) and (msg.author != self.bot.user):
                await asyncio.sleep(1)

                afarid = await  msg.channel.send(file=discord.File('./img/afarid.jpeg'))
                await asyncio.sleep(30)
                await afarid.delete()

            if ("我就爛" in msg.content) and (msg.author != self.bot.user):
                await asyncio.sleep(1)

                mybadbad = await  msg.channel.send(file=discord.File('./img/mybadbad.jpg'))
                await asyncio.sleep(30)
                await mybadbad.delete()

            if (msg.content.startswith("早安")) and (msg.author != self.bot.user):
                await asyncio.sleep(1)
                await msg.delete()
                list = random.choice(['./img/yagoomorning.webp','./img/uglyGG.png'])
                yagoomorning = await  msg.channel.send(file=discord.File(list))
                await asyncio.sleep(30)
                await yagoomorning.delete()

            if (msg.content.startswith("晚安")) and (msg.author != self.bot.user):
                await asyncio.sleep(1)
                await msg.delete()
                yagoonight = await  msg.channel.send(file=discord.File('./img/yagoonight.webp'))
                await asyncio.sleep(30)
                await yagoonight.delete()

            if (msg.content.startswith("午安")) and (msg.author != self.bot.user):
                await asyncio.sleep(1)
                await msg.delete()
                yagooafternoon = await  msg.channel.send(file=discord.File('./img/yagooafternoon.webp'))
                await asyncio.sleep(30)
                await yagooafternoon.delete()

            if ("老鼠" in msg.content or "勞贖" in msg.content) and (msg.author != self.bot.user):
                await asyncio.sleep(1)

                laushu = await  msg.channel.send(file=discord.File('./img/laushu.jpeg'))
                await asyncio.sleep(30)
                await laushu.delete()

            if ("歸剛" in msg.content) and (msg.author != self.bot.user):
                await asyncio.sleep(1)

                allday = await  msg.channel.send(file=discord.File('./img/allday.png'))
                await asyncio.sleep(30)
                await allday.delete()

            if ("血流成河"in msg.content) and (msg.author != self.bot.user):
                await asyncio.sleep(1)

                iwanttoseeblood = await  msg.channel.send(file=discord.File('./img/iwanttoseeblood.jpeg'))
                await asyncio.sleep(30)
                await iwanttoseeblood.delete()

            if (("<:" in msg.content)==False) and (("peko" in msg.content) or ("Peko" in msg.content)) and (msg.author != self.bot.user):
                await asyncio.sleep(1)
                await msg.delete()
                list = random.choice(os.listdir('peko/'))
                embed=discord.Embed(title="PEKO～ PEKO～", description='HA↗HA↗HA↗～' , color=0xecce8b)
                if "gif" in list:
                    bot_msg = await  msg.channel.send(file=discord.File('./peko/'+list))
                else:
                    file = discord.File(f"./peko/"+list, filename="image.png")            
                    embed.set_image(url="attachment://image.png")
                    peko = await msg.channel.send(file=file, embed=embed)
                await asyncio.sleep(30)
                await peko.delete()

            if 'tako'==msg.content and msg.author != self.bot.user:
                await msg.delete()
                # print('pass')
                # print(os.listdir('tako/'))
                await asyncio.sleep(1)
                tako_show = random.choice(os.listdir('tako/'))
                print(tako_show)
                tako = await  msg.channel.send(file=discord.File('./tako/'+tako_show))
                await asyncio.sleep(30)
                await tako.delete()

            if ("不想" in msg.content and "色色" in msg.content) and msg.author != self.bot.user:
                await asyncio.sleep(1)
                dontwanthorny = await  msg.channel.send(file=discord.File('./img/dontwanthorny.jpg'))
                await asyncio.sleep(30)
                await dontwanthorny.delete()

            elif ("想色色" in msg.content) and msg.author != self.bot.user:
                await asyncio.sleep(1)
                canwanthorny = await  msg.channel.send(file=discord.File('./img/canwanthorny.jpg'))
                await asyncio.sleep(30)
                await canwanthorny.delete()
        except:
            pass

def setup(bot):
    bot.add_cog(MeMe(bot))