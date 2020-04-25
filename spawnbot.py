import discord
from discord.ext import commands
import random
import numpy
import pymongo
from pymongo import MongoClient
import os

moves = ['Dengbidthini', 'Hari Om', 'Tunne', 'Fuck You', 'Amman', 'Minni Kai', 'Buttsex']
spawn_flag = {}

collection = None

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
        global spawn_flag, collection
        self.bot = bot
        
        for guild in self.bot.guilds:
            spawn_flag[guild.id] = True

        print('Reloading spawnbot')

        try:
            MONGO = os.environ.get('MONGO', None)
            url = "mongodb+srv://kadleBot:" + str(MONGO) + "@kadlebot-t63y9.mongodb.net/test?retryWrites=true&w=majority"
            cluster = MongoClient(url)
            db = cluster["discord"]
            collection = db["kadledex"]
            print('Connected to Mongodb')
        except pymongo.errors.ServerSelectionTimeoutError:
            print('Mongodb: TimeoutError. Could not retrieve Spawn Channel')

    @commands.Cog.listener('on_ready')
    async def init_spawn(self):
        global spawn_flag
        for guild in self.bot.guilds:
            spawn_flag[guild.id] = True
        print('KadleBot is ready. Initialized Spawn Flags')

    @commands.Cog.listener('on_message')
    async def spawn_image(self, message):
        global collection, moves, spawn_flag
        
        if message.author == self.bot.user or message.content.startswith('kadle.'):
            return
        a = random.randint(0,1000)
        if a > 920 and spawn_flag[message.guild.id] is True:
            weights = [0.09, 0.2, 0.061, 0.06, 0.12, 0.12, 0.08, 0.1, 0.1, 0.067, 0.002] 
            file_path = "./kadlemon/IMG" + str(numpy.random.choice(numpy.arange(1,12), p=weights)) + ".jpg"

            query = {"_id": message.guild.id, "channel": {"$exists": True}}
            results = collection.find_one(query)
            if results:
                message.channel = self.bot.get_channel(results["channel"])

            await message.channel.send(content="A wild Kadle appeared!",
                                       delete_after=60,
                                       file=discord.File(fp=file_path,
                                                         filename="Kadlemon.jpg"))
            spawn_flag[message.guild.id] = False

            def check(m):
                global spawn_flag
                if m.content == "kadle.catch kadle" and m.channel == message.channel:
                    spawn_flag[message.guild.id] = True
                    return m

            try:
                msg = await self.bot.wait_for('message', check=check, timeout=60)
            except Exception as e:
                await message.channel.send("Oh no! The wild Kadle fled", delete_after=20)
                spawn_flag[message.guild.id] = True
                return

            level = random.randint(4,32)
            await msg.channel.send(f"Congratulations {msg.author.mention}! You caught a Level {level} Kadle!", delete_after=20)

            query = {"_id": msg.guild.id}
            results = collection.find_one(query)

            if results is None:
                post = {"_id": msg.guild.id,
                        str(msg.author.id):
                            {"1":
                                 {"Name": "Kadle",
                                  "Level": level,
                                  "Moves": random.sample(moves, 4)
                                  },
                             "S": 1
                             }
                        }
                results = collection.insert_one(post)

            else:
                results = collection.find_one({"_id": msg.guild.id, str(msg.author.id): {"$exists": True}})

                results = list(results[str(msg.author.id)].keys())
                results.remove('S')
                results = list(map(int, results))
                results.sort()

                final_res = results[-1] + 1
                for i in range(1, results[-1] + 1):
                    if i not in results:
                        final_res = i
                        break

                post = {"$set":
                    {
                        str(msg.author.id) + "." + str(final_res):
                            {

                                "Name": "Kadle",
                                "Level": level,
                                "Moves": random.sample(moves, 4)
                            }
                    }
                }

                results = collection.update_one({"_id": msg.guild.id}, post)

    @commands.command(name='spawn',
                      description='Sets the channel for kadle to spawn in',
                      brief='Set spawn channel',
                      help='Makes sure that kadle spawns only in the text channel mentioned, requires admin privileges',
                      pass_context=True,
                      usage='kadle.spawn [channel-name]',
                      cog='Spawn'
                      )
    async def spawn(self, ctx, payload=None):
        global collection

        channel = ctx.message.channel_mentions[0]

        query = {"_id": ctx.guild.id, "channel": {"$exists": True}}
        results = collection.find_one(query)
        if not results:
            collection.insert_one({"_id": ctx.guild.id, "channel": channel.id})
        else:
            results = collection.update_one({"_id": ctx.guild.id}, {"$set": {"channel": channel.id}})

        await ctx.send(f"Kadle will now spawn in the text channel {ctx.message.channel_mentions[0].mention}")

    @commands.command(name='list')
    async def list(self, ctx, payload = 1):
        global collection

        upper_limit = payload*10 + 1

        results = collection.find_one({"_id": ctx.guild.id, str(ctx.message.author.id): {"$exists": True}})
        if results is None:
            await ctx.send("You haven't caught any Kadles yet")
            return
        elif len(results[str(ctx.message.author.id)].keys()) < upper_limit - 10:
            await ctx.send("You haven't caught that many Kadles yet")
            return

        results[str(ctx.message.author.id)].pop('S')
        keys = sorted(results[str(ctx.message.author.id)].keys(), key=lambda x: int(x))
        op = "```"

        for key in keys:
            if upper_limit - 10 <= int(key) < upper_limit:
                op += results[str(ctx.message.author.id)][key]["Name"] + "     #" + str(key) + \
                      "      Level " + str(results[str(ctx.message.author.id)][key]["Level"])
            op += "\n"
            last_key = int(key)
        op += "```"

        if last_key <= upper_limit - 1:
            page_limit = last_key
        else:
            page_limit = upper_limit - 1

        e = discord.Embed(type="rich", color=0x91f735)
        e.title = str(ctx.message.author) + "'s Kadles"
        e.add_field(name=f"Page {payload}", value=op)
        e.set_footer(text=f"Showing {upper_limit - 10} to {page_limit} of {last_key} Kadles on this page")

        await ctx.send(embed=e, delete_after=300)

    @commands.command(name='select')
    async def select(self, ctx, payload: int):
        global collection

        results = collection.find_one({"_id": ctx.guild.id, str(ctx.message.author.id): {"$exists": True}})

        if results is None:
            await ctx.send("You haven't caught any Kadle yet")
            return

        if str(payload) in results[str(ctx.message.author.id)].keys():
            results = collection.update_one({"_id": ctx.guild.id},
                                            {"$set": {str(ctx.message.author.id) + "." + "S": payload}})
            await ctx.send(f"You have selected Kadle #{payload}")
        else:
            await ctx.send("You haven't caught that Kadle yet")

    @commands.command(name='moves')
    async def moves(self, ctx):
        global collection

        results = collection.find_one({"_id": ctx.guild.id, str(ctx.message.author.id): {"$exists": True}})

        if results is None:
            await ctx.send("You haven't caught any Kadle yet")
            return

        number = results[str(ctx.message.author.id)]["S"]
        level = str(results[str(ctx.message.author.id)][str(number)]["Level"])
        op = '\n'.join(results[str(ctx.message.author.id)][str(number)]["Moves"])
        name = results[str(ctx.message.author.id)][str(number)]["Name"]

        e = discord.Embed(type="rich", color=0x91f735)
        e.set_author(name=str(ctx.message.author) + "'s Kadle")
        e.title = "Level " + level + " " + name
        e.add_field(name=f"Moves", value=op)
        await ctx.send(embed=e, delete_after=300)

def setup(bot):
    bot.add_cog(Spawn(bot))
    print('spawnbot.py is loaded')
