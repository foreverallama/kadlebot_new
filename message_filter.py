import discord
from discord.ext import commands

class Message(commands.Cog):
    """A chat filter that looks for a swear word or the word 'Wonderla'"""

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener('on_message')
    async def hari_om(self, message):
        
        if message.author == self.bot.user:
            return 
        swear_words = ['FUCK', 'BASTARD', 'AMMAN', 'SULE', 'MOTHERFUCKER',
                   'ASSHOLE', 'DENGIBDTHINI', 'TIKKA', 'SHIT', 'CRAP',
                   'SHAATA', 'CHUTIYA', 'BHENCHOD', 'MADARCHOD', 'GAND',
                   'GAAND', 'LUND', 'PUTA', 'BHOSEDK', 'LODE', 'LOUDE',
                   'LAUDE', 'SHATA']
        if any(word in message.content.upper() for word in swear_words):
            await message.channel.send("Hari Om")

    @commands.Cog.listener('on_message')
    async def wonderla(self, message):

        if message.author == self.bot.user:
            return
        if "WONDERLA" in message.content.upper():
            await message.channel.send("Macha come lets go to Wonderla!")    

def setup(bot):
    """Adds cog to the bot and logs to console"""
    bot.add_cog(Message(bot))
    print('message_filter.py is loaded')
