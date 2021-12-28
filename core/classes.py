import discord
from discord.ext import commands
from core.firebase_config import *
class Cog_Extension(commands.Cog):
        def __init__(self, bot):
            self.bot = bot
            self.ref = ref