import discord, random, json, datetime, asyncio
from discord.ext import commands
from core.classes import Cog_Extension
from random import randint
import time
import datetime

class Game(Cog_Extension):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.stack
        self.game_leader = None
        self.game_init_msg = None
        self.reaction_stack = ['0️⃣','1️⃣','2️⃣','3️⃣','4️⃣','5️⃣','6️⃣','7️⃣','8️⃣','9️⃣']
        self.participant_table = {}
        self.Betting_plate=None
        self.PLAY_MESSAGE_EDIT = {"Game_Main": None, "Game_title": None, "Game_Activate": False, "Game_End_time": False, "End_time": None}
    @commands.Cog.listener()
    async def  on_message(self, msg):
        await self.bot.wait_until_ready()
        now_time = (datetime.datetime.now().strftime("%H%M")).replace(' ','')
        user = msg.author
        self.user = msg.author
        # --------------------------------------------------
        # 開賭盤 <如果沒接續edit stack 會出現help
        # 開賭盤 {title}, {condition}, {Closing time}, {condition1}, {condition2}, {condition3}.... Max 10
        # 開賭盤 {標題}, {條件}, {收盤時間}, {條件1}, {條件2}, {條件3}.... 最大 10
        # 開賭盤 老黑7414團, 誰會先死, 2130, 阿布, 赤冥, 死靈, 雅, 龐克, 水水....
        #                         reaction  zero, one, two, three ,four, five....
        # --------------------------------------------------
        if msg.content == "$game" and msg.author != self.bot.user:
            await msg.delete()
            embed=discord.Embed(title='開Game教學', 
                                description='',color=0xecce8b)
            # embed.add_field(name = "commands", inline=False, value="$game {title}, {condition}, {Closing time}, {cond01}, {condi2}, {cond3}.... Max 10")
            # embed.add_field(name = "指令", inline=False, value="$game {標題}, {條件}, {收盤時間}, {條件1}, {條件2}, {條件3}.... 最多10個條件")
            # embed.add_field(name = "範例(建議直接複製下面的範例指令修改)", inline=False, value="$game 老黑7414團, 誰會先死, 2130, 阿布, 赤冥, 死靈, 雅, 龐克, 水水")
            embed.add_field(name = "commands", inline=False, value="$game {title}, {condition}, {Closing time}, {cond01}, {condi2}, {cond3}.... Max 10")
            embed.add_field(name = "指令", inline=False, value="$game {標題}, {條件}, {條件1}, {條件2}, {條件3}.... 最多10個條件")
            embed.add_field(name = "範例(建議直接複製下面的範例指令修改)", inline=False, value="$game 老黑7414團, 誰會先死, 阿布, 赤冥, 死靈, 雅, 龐克, 水水")
            embed.add_field(name = "Game開啟後相關指令", inline=False, value="輸入「$list」可以查詢當前下注情況\n輸入「$end」可以提早收起Game或者輸入「$del」刪除Game(只有創立者可以使用)")
            Tutorials = await msg.channel.send(embed=embed)
            await asyncio.sleep(120)
            await Tutorials.delete()

        elif self.PLAY_MESSAGE_EDIT['Game_Activate'] == False:
            if msg.content[0:5]=="$game" and "$game" in msg.content and msg.author != self.bot.user:
                #開賭盤 老黑7414團, 誰會先死, 2130, 阿布, 赤冥, 死靈, 雅, 龐克, 水水
                await asyncio.sleep(1)
                message = msg.content
                game_setting = message[5::].split(',')
                print(game_setting[0], game_setting[1], len(game_setting[2].replace(' ','')), len(game_setting[3::]))
                if False:
                    pass
                # elif len(game_setting[2].replace(' ',''))!=4 or ":" in game_setting[2]:
                #     t = await msg.channel.send("時間格式有誤. 請確定輸入的時間是24小時制. example: 0800, 2100")
                #     await asyncio.sleep(15)
                #     await msg.delete()
                #     await t.delete()

                # elif len(game_setting[2].replace(' ',''))==4 and int(game_setting[2].replace(' ',''))>2400:
                #     t = await msg.channel.send("時間格式有誤. 請確定輸入的時間是24小時制. example: 0800, 2100")
                #     await asyncio.sleep(15)
                #     await msg.delete()
                #     await t.delete()
                # elif len(game_setting[3::])>10:
                elif len(game_setting[2::])>10:
                    t = await msg.channel.send("請確認設定的條件是否超過10個")
                    await asyncio.sleep(15)
                    await msg.delete()
                    await t.delete()

                else:
                    self.default_title = game_setting[0]
                    self.default_condition = game_setting[1]
                    # self.PLAY_MESSAGE_EDIT['End_time'] = game_setting[2].replace(' ','')
                    # self.default_condition_stack = game_setting[3::]
                    self.default_condition_stack = game_setting[2::]
                    await msg.delete()
                    self.game_leader = user
                    self.PLAY_MESSAGE_EDIT['Game_Activate'] = True
                    default_condition_dict ={}
                    for idx, i in enumerate(self.default_condition_stack):
                        default_condition_dict[i] = self.reaction_stack[idx]
            
                    embed=discord.Embed(title=self.default_title +' - '+ self.default_condition, 
                                        description='',color=0xecce8b)
                    for idx, i in enumerate(self.default_condition_stack):
                        embed.add_field(name =self.reaction_stack[idx]+'  '+ i, value = '-')
                    # embed.add_field(name = f"停止參與時間為{self.PLAY_MESSAGE_EDIT['End_time']}", inline=False, value="------------------------------------")
                    embed.add_field(name = "請點擊下方的Emoji參與!!\n請勿做重複的選擇!!\n創立者請好好檢查警告作弊仔XD", inline=False, value="------------------------------------")
                    embed.add_field(name = "可以輸入「$list」觀看參與情況\n創立者可以輸入「$end」結束Game或者輸入 「$del」刪除Game", inline=False, value="------------------------------------")
                    self.game_init_msg = await msg.channel.send(embed=embed)
                    for i in range(len(self.default_condition_stack)):
                        await self.game_init_msg.add_reaction(self.reaction_stack[i])
                    for i in self.default_condition_stack:
                        self.participant_table[i] = []
                    self.PLAY_MESSAGE_EDIT['Game_Main'] = self.game_init_msg
                    self.PLAY_MESSAGE_EDIT['Game_title'] = self.default_title +' - '+ self.default_condition

        elif  self.PLAY_MESSAGE_EDIT['Game_Activate']==True:
            if msg.content[0:5]=="$game":
                if len(msg.content)==5:
                    embed=discord.Embed(title='開Game教學', 
                                        description='',color=0xecce8b)
                    # embed.add_field(name = "commands", inline=False, value="$game {title}, {condition}, {Closing time}, {cond01}, {condi2}, {cond3}.... Max 10")
                    # embed.add_field(name = "指令", inline=False, value="$game {標題}, {條件}, {收盤時間}, {條件1}, {條件2}, {條件3}.... 最多10個條件")
                    # embed.add_field(name = "範例(建議直接複製下面的範例指令修改)", inline=False, value="$game 老黑7414團, 誰會先死, 2130, 阿布, 赤冥, 死靈, 雅, 龐克, 水水")
                    embed.add_field(name = "commands", inline=False, value="$game {title}, {condition}, {Closing time}, {cond01}, {condi2}, {cond3}.... Max 10")
                    embed.add_field(name = "指令", inline=False, value="$game {標題}, {條件}, {條件1}, {條件2}, {條件3}.... 最多10個條件")
                    embed.add_field(name = "範例(建議直接複製下面的範例指令修改)", inline=False, value="$game 老黑7414團, 誰會先死, 阿布, 赤冥, 死靈, 雅, 龐克, 水水")
                    embed.add_field(name = "Game開啟後相關指令", inline=False, value="輸入「$list」可以查詢當前下注情況\n輸入「$end」可以提早收起Game或者輸入「$del」刪除Game(只有創立者可以使用)")
                    Tutorials = await msg.channel.send(embed=embed)
                    await asyncio.sleep(120)
                    await Tutorials.delete()

                elif len(msg.content)!=5:
                    t = await msg.channel.send("當前已經有Game存在 請創立者刪除後再新增")
                    await asyncio.sleep(10)
                    await msg.delete()
                    await t.delete()   
            # 僅有使用者可以控制賭盤的exist
            # !commands dele game
            elif msg.content =="$del":
                if (self.game_leader ==user or user.id==725714853872009216):
                    END_TIME =None
                    t = await msg.channel.send("Game已經刪除...")
                    await msg.delete()
                    await self.game_init_msg.delete()
                    END_TIME =None
                    self.PLAY_MESSAGE_EDIT = {"Game_Main": None, "Game_title": None, "Game_Activate": False, "Game_End_time": False, "End_time": None} #
                    self.game_leader = None
                    self.game_init_msg = None
                    self.participant_table = {}
                    self.Betting_plate=None
                    await asyncio.sleep(5)
                    await t.delete()

                elif self.game_leader !=user:
                    await asyncio.sleep(2)
                    await msg.delete()
                    t = await msg.channel.send("親 您不是創立者喔～ 所以無法刪除Game")
                    await asyncio.sleep(5)
                    await t.delete()

            elif msg.content=='$reply' and self.PLAY_MESSAGE_EDIT['Game_End_time']==False:
                    # await msg.delete()
                    print('reply finish!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
                    await self.game_init_msg.reply("Game發生中!!!  請點擊上方的「按一下查看附件」參與Game. [現在的Game] :  " + self.default_title +' - '+ self.default_condition )
            
            elif msg.content =="$list":
                # 監聽reaction使用狀況(無視非設定內reaction反應)
                cache_msg = discord.utils.get(self.bot.cached_messages, id = self.game_init_msg.id)
                for reactions, condition1 in zip(cache_msg.reactions, self.participant_table):
                    self.participant_table[condition1]=[]
                    user_list = [user async for user in reactions.users() if user != self.bot.user]
                    for user in user_list:
                        self.participant_table[condition1].append(user.display_name)

                if self.PLAY_MESSAGE_EDIT['Game_End_time']==True:
                    title_ = 'Game List(End)'
                else:
                    title_ = 'Game List (該功能非常延遲 建議30秒查詢一次 以確保資料有更新)'
                embed=discord.Embed(title=title_,description=f'{self.default_title} - {self.default_condition}',color=0xecce8b)
                
                for idx, i in enumerate(self.participant_table):
                    embed.add_field(name = i, inline=False, value = self.participant_table[i])
                if self.PLAY_MESSAGE_EDIT['Game_End_time']==True:
                    name_ = f"已經結束. 停止參與. Game結果以目前Game List為主"
                else:
                    name_ = f"Game進行中."
                embed.add_field(name = name_, inline=False, value="------------------------------------")
                if self.PLAY_MESSAGE_EDIT['Game_End_time']==True:
                    self.Betting_plate= await msg.channel.send(embed=embed)
                    self.PLAY_MESSAGE_EDIT = {"Game_Main": None, "Game_title": None, "Game_Activate": False, "Game_End_time": False, "End_time": None} #
                    await msg.delete()
                    await self.game_init_msg.delete()
                    self.game_leader = None
                    self.game_init_msg = None
                    self.participant_table = {}
                    self.Betting_plate=None
                elif self.PLAY_MESSAGE_EDIT['Game_End_time']==False:
                    embed.add_field(name = "Game List 30秒後會自動關閉",inline=False, value="------------------------------------")
                    self.Betting_plate= await msg.channel.send(embed=embed)
                    await asyncio.sleep(30)
                    await msg.delete()
                    await self.Betting_plate.delete()
            # 假如賭盤已經收盤 建置game table指令提供查詢  
            
            elif (msg.content == "$end") and (self.game_leader ==user or user=="PuiPui-MoMoJUJU#0550"):
                if self.PLAY_MESSAGE_EDIT['Game_End_time']==False:
                    self.PLAY_MESSAGE_EDIT['Game_End_time']=True
                    t = await msg.channel.send("Game已經結束. 可以再次使用Game開新的局. 請輸入「$list」確認最終結果.")
                    await msg.delete()
                    await asyncio.sleep(1)

            print(self.PLAY_MESSAGE_EDIT["End_time"], now_time)

            # 需要使用即時檢測function

class Lucky(Cog_Extension):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.stack
        self.game_leader = None
        self.game_init_msg = None
        self.luckydraw_icon ='👏'
        self.participant_table = {}
        self.Betting_plate=None
        self.PLAY_MESSAGE_EDIT = {"Game_Title": None, "Numbers": None, "Reward": [],"Game_Activate": False, "Game_End_time": False, "End_time": None}
    @commands.Cog.listener()
    async def  on_message(self, msg):
        await self.bot.wait_until_ready()
        now_time = (datetime.datetime.now().strftime("%H%M")).replace(' ','')
        user = msg.author
        self.user = msg.author
        # print(self.PLAY_MESSAGE_EDIT)
        if msg.content == "$draw" and msg.author != self.bot.user:
            await msg.delete()
            embed=discord.Embed(title='開LuckyDraw教學', 
                                description='',color=0xecce8b)
            embed.add_field(name = "*Notice", inline = False, value="還沒正式啟用 請使用「$deldraw」刪除抽獎")
            embed.add_field(name = "commands", inline = False, value="$draw {title},{reward1},{reward2},{reward3},{reward4}...")
            embed.add_field(name = "指令", inline=False, value="$draw {標題}, {獎品1}, {獎品2}, {獎品3}, {獎品4}...")
            embed.add_field(name = "範例(建議直接複製下面的範例指令修改)", inline=False, value="$draw 阿布抽100E楓幣, 50E, 40E, 10E")
            embed.add_field(name = "LuckyDraw開啟後相關指令", inline=False, value="輸入「$start」可以開始抽獎或者輸入「$deldraw」刪除抽獎(只有創立者可以使用)")
            Tutorials = await msg.channel.send(embed=embed)
            await asyncio.sleep(120)
            await Tutorials.delete()

        elif self.PLAY_MESSAGE_EDIT['Game_Activate'] == False:
            if msg.content[0:5]=="$draw" and "$draw" in msg.content and msg.author != self.bot.user:
                await asyncio.sleep(1)
                message = msg.content
                if False:
                    pass
                else:
                    game_setting = message[5::].split(',')
                    
                    self.PLAY_MESSAGE_EDIT['Game_Title'] = game_setting[0]
                    self.PLAY_MESSAGE_EDIT['Reward'] = game_setting[1::]
                    await msg.delete()
                    self.game_leader = user
                    self.PLAY_MESSAGE_EDIT['Game_Activate'] = True
                    default_condition_dict = {}
                    for idx, i in enumerate(self.PLAY_MESSAGE_EDIT['Reward']):
                        default_condition_dict[i] = i
            
                    embed=discord.Embed(title=self.PLAY_MESSAGE_EDIT['Game_Title'], 
                                        description='',color=0xecce8b)
                    embed.add_field(name ="獎品清單", inline=False, value = '------------------------------------')
                    for idx, i in enumerate(self.PLAY_MESSAGE_EDIT['Reward']):
                        embed.add_field(name =i, value = '-')
                    embed.add_field(name = "請點擊下方的Emoji參與!!\n請勿做重複的選擇!!\n重複點選是沒有用的喔!!", inline=False, value="------------------------------------")
                    embed.add_field(name = "輸入「$start」可以開始抽獎或者輸入「$deldraw」刪除抽獎", inline=False, value="------------------------------------")
                    self.game_init_msg = await msg.channel.send(embed=embed)
                    await self.game_init_msg.add_reaction(self.luckydraw_icon)

        elif  self.PLAY_MESSAGE_EDIT['Game_Activate']==True:
            if msg.content[0:5]=="$draw":
                if len(msg.content)==5:
                    await msg.delete()
                    embed=discord.Embed(title='開LuckyDraw教學', 
                                        description='',color=0xecce8b)
                    embed.add_field(name = "commands", inline = False, value="$draw {title}, {condition},{number},{reward1},{reward2},{reward3},{reward4}...")
                    embed.add_field(name = "指令", inline=False, value="$draw {標題}, {中獎人數}, {獎品1}, {獎品2}, {獎品3}, {獎品4}...")
                    embed.add_field(name = "範例(建議直接複製下面的範例指令修改)", inline=False, value="$game 阿布抽100E楓幣, 3, 50E, 40E, 10E")
                    embed.add_field(name = "LuckyDraw開啟後相關指令", inline=False, value="輸入「$draw」可以開始抽獎或者輸入「$deldraw」刪除抽獎(只有創立者可以使用)")
                    Tutorials = await msg.channel.send(embed=embed)
                    await asyncio.sleep(120)
                    await Tutorials.delete()

                elif len(msg.content)!=5:
                    t = await msg.channel.send("當前已經有Game存在 請創立者刪除後再新增")
                    await asyncio.sleep(10)
                    await msg.delete()
                    await t.delete()   
            # 僅有使用者可以控制賭盤的exist
            # !commands dele game
            elif msg.content =="$deldraw":
                if (self.game_leader ==user or user.id==725714853872009216):
                    END_TIME =None
                    t = await msg.channel.send("抽獎已經刪除...")
                    await msg.delete()
                    await self.game_init_msg.delete()
                    END_TIME =None
                    self.PLAY_MESSAGE_EDIT = {"Game_Main": None, "Numbers": None, "Reward": [],"Game_Activate": False, "Game_End_time": False, "End_time": None}
                    self.game_leader = None
                    self.game_init_msg = None
                    self.participant_table = {}
                    self.Betting_plate=None
                    await asyncio.sleep(5)
                    await t.delete()

                elif self.game_leader !=user:
                    await asyncio.sleep(2)
                    await msg.delete()
                    t = await msg.channel.send("親 您不是創立者喔～ 所以無法刪除抽獎")
                    await asyncio.sleep(5)
                    await t.delete()

            elif (msg.content == "$start") and (self.game_leader ==user or user.id==725714853872009216):
                # if self.PLAY_MESSAGE_EDIT['Game_End_time']==False:
                    # self.PLAY_MESSAGE_EDIT['Game_End_time']=True
                    cache_msg = discord.utils.get(self.bot.cached_messages, id = self.game_init_msg.id)
                    print(cache_msg)
                    for idx, reactions in enumerate(cache_msg.reactions):
                        print(idx)
                        if idx==0:
                            all_participants = [user.display_name async for user in reactions.users() if user != self.bot.user]
                            # all_participants = ['CM', '阿如', '阿布', '右手', '圍圍', '龐董']
                            print(all_participants)
                            embed=discord.Embed(title=self.PLAY_MESSAGE_EDIT['Game_Title'], description='',color=0xecce8b)
                            embed.add_field(name ="得獎清單", inline=False, value = '------------------------------------')
                            print("all_participants", len(all_participants), "Reward", len(self.PLAY_MESSAGE_EDIT['Reward']))
                            if len(self.PLAY_MESSAGE_EDIT['Reward'])>len(all_participants):
                                L1 = random.sample(all_participants, len(all_participants))
                            else:
                                L1 = random.sample(all_participants, len(self.PLAY_MESSAGE_EDIT['Reward']))
                                                        # 人數                                  獎品數量
                            for idx, i in enumerate(self.PLAY_MESSAGE_EDIT['Reward']):
                                try:
                                    embed.add_field(name =i, value = L1[idx])
                                except:
                                    embed.add_field(name =i, value = '-')
                            draw_result = await msg.channel.send(embed=embed)
                            if True:
                                t = await msg.channel.send("抽獎已經結束...")
                                await msg.delete()
                                await self.game_init_msg.delete()
                                END_TIME =None
                                self.PLAY_MESSAGE_EDIT = {"Game_Main": None, "Numbers": None, "Reward": [],"Game_Activate": False, "Game_End_time": False, "End_time": None}
                                self.game_leader = None
                                self.game_init_msg = None
                                self.participant_table = {}
                                self.Betting_plate=None
                                await asyncio.sleep(5)
                                await t.delete()

def setup(bot):
    bot.add_cog(Game(bot))
    bot.add_cog(Lucky(bot))