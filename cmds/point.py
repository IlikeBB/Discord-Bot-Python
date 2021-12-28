import discord, random, json, datetime, asyncio
from discord import message
from discord.ext import commands
# from firebase_admin import db
from core.classes import Cog_Extension
from random import randint
import datetime



class Point(Cog_Extension):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.counter = 0
        self.get_point_msg=None
        async def point_dete():
            await self.bot.wait_until_ready()
            while not self.bot.is_closed():
                self.channel = self.bot.get_channel(914680532909064323)
                await asyncio.sleep(5)
                # create new member
                # 每日日期檢測 跨日自動更新訊息
                now_time = (datetime.datetime.now().strftime("%Y%m%d%H%M"))
                date_check = now_time[0:8]
                check_index = self.ref.child("CHECK_SET").get()
                lateset_date = str(check_index['POINT_TODAY'])
                if (lateset_date!= date_check) and (now_time[-1]=='3'):
                    try:
                        msg_id = check_index['POINT_MSG']
                        msg = await self.channel.fetch_message(msg_id)
                        await msg.delete()
                        ID_values = self.ref.child("ID").get() #type.String
                        ID_stack = [i for i in ID_values]
                        for id in ID_stack:
                            if ID_values[id]["TODAY_STATUS"]==True:
                                new_data = {"TODAY_STATUS": False}
                                self.ref.child("ID").child(id).update(new_data)
                    except:
                        print("INIT ERROR: First Create......")
                        
                    embed=discord.Embed(title="每日點名領瑟瑟幣", 
                                        description='',color=0xecce8b)
                    embed.add_field(name =(now_time[0:4]+'/'+now_time[4:6]+'/'+now_time[6:8]), inline=False, value = '------------------------------------')
                    embed.add_field(name ="請點擊<:maplecanhorny:903265336743301181>領取點數", inline=False, value = '------------------------------------')
                    embed.add_field(name ="目前資料庫每5分鐘更新一次，可以使用「$pt」查訊現在擁有的點數", inline=False, value = '------------------------------------')
                    embed.add_field(name ="※當前瑟瑟幣主要用於抽獎時的參加費用\n※另外也可以拿來當作對於社群功能的參與程度XD..\n※未來會加入下注系統提供大家下注，如果有甚麼idea也可以告訴我~\n", inline=False, value = '------------------------------------')
                    self.get_point_msg =  await self.channel.send(embed=embed)
                    await self.get_point_msg.add_reaction('<:maplecanhorny:903265336743301181>')
                    
                    print(self.get_point_msg.id)
                    self.ref.child("CHECK_SET").update({"POINT_MSG": str(self.get_point_msg.id), "POINT_TODAY": str(date_check)})
                    await asyncio.sleep(5)
                else:
                    pass
                # if now_time[-1] in ['3','6','9'] and self.counter==0:
                if now_time[-1] in ['5','0']:
                    await asyncio.sleep(1)
                    ID_values = self.ref.child("ID").get() #type.String
                    msg = await self.channel.fetch_message(int(check_index["POINT_MSG"]))
                    await asyncio.sleep(1)
                
                    for idx, reactions in enumerate(msg.reactions):
                        # print(idx)
                        if idx==0:
                            # print("RUN database")
                            # on_reaction listener check
                            all_participants = [str(user.id) async for user in reactions.users() if user != self.bot.user]
                            # print('all_participants: ', len(all_participants), '\n---------------------------------------------------------')
                            for id_name in all_participants:
                                ID_stack = [i for i in ID_values]
                                await asyncio.sleep(1)

                                if (id_name in ID_stack)==False:
                                    raw_data= {
                                        id_name :{
                                            "MONEY":100, 
                                            "FINAL_DATE": date_check, 
                                            "WIN_COUNT":0, 
                                            "LOSE_COUNT":0,  
                                            "TODAY_STATUS": True, 
                                            }
                                        }
                                    self.ref.child("ID").update(raw_data)

                                elif ID_values[id_name]["TODAY_STATUS"]==False:
                                    current_point = ID_values[id_name]["MONEY"]
                                    new_data = {"FINAL_DATE": date_check, "MONEY": (current_point+100), "TODAY_STATUS": True}
                                    self.ref.child("ID").child(id_name).update(new_data)
                    
                    # print("update data!!!")
                #     print('updata finished!!!')
                #     await asyncio.sleep(2)
                    

        self.flag_ = self.bot.loop.create_task(point_dete())

