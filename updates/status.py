import discord
from discord.ext import commands
import random

spawn_channel = {}

class Status(commands.Cog):

    def __init__(self,bot):
        self.bot = bot

    @commands.Cog.listener('on_member_join')
    async def greet_member(self, message):
        if message.author == self.bot.user:
            return
        await message.channel.send("Who invited you here?")

    @commands.Cog.listener('on_member_update')
    async def inform_members(self, before, after):
        if message.author == self.bot.user:
            return
        if before.activity is None and after.activity is not None:
            


    
def setup(bot):
    bot.add_cog(Spawn(bot))
    print('status.py loaded')
