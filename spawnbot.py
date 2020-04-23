import discord
from discord.ext import commands
import random
from random import choices
import numpy


spawn_channel = {}
kadledex = {}
moves = ['Dengbidthini', 'Hari Om', 'Tunne', 'Fuck You', 'Amman', 'Minni Kai', 'Buttsex']
spawn_flag = {}

class Spawn(commands.Cog):
    """
       Commands for Category: Kadlemon
       -------------------------------
        Note: This basically tries to mirror Pokecord. Check out their bot

        spawn:
            sets a text channel to spawn in
        list:
            lists all kadles caught till now
        select:
            selects a kadle as your companion
        moves:
            lists the moves for your selected kadle
    """

    def __init__(self,bot):
        global kadledex
        self.bot = bot
        
        for guild in self.bot.guilds:
            spawn_flag[guild.id] = True
            kadledex[guild.id] = {}
            for member in guild.members:
                kadledex[guild.id][member.id] = {}
        print('Initialized Kadledex on Reload')

    @commands.Cog.listener('on_ready')
    async def initialize_kadledex(self):
        global kadledex, spawn_flag
        
        for guild in self.bot.guilds:
            spawn_flag[guild.id] = True
            kadledex[guild.id] = {}
            for member in guild.members:
                kadledex[guild.id][member.id] = {}
        print('Initialized Kadledex on Login')        

    @commands.Cog.listener('on_message')
    async def spawn_image(self, message):
        global spawn_channel, kadledex, moves, spawn_flag
        
        if message.author == self.bot.user or message.content.startswith('kadle.'):
            return
        a = random.randint(0,1000)
        if a > 920 and spawn_flag[message.guild.id]==True:
            weights = [0.09, 0.2, 0.061, 0.06, 0.12, 0.12, 0.08, 0.1, 0.1, 0.067, 0.002] 
            file_path = "./kadlemon/IMG" + str(numpy.random.choice(numpy.arange(1,12), p=weights)) + ".jpg"
            if message.guild.id in spawn_channel.keys():
                message.channel = spawn_channel[message.guild.id]

            await message.channel.send(content="A wild Kadle appeared!",
                                       delete_after=60,
                                       file=discord.File(fp=file_path,
                                                         filename="Kadlemon.jpg"))
            spawn_flag[message.guild.id]=False

            def check(m):
                global spawn_flag
                if m.content == "kadle.catch kadle" and m.channel == message.channel:
                    spawn_flag[message.guild.id] = True
                    return m

            try:
                msg = await self.bot.wait_for('message', check=check, timeout=60)
                level = random.randint(4,32)
                await msg.channel.send(f"Congratulations {msg.author.mention}! You caught a Level {level} Kadle!", delete_after=20)

                kadledex[msg.guild.id][msg.author.id]["Select"] = 0
                
                res = -1
                for key in kadledex[msg.guild.id][msg.author.id].keys():
                    res += 1
                    
                kadledex[msg.guild.id][msg.author.id][res+1] = {}
                kadledex[msg.guild.id][msg.author.id][res+1]["Name"] = "Kadle"
                kadledex[msg.guild.id][msg.author.id][res+1]["Level"] = level
                kadledex[msg.guild.id][msg.author.id][res+1]["Moves"] = random.sample(moves,4)
                

            except:
                await message.channel.send("Oh no! The wild Kadle fled",delete_after=20)
                spawn_flag[message.guild.id] = True

    @commands.command(name='spawn',
                      description='Sets the channel for kadle to spawn in',
                      brief='Set spawn channel',
                      help='Makes sure that kadle spawns only in the text channel mentioned, requires admin privileges',
                      pass_context=True,
                      usage='kadle.spawn [channel-name]',
                      cog='Spawn'
                      )
    async def spawn(self, ctx, payload=None):
        global spawn_channel
        channel = ctx.message.channel_mentions[0]
        spawn_channel[ctx.guild.id] = channel
        await ctx.send(f"Kadle will now spawn in the text channel {ctx.message.channel_mentions[0].mention}")

    @commands.command(name='list')
    async def list(self, ctx, payload = 1):
        global kadledex
        user_id = ctx.message.author.id

        upper_limit = payload*10 + 1

        if (upper_limit-10) not in kadledex[ctx.guild.id][user_id].keys():
            await ctx.send("You haven't caught that many Kadles yet")
            return
        
        op = "```"

        for key in kadledex[ctx.guild.id][user_id]:
            if isinstance(key, int):
                if key >= upper_limit - 10 and key < upper_limit:
                    op += kadledex[ctx.guild.id][user_id][key]["Name"]  + "     #" + str(key) + "     Level " + str(kadledex[ctx.guild.id][user_id][key]["Level"])
                    op += "\n"
            last_key = key
        op+="```"

        e = discord.Embed(type="rich", color=0x91f735)
        e.title = str(ctx.message.author) + "'s Kadles"
        e.add_field(name=f"Page {payload}", value=op)
        e.set_footer(text=f"Showing {upper_limit-10} to {upper_limit-1} of {last_key} Kadles on this page")

        await ctx.send(embed=e, delete_after=300)

    @commands.command(name='select')
    async def select(self, ctx, payload: int):
        global kadledex
        user_id = ctx.message.author.id

        try:
            if payload in kadledex[ctx.guild.id][user_id].keys():
                kadledex[ctx.guild.id][user_id]["Select"] = payload
            else:
                await ctx.send("You don't have that Kadle yet")
                return
        except:
            await ctx.send("You don't have any Kadles yet")
            return

        await ctx.send(f"You have selected Kadle #{payload}")

    @commands.command(name='moves')
    async def moves(self, ctx):
        global kadledex
        user_id = ctx.message.author.id

        try:
            number = kadledex[ctx.guild.id][user_id]["Select"]
            if number == 0:
                await ctx.send("You have to select a Kadle first. Type kadle.list to find out what Kadles you've caught")
                return
        except:
            await ctx.send("You don't have that Kadle yet")
            return


        e = discord.Embed(type="rich", color=0x91f735)
        e.set_author(name=str(ctx.message.author) + "'s Kadle")
        e.title = "Level " + str(kadledex[ctx.guild.id][user_id][number]["Level"]) + " " + kadledex[ctx.guild.id][user_id][number]["Name"]

        op = '\n'.join(kadledex[ctx.guild.id][user_id][number]["Moves"])
        e.add_field(name=f"Moves", value=op)

        await ctx.send(embed=e, delete_after=300)

def setup(bot):
    bot.add_cog(Spawn(bot))
    print('spawnbot.py is loaded')