class Point_Listener(Cog_Extension):
    @commands.Cog.listener()
    async def  on_message(self, msg):
        await self.bot.wait_until_ready()
        user = msg.author
        user_id = msg.author.id
        message_id = msg.id
        content = msg.content
        message_channel = msg.channel.id

        if (msg.content.startswith("$pt") or msg.content.startswith("$PT"))and (msg.author != self.bot.user):
            await asyncio.sleep(1)
            ID_values = self.ref.child("ID").get()
            ID_stack = [i for i in ID_values]
            # print(user_id, ID_stack)
            if str(user_id) in ID_stack:
                embed=discord.Embed(title=f"<:maplecanhorny:903265336743301181>", description=f'<@{user_id}> - 瑟瑟幣查詢' , color=0xecce8b)
                user_id = str(user_id)
                embed.add_field(name ="瑟瑟幣數量", inline=False, value = ID_values[user_id]["MONEY"])
                embed.add_field(name ="最後領取時間", inline=False, value = ID_values[user_id]['FINAL_DATE'])
                embed.add_field(name ="歐洲次數", inline=False, value = int(ID_values[user_id]['WIN_COUNT']))
                embed.add_field(name ="非洲次數", inline=False,value = int(ID_values[user_id]['LOSE_COUNT']))
                bot_msg = await msg.channel.send(embed=embed)
                await asyncio.sleep(60)
                await msg.delete()
                await bot_msg.delete()
            else:
                temp = await msg.channel.send(f"<@{user_id}>資料庫尚無您的資料，請到 「📢每日point-coin領取區」進行點名過5分鐘後在使用查詢功能")
                await asyncio.sleep(10)
                await msg.delete()
                await temp.delete()
        if (msg.content.startswith("$spt") or msg.content.startswith("$SPT"))and (user_id in [725714853872009216, 395199000640225281, 531100369334304798]):
            await asyncio.sleep(1)
            ID_values = self.ref.child("ID").get()
            print("ADD--------------------------------------------------------------------")
            add_point_list = msg.content[5::].split(',')
            add_point_list[-1] = int(add_point_list[-1].replace('-',''))
            add_point_list[0] = f'{(((add_point_list[0])[3:21]).replace(" ",""))}'
            try:
                user_ = add_point_list[0]
                point_ = int(ID_values[str(user_)]["MONEY"])
                add_point = int(add_point_list[1])
                current_point = ID_values[user_]["MONEY"]
                self.ref.child("ID").child(user_).update({"MONEY": (current_point+add_point)})
                temp = await msg.channel.send(f"已經贈送{int(add_point_list[1])}個瑟瑟幣給<@{add_point_list[0]}>\n [{current_point} → {current_point+add_point}]")
                await asyncio.sleep(60)
                await msg.delete()
                await temp.delete()
            except:
                await msg.channel.send("該會員尚未註冊資料庫資料或是不存在喔~~")

        if (msg.content.startswith("$dpt") or msg.content.startswith("$DPT"))and (user_id in [725714853872009216, 395199000640225281, 531100369334304798]):
            await asyncio.sleep(1)
            ID_values = self.ref.child("ID").get()
            # print("ADD--------------------------------------------------------------------")
            add_point_list = msg.content[5::].split(',')
            add_point_list[-1] = str(add_point_list[-1]).replace('-','')
            add_point_list[-1] = int(add_point_list[-1])
            add_point_list[0] = str(((add_point_list[0])[3:21]).replace(" ",""))
            # try:
            user_ = add_point_list[0]
            point_ = int(ID_values[str(user_)]["MONEY"])
            add_point = int(add_point_list[1])
            current_point = ID_values[user_]["MONEY"]
            self.ref.child("ID").child(user_).update({"MONEY": (0 if (current_point-add_point)<0 else  current_point-add_point)})
            temp = await msg.channel.send(f"已經向<@{add_point_list[0]}>扣款{int(add_point_list[1])}個瑟瑟幣\n [{current_point} → {(0 if (current_point-add_point)<0 else  current_point-add_point)}]")
            await asyncio.sleep(60)
            await msg.delete()
            await temp.delete()
            # except:
            #     await msg.channel.send("該會員尚未註冊資料庫資料或是不存在喔~~")
        if (msg.content.startswith("$gpt") or msg.content.startswith("$GPT")) and (msg.author != self.bot.user):
            ID_values = self.ref.child("ID").get()
            gift_stack = (msg.content[5::]).split(",")
            gift_A = str(user_id)
            gift_B = str(((gift_stack[0])[3:21]).replace(" ",""))
            gift_stack[-1] = str(gift_stack[-1]).replace('-','')
            gift_stack[-1] = int(gift_stack[-1])
            # print(gift_A, gift_B)
            try:
                if gift_A!=gift_B:
                    if ID_values[gift_A]["MONEY"]>=int(gift_stack[-1]):
                        A_current_point = ID_values[gift_A]["MONEY"]
                        B_current_point = ID_values[gift_B]["MONEY"]
                        self.ref.child("ID").child(gift_A).update({"MONEY": (0 if (A_current_point-int(gift_stack[-1]))<0 else  A_current_point-int(gift_stack[-1]))})

                        self.ref.child("ID").child(gift_B).update({"MONEY": (B_current_point+int(gift_stack[-1]))})


                        gift_msg = await msg.reply(f'<@!{int(gift_A)}> 已經贈送{int(gift_stack[-1])}個瑟瑟幣給<@!{int(gift_B)}>')
                        await asyncio.sleep(15)
                        await gift_msg.delete()
                        await msg.delete()
                    else:
                        gift_msg = await msg.reply(f'<@!{int(gift_A)}> 您沒辦法送這麼多瑟瑟幣喔. 您現在只有{ID_values[gift_A]["MONEY"]}個瑟瑟幣')
                        await asyncio.sleep(15)
                        await gift_msg.delete()
                        await msg.delete()
                else:
                        gift_msg = await msg.reply(f'<@!{int(gift_A)}> 請不要贈送瑟瑟幣給自己喔！給你一個刀粉印章')
                        await asyncio.sleep(15)
                        await gift_msg.delete()
                        await msg.delete()
            except:
                    error_msg = await msg.reply("請確認有沒有打錯格式或是當前被贈送方並沒有在資料庫上建檔. e.g. $gpt {tage某人}, {瑟瑟幣數量}")
                    await asyncio.sleep(15)
                    await error_msg.delete()
                    await msg.delete()

        if msg.content.startswith("$prank") or msg.content.startswith("$PRANK"):
            await asyncio.sleep(1)
            ID_values = self.ref.child("ID").get()
            ID_stack = [i for i in ID_values]

            embed=discord.Embed(title="<:maplecanhorny:903265336743301181>  瑟瑟幣排行榜", description='',color=0xecce8b)
            scores=[]
            for id in ID_stack:
                scores.append((f'<@{int(id)}>',':  ', ID_values[id]["MONEY"],' $','\n'))
            scores.sort(key = lambda s: s[2], reverse=True)
            scores = scores[0:10]
            for idx, i in enumerate(scores):
                scores[idx] = ''.join(f'{x}' if type(x)==int else x for x in i )
            strs =''.join(scores)
            embed.add_field(name ="```前10名```", inline=False, value = strs)
            coin_rank = await msg.channel.send(embed=embed)
            await asyncio.sleep(30)
            await coin_rank.delete()
            await msg.delete()
def setup(bot):
    bot.add_cog(Point(bot))
    bot.add_cog(Point_Listener(bot))
    pass