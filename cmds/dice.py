# 賭場骰子專用 Listener
# from 巴哈 Source Code, Used LSTM and Keras API
# Activaty Status Chcek : Firebase
import discord, random, json, datetime, asyncio, os
from discord.ext import commands
from discord.utils import get
from core.classes import Cog_Extension_dice
from random import randint
import time, sys, datetime
# sys.path.append("..")
from dice_pred.NB import *

class Dice(Cog_Extension_dice):

    @commands.Cog.listener()
    async def  on_message(self, msg):
        user = msg.author
        user_id = msg.author.id
        message_id = msg.id
        content = msg.content
        message_channel = msg.channel.id
        await self.bot.wait_until_ready()
        endls = False



        if msg.content.startswith("$money") and msg.channel.id==953529876802056233:
            await msg.reply("請輸入六個整數數字 (1-6) 作為歷史追蹤，例如：123456 要結束請打: $endl")
            def is_correct(m):
                # print(m)
                # return m.author == msg.author
                return m.author == msg.author and (m.content.isdigit() or ('end' in m.content or 'END' in m.content))

            while(1):
                try:
                    input_num = await self.bot.wait_for('message', check=is_correct, timeout=360.0)
                    try:
                        await error_in.delete()
                    except:
                        pass

                except asyncio.TimeoutError:
                    return await msg.channel.send(f'等待時間過長 請重新啟用')

                input_num = input_num.content
                if len(input_num)!=6:
                    error_in = await msg.channel.send(f'輸入錯誤!! 請輸入6位阿拉伯數字')
                else:
                    break
            while endls==False:
                if endls==False:
                    data = turn_data(input_num)
                    data_weight = get_weight_dis(data, self.model)
                    manual_score, predict_score,= clc_weight(data_weight)
                    predcit_num_stack, program_pred, double_single, g_or_l, program_recommend = show_result(manual_score, predict_score, data_weight)
                    now_time = (datetime.datetime.now().strftime("%Y%m%d%H%M"))
                    embed=discord.Embed(title="賭博預測", description=now_time,color=0xecce8b)
                    embed.add_field(name = '當前數據為', inline=False, value = [i for i in input_num])
                    embed.add_field(name = '數字預測機率', inline=False, value = ''.join([(str(i)) for i in predcit_num_stack]))
                    embed.add_field(name = '程式預測數字', inline=False, value = program_pred)
                    embed.add_field(name = '單雙推薦下注', inline=False, value = double_single)
                    embed.add_field(name = '大小推薦下注', inline=False, value = g_or_l)            
                    embed.add_field(name = '程式預測下注', inline=False, value = program_recommend)
                    get_gamble_table =  await msg.channel.send(embed=embed)
                    bot_msg_Q = await msg.channel.send(f'請輸入實際數字')
                    while(1):
                        await asyncio.sleep(1)
                        try:
                            actual_num = await self.bot.wait_for('message', check=is_correct, timeout=360.0)
                            actual_num_ = actual_num.content
                        except asyncio.TimeoutError:
                            return await msg.channel.send(f'等待時間過長 請重新啟用')
                        # await asyncio.sleep(1)
                        n = actual_num_
                        # print('-------------------------n ', n)
                        try:
                            await error_in.delete()
                        except:
                            pass
                        if 'end' in n or 'END' in n:
                            endls=True
                            await get_gamble_table.delete()
                            await actual_num.delete()
                            await bot_msg_Q.delete()
                            await msg.channel.send(f'結束預測!!!!')
                            await asyncio.sleep(1)
                            break
                        elif (n=='' or int(n) > 6 ) and (('end' in n) == False):
                            error_in = await msg.channel.send(f'輸入錯誤!! 請重新輸入')
                        elif endls!=True:
                            try:
                                input_num = input_num.content[1:6] + n
                            except:
                                input_num = input_num[1:6] + n    
                            await get_gamble_table.delete()
                            await actual_num.delete()
                            await bot_msg_Q.delete()
                            break
                # print("gameble status: ", endls, n)
            


def setup(bot):
    bot.add_cog(Dice(bot))