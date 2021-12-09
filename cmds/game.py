import discord, random, json, datetime, asyncio
from discord.ext import commands
from core.classes import Cog_Extension
from random import randint
import time
import datetime
with open('./setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

class Game(Cog_Extension):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.stack
        
        self.game_leader = None
        self.game_init_msg = None
        self.reaction_stack = ['0️⃣','1️⃣','2️⃣','3️⃣','4️⃣','5️⃣','6️⃣','7️⃣','8️⃣','9️⃣']
        self.participant_table = {}
        self.closetime=None
        self.Betting_plate=None
        self.game_detection = False
        self.game_cloase_time_detec=False
    @commands.Cog.listener()
    async def  on_message(self, msg):
        await self.bot.wait_until_ready()
    
        now_time = (datetime.datetime.now().strftime("%H%M")).replace(' ','')
        user = msg.author
        self.user = msg.author
        # print("user name", self.user, "guild name", self.user.display_name,'\n\n')
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
            embed.add_field(name = "commands", inline=False, value="$game {title}, {condition}, {Closing time}, {cond01}, {condi2}, {cond3}.... Max 10")
            embed.add_field(name = "指令", inline=False, value="$game {標題}, {條件}, {收盤時間}, {條件1}, {條件2}, {條件3}.... 最多10個條件")
            embed.add_field(name = "範例(建議直接複製下面的範例指令修改)", inline=False, value="$game 老黑7414團, 誰會先死, 2130, 阿布, 赤冥, 死靈, 雅, 龐克, 水水")
            embed.add_field(name = "Game開啟後相關指令", inline=False, value="輸入「$list」可以查詢當前下注情況\n輸入「$end」可以提早收起Game或者輸入「$del」刪除Game(只有創立者可以使用)")
            Tutorials = await msg.channel.send(embed=embed)
            await asyncio.sleep(120)
            await Tutorials.delete()

        elif self.game_detection == False:
            if msg.content[0:5]=="$game" and "$game" in msg.content and msg.author != self.bot.user:
                #開賭盤 老黑7414團, 誰會先死, 2130, 阿布, 赤冥, 死靈, 雅, 龐克, 水水
                await asyncio.sleep(1)
                message = msg.content
                game_setting = message[5::].split(',')
                print(game_setting[0], game_setting[1], len(game_setting[2].replace(' ','')), len(game_setting[3::]))
                if False:
                    pass
                elif len(game_setting[2].replace(' ',''))!=4 or ":" in game_setting[2]:
                    t = await msg.channel.send("時間格式有誤. 請確定輸入的時間是24小時制. example: 0800, 2100")
                    await asyncio.sleep(15)
                    await msg.delete()
                    await t.delete()

                elif len(game_setting[2].replace(' ',''))==4 and int(game_setting[2].replace(' ',''))>2400:
                    t = await msg.channel.send("時間格式有誤. 請確定輸入的時間是24小時制. example: 0800, 2100")
                    await asyncio.sleep(15)
                    await msg.delete()
                    await t.delete()
                
                elif len(game_setting[3::])>10:
                    t = await msg.channel.send("請確認設定的條件是否超過10個")
                    await asyncio.sleep(15)
                    await msg.delete()
                    await t.delete()

                else:
                    self.default_title = game_setting[0]
                    self.default_condition = game_setting[1]
                    self.closetime = game_setting[2].replace(' ','')
                    self.default_condition_stack = game_setting[3::]
                    # print(default_title, default_condition, default_condition_stack)
                    await msg.delete()
                    self.game_leader = user
                    self.game_detection = True
                    with open('./setting.json', 'w', encoding='utf8') as jfile:
                        json.dump(jdata, jfile, indent=4)
                    self.game_detection = True
                    default_condition_dict ={}
                    for idx, i in enumerate(self.default_condition_stack):
                        default_condition_dict[i] = self.reaction_stack[idx]
            
                    embed=discord.Embed(title=self.default_title +' - '+ self.default_condition, 
                                        description='',color=0xecce8b)
                    for idx, i in enumerate(self.default_condition_stack):
                        embed.add_field(name =self.reaction_stack[idx]+'  '+ i, value = '-')
                    embed.add_field(name = f"停止參與時間為{self.closetime}", inline=False, value="------------------------------------")
                    embed.add_field(name = "請點擊下方的Emoji參與!!\n請勿做重複的選擇!!\n創立者請好好檢查警告作弊仔XD", inline=False, value="------------------------------------")
                    embed.add_field(name = "可以輸入「$list」觀看參與情況\n創立者可以輸入「$end」結束Game或者輸入 「$del」刪除Game", inline=False, value="------------------------------------")
                    self.game_init_msg = await msg.channel.send(embed=embed)
                    for i in range(len(self.default_condition_stack)):
                        await self.game_init_msg.add_reaction(self.reaction_stack[i])
                    for i in self.default_condition_stack:
                        self.participant_table[i] = []
        
        elif  self.game_detection==True:
            if msg.content[0:5]=="$game":
                if len(msg.content)==5:
                
                    embed=discord.Embed(title='開Game教學', 
                                        description='',color=0xecce8b)
                    embed.add_field(name = "commands", inline=False, value="$game {title}, {condition}, {Closing time}, {cond01}, {condi2}, {cond3}.... Max 10")
                    embed.add_field(name = "指令", inline=False, value="$game {標題}, {條件}, {收盤時間}, {條件1}, {條件2}, {條件3}.... 最多10個條件")
                    embed.add_field(name = "範例(建議直接複製下面的範例指令修改)", inline=False, value="$game 老黑7414團, 誰會先死, 2130, 阿布, 赤冥, 死靈, 雅, 龐克, 水水")
                    embed.add_field(name = "Game開啟後相關指令", inline=False, value="輸入「$list」可以查詢當前下注情況\n輸入「$end」可以提早收起Game或者輸入「$del」刪除Game(只有創立者可以使用)")
                    Tutorials = await msg.channel.send(embed=embed)
                    await asyncio.sleep(120)
                    await msg.delete()
                    await Tutorials.delete()

                elif len(msg.content)!=5:
                    t = await msg.channel.send("當前已經有Game存在 請創立者刪除後再新增")
                    await asyncio.sleep(10)
                    await msg.delete()
                    await t.delete()   
            # 僅有使用者可以控制賭盤的exist
            # !commands dele game
            elif msg.content =="$del":
                if (self.game_leader ==user or user=="PuiPui-MoMoJUJU#0550"):
                    await msg.delete()
                    self.game_cloase_time_detec=False
                    self.game_detection = False
                    await self.game_init_msg.delete()
                    self.game_leader = None
                    self.game_init_msg = None
                    self.participant_table = {}
                    self.closetime=None
                    self.Betting_plate=None
                    self.game_detection = False
                    self.reply_status==True

                elif self.game_leader !=user:
                    await asyncio.sleep(2)
                    await msg.delete()
                    t = await msg.channel.send("親 您不是創立者喔～ 所以無法刪除Game")
                    await asyncio.sleep(5)
                    await t.delete()

            elif msg.content=='$reply' and self.game_cloase_time_detec==False:
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

                if self.game_cloase_time_detec==True:
                    title_ = 'Game List(End)'
                else:
                    title_ = 'Game List (該功能非常延遲 建議30秒查詢一次 以確保資料有更新)'
                embed=discord.Embed(title=title_,description=f'{self.default_title} - {self.default_condition}',color=0xecce8b)
                
                for idx, i in enumerate(self.participant_table):
                    embed.add_field(name = i, inline=False, value = self.participant_table[i])
                if self.game_cloase_time_detec==True:
                    name_ = f"已經結束. 停止參與. Game結果以目前Game List為主"
                else:
                    name_ = f"停止參與時間為{self.closetime}. 現在時間是{now_time}."
                embed.add_field(name = name_, inline=False, value="------------------------------------")
                if self.game_cloase_time_detec==True:
                    self.Betting_plate= await msg.channel.send(embed=embed)
                    await msg.delete()
                    self.game_cloase_time_detec=False
                    self.game_detection = False
                    await self.game_init_msg.delete()
                    self.game_leader = None
                    self.game_init_msg = None
                    self.participant_table = {}
                    self.closetime=None
                    self.Betting_plate=None
                    self.game_detection = False
                    self.game_cloase_time_detec=False
                elif self.game_cloase_time_detec==False:
                    embed.add_field(name = "Game List 30秒後會自動關閉",inline=False, value="------------------------------------")
                    self.Betting_plate= await msg.channel.send(embed=embed)
                    await asyncio.sleep(30)
                    await msg.delete()
                    await self.Betting_plate.delete()
                        
            # print('participant list', self.participant_table)

            # 假如賭盤已經收盤 建置game table指令提供查詢  
            
            elif (now_time==self.closetime or msg.content == "$end") and (self.game_leader ==user or user=="PuiPui-MoMoJUJU#0550"):
                if self.game_cloase_time_detec==False:
                    self.game_cloase_time_detec=True
                    t = await msg.channel.send("Game已經結束. 可以再次使用Game開新的局. 請輸入「$list」確認最終結果.")
                    await msg.delete()
                    await asyncio.sleep(1)

            print(self.closetime, type(self.closetime), now_time, type(now_time))

            # 需要使用即時檢測function


def setup(bot):
    bot.add_cog(Game(bot))