import discord, random, json, datetime, asyncio, os
from discord.ext import commands
from core.classes import Cog_Extension
from random import randint
import time
import datetime
with open('./setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

class Event(Cog_Extension):

    @commands.Cog.listener()
    async def  on_message(self, msg):
        await self.bot.wait_until_ready()
        user = msg.author
        user_id = msg.author.id
        message_id = msg.id
        content = msg.content
        message_channel = msg.channel.id
        #check onedrive
        face_stack = {'數字人': , 
                        '布里阿布':, 
                        '綿羊': , 
                        '沝阿水': ,
                        '東東':,
                        '微微':,
                        '回鍋':,
                        '阿如':,
                        'CM':,
                        '赤冥':,
                        '謎漾':,
                        '右手':}

        if msg.channel.id==:
            if ("one" in msg.content) and (msg.author != self.bot.user):
                await msg.channel.send('test2')
                await asyncio.sleep(5)

        keyword = ['None', 'None2', 'None3', 'None4']
        if "倒讚幫" == msg.content  and msg.author != self.bot.user:
            await msg.delete()
            await msg.channel.send('<@&> 站起來!! 我們的敵人在上面 狠狠地踩爛他')
            await asyncio.sleep(5)
        # 龐克區
        try:
            if msg.content=="煞氣幫" and (msg.author.id ==) and msg.author != self.bot.user:
                list = random.choice(['子民們站起來 龐董說話了!!','股東你好 請問有事嗎?','龐董你好.. 有事請tag 阿如, 阿布, CF', '又想踩阿水了嗎?'])
                await msg.add_reaction('👍')
                await msg.channel.send(list)
                await asyncio.sleep(5)

            elif msg.content=="煞氣幫" and ( in [y.id for y in user.roles])==False and msg.author != self.bot.user:
                list = random.choice(['該舔ㄍ廣播只有帥氣龐克幫主可以使用! 請加入煞氣幫! 大聲喊出! 「我要加入煞氣幫」'])
                await msg.channel.send(list)
                await asyncio.sleep(5)
                await msg.delete()
            
            elif msg.content=="煞氣幫" and ( in [y.id for y in user.roles])==True and msg.author != self.bot.user:
                list = random.choice(['請開始歌頌龐董贊歌 玉樹臨風 瀟灑倜儻...', '我龐董說甚麼都是對的 你們通通下去' ,'感謝龐董又幫台灣GDP上升了幾個百分點'])
                await msg.channel.send(list)
                await asyncio.sleep(5)

            if msg.content=="我要加入煞氣幫" and (msg.author.id !=):
                var = discord.utils.get(msg.guild.roles, name = "煞氣幫")
                await msg.author.add_roles(var)
                await msg.channel.send(f"<@>幫主!! <@{user_id}>剛剛加入<@&>了")
            
            elif (len(msg.content)==7) and (msg.author.id !=):
                if ("我要加" in msg.content) and ("幫" in msg.content):
                    var = discord.utils.get(msg.guild.roles, name = "煞氣幫")
                    await msg.author.add_roles(var)
                    send_list =  random.choice([f"歡迎加入煞氣幫<@{user_id}>！ 我知道加入煞氣幫是一個很令人興奮的事情，所以打錯字了", f"唉嘿～還想噁心龐董，換我噁心你，歡迎<@{user_id}>加入煞氣幫！！"])
                    t = await msg.channel.send(send_list)
                    await asyncio.sleep(5)
                    await msg.delete()
                    await t.delete()
                    await msg.channel.send(f"<@>幫主!! <@{user_id}>剛剛加入<@&>了")
        except:
            pass
            # Embed edit
        try:
            if msg.content =='龐克尊容'and msg.author != self.bot.user:
                # await msg.channel.send("該功能測試中 可能會有點延遲")
                # await asyncio.sleep(1)
                user = await self.bot.fetch_user()
                # await asyncio.sleep(1)
                pfp = user.avatar_url
                # pfp = 'https://cdn.discordapp.com/avatars/859450432480608267/79186671bb2e5097c1d8a4f1fc4d2437.png'
                print(pfp)
                # await asyncio.sleep(1)
                print(pfp)
                embed=discord.Embed(title="偉大的龐董尊容", description='玉樹臨風 瀟灑倜儻 奠定細雨百年基柱' , color=0xecce8b)
                embed.set_image(url=(pfp))
                await msg.channel.send(embed=embed)


            elif (msg.content[-2::]=='尊容') and (msg.content[0:-2] in  str(face_stack.keys()))and msg.author != self.bot.user:
                for i in face_stack:
                    if msg.content[0:-2] in i:
                        user = await self.bot.fetch_user(face_stack[i])
                        pfp = user.avatar_url
                        embed=discord.Embed(title=f"{user.name}尊容", description='' , color=0xecce8b)
                        embed.set_image(url=(pfp))
                        t = await msg.channel.send(embed=embed)
                        await asyncio.sleep(30)
                        await t.delete()
                        await msg.delete()

            elif "peko" in msg.content and msg.author != self.bot.user:
                print('pass')
                await asyncio.sleep(1)
                list = random.choice(["http://i2.hdslb.com/bfs/archive/be748ba0e1659d958b0f29c902b200e86dbea9a6.jpg", 
                                      "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSMay5DKuIGKusup7xEGoQnmwb9Bqmm336KSg&usqp=CAU",
                                      "http://i0.hdslb.com/bfs/archive/46660bdb9670ea6541aa9e4102c2615da6a05f6c.jpg"])
                embed=discord.Embed(title="PEKO～ PEKO～", description='HA↗HA↗HA↗～' , color=0xecce8b)
                embed.set_image(url=list)
                bot_msg = await msg.channel.send(embed=embed)
                await asyncio.sleep(5)
                await bot_msg.delete()
                await asyncio.sleep(4)
            
            elif 'tako'==msg.content and msg.author != self.bot.user:
                await msg.delete()
                # print('pass')
                # print(os.listdir('tako/'))
                await asyncio.sleep(1)
                tako_show = random.choice(os.listdir('tako/'))
                print(tako_show)

                await  msg.channel.send(file=discord.File('./tako/'+tako_show))
                
        except:
            pass
        
        # 噁心人專用
        if (msg.author.id in [])and msg.author != self.bot.user:
            send = random.randint(0,100)
            await asyncio.sleep(1)
            if send in [0,10,20,30,40,50,60,70,80,90,100]:
                choice = random.choice(['<:maplelovelovejump:884738023764398121>','🥳'])
                await msg.add_reaction(choice)
            
            elif send in [5, 25 , 45, 65, 85]:
                await asyncio.sleep(1)
                choice = random.choice(['布里愛礦泉水', '7414團長' ,'座右銘-我還沒死爽','倒讚教主'])
                await msg.reply(choice)
            

        # if (msg.author.id in [531100369334304798])and msg.author != self.bot.user:
        #     send = random.randint(0,100)
        #     if send in [0,10,20,30,40,50,60,70,80,90,100]:
        #         await msg.add_reaction('<:arutel2:885478709195309096>')

        # if (msg.author.id in [859450432480608267])and msg.author != self.bot.user:
        #     await msg.add_reaction('<:mapleMVP:886565466712186920>')

        # bad_emjio = [725714853872009216]
        # if (msg.author.id in bad_emjio)and msg.author != self.bot.user:
        #     await msg.add_reaction('<:holofriend:902538169076035594>')


        # 管理綿羊開車頻道用
        if msg.channel.id==:
            if (("http" in msg.content)==False) and msg.author != self.bot.user:
                await msg.delete()

        if "!test." in msg.content and msg.author != self.bot.user:
            await msg.channel.send(f'{user} - {user_id} - {message_id} - {content} - {message_channel}')

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        await asyncio.sleep(1)
        self.channel = self.bot.get_channel()

        emoji = reaction.emoji
        # if (emoji =='👎' )and (user.id==395199000640225281):
        if (emoji =='👎' )and user != self.bot.user:
            send = random.randint(0,100)
            if send in [0,10,20,30,40,50,60,70,80,90,100]:
                embed = discord.Embed(title = "", description = f"<@{user.id}>", color = 0x00ff00) #creates embed
                embed.set_image(url = "https://cdn.discordapp.com/attachments/914780104704536576/918327038128046100/GG.jpg")
                t = await self.channel.send(embed=embed)
                await asyncio.sleep(10)
                await t.delete()

        elif (emoji =='🖕' ) and user != self.bot.user:
            send = random.randint(0,100)
            if send in [0,10,20,30,40,50,60,70,80,90,100]:
                embed = discord.Embed(title = "", description = f"<@{user.id}>", color = 0x00ff00) #creates embed
                embed.set_image(url = "https://cdn.discordapp.com/attachments/914780104704536576/918372755613818900/bad_nausea.png")
                t = await self.channel.send(embed=embed)
                await asyncio.sleep(10)
                await t.delete()



def setup(bot):
    bot.add_cog(Event(bot))
