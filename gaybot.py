import random
import discord
from discord.ext import commands

def __init__(self, bot):
        self.bot = bot

class GayStuff(commands.Cog):
    """Commands for the Category: GayStuff

    Commands
    --------
    message:
            Sends a random message in the same channel from the list 'possible_responses'
    image:
            Sends a random image in the same channel from the folder kadlepics
    video:
            Sends a random video in the same channel from the folder kadlepics
    howgay:
            Replies back to the user in the same channel telling how gay the user is in %
    say:
            Says the text sent by the user with Text-to-Speech enabled
    whisper:
            Sends a DM to the user with a random secret from the list 'secret'
    date:
            Checks compatibility with another discord user
    dateme:
            Checks compatibility with Kadle
    """
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='message',
                      description='Sends a random message',
                      brief='Sends a message',
                      help='Sends a random personalized message from Kadle',
                      pass_context=True,
                      usage='kadle.message',
                      cog='Gaystuff'
                      )
    async def message(self, ctx):
        possible_responses = ['kadle is gay!',
         'I\'ve been holding out my feelings for too long and now I\'ll come out and say it. I am gay :heart:',
         'Who called me amman?',
         'I am going to do something for the LGBT community :gay_pride_flag:',
         'Do you want to be my boyfriend? :couple_mm:',
         'It\'s time for me to come out of the closet',
         'I will play :rainbow: today',
         'Nodu... bai muchko illa andre dengbidthini',
         'Innondu sala message madu andre dengbidthini',
         'Sumne iru! Nan thante ge barbeda',
         ]
        await ctx.send(random.choice(possible_responses))

    @commands.command(name='image',
                      description='Sends a random image',
                      brief='Sends an image',
                      help='Sends a random gay image of kadle',
                      pass_context=True,
                      usage='kadle.image',
                      cog='Gaystuff'
                      )
    async def image(self, ctx):
        path = "./kadlepics/IMG" + str(random.randint(1,12)) + ".jpg"
        await ctx.message.channel.send(file=discord.File(fp=path,filename="kadle.jpg"))

    @commands.command(name='video',
                      description='Sends a random video',
                      brief='Sends a video',
                      help='Sends a random gay video of kadle',
                      pass_context=True,
                      usage='kadle.video',
                      cog='Gaystuff'
                      )
    async def video(self, ctx):
        path = "./kadlepics/VID" + str(random.randint(1,2)) + ".mp4"
        await ctx.message.channel.send(file=discord.File(fp=path,filename="kadle.mp4"))

    @commands.command(name='howgay',
                      description='Tells how gay the user is',
                      brief='How gay are you',
                      help='Replies back with the Gayness in percentage',
                      pass_context=True,
                      usage='kadle.howgay',
                      cog='Gaystuff'
                      )
    async def howgay(self, ctx):
##        Use your own formula to derive a gayness percentage
        if ctx.message.author.id == 390793883631747073 or ctx.message.author.id == 452173950949261312:
            await ctx.message.channel.send(f"You are the gayest man alive {ctx.message.author.mention}")
        else:
            gayness = int((ctx.message.author.id/1000000000000000-random.randint(2000,4500))/ctx.message.author.id * 100)
            await ctx.message.channel.send(f"You are {gayness}% gay {ctx.message.author.mention}")

    @commands.command(name='say',
                      description='Says what you want me to',
                      brief='Does your bidding',
                      help='Now you can hear something being said in Kadle\'s own words!',
                      pass_context=False,
                      usage='kadle.say [message]',
                      cog='Gaystuff'
                      )
    async def say(self, ctx, *payload: str):
        if not payload:
            await ctx.message.channel.send('En helbeku. Helu?')
        else:
            await ctx.message.channel.send(' '.join(payload), tts=True);

    @commands.command(name='whisper',
                      description='Whispers the deepest, darkest secrets',
                      brief='Whispers a secret',
                      help='Kadle has a lot of dark secrets. Type out the command to find out',
                      pass_context=True,
                      usage='kadle.whisper [message]',
                      cog='Gaystuff'
                      )
    async def whisper(self, ctx):
        secret = ['I don\t trust you to keep my secrets so please stop asking',
              'I first got married at the age of 6',
              'I sometimes imagine a future for you and me',
              'I have 12 cows whom I love everyday',
              'My second wife doesn\'t seem to love me anymore',
              'I originally migrated from Nepal through Uttarkhand and changed my surname from \'Bhatt\' to \'Bhat\'',
              'It\'s a beautful day',
              ]
        await ctx.message.author.send(random.choice(secret))

    @commands.command(name='dateme',
                      brief='Will I date you',
                      description='Tells if Kadle will date you',
                      help='Tells if Kadle will go out on a date with you',
                      pass_context=True,
                      usage='kadle.dateme',
                      cog='Gaystuff'
                      )
    async def dateme(self, ctx):
##        Use your own formula to obtain a compatiblity percentage
        percentage = 100
        user_id = str(ctx.message.author)
        user_id = user_id.upper()
        print(user_id)
        kadle_id = 'VINIRANJ#6442'
        for character in user_id:
            if character in kadle_id:
                percentage = percentage - ord(character)/10 
        percentage = round(percentage)
        if percentage >= 100:
            await ctx.message.channel.send("I have met my one true soulmate!")
        elif percentage>=80:
            await ctx.message.channel.send("I would definitely date you. My calculations say we have a " + str(percentage) + "% compatibility")
        elif percentage>=50:
            await ctx.message.channel.send("We could give it a shot. My calculations say we have a " + str(percentage) + "% compatibility")
        elif percentage>=20:
            await ctx.message.channel.send("We can try but don't expect much. We only have a " + str(percentage) + "% compatibility")
        else:
            await ctx.message.channel.send("I would never date a waste of sperm like you")

    @commands.command(name='date',
                      brief='Date a user',
                      description='Checks your compatibility with another user',
                      help='Tells if you and a user are compatible enough to go on a date',
                      pass_context=True,
                      usage='kadle.date @user',
                      cog='Gaystuff'
                      )
    async def date(self, ctx):
##        Use your own formula to obtain a compatiblity percentage
        percentage = 100
        user_id = str(ctx.message.author)
        user_id = user_id.upper()
        interest_id = str(ctx.message.mentions[0])
        interest_id = interest_id.upper()
        for character in user_id:
            if character in interest_id:
                percentage = percentage - ord(character)/10 + random.randint(-10,10)
        percentage = round(percentage)
        if percentage >= 100:
            await ctx.send("You have met your one true soulmate!")
        elif percentage>=80:
            await ctx.send("You should definitely go on a date. My calculations say you are " + str(percentage) + "% compatible")
        elif percentage>=50:
            await ctx.send("You could give it a shot. My calculations say you have a " + str(percentage) + "% compatibility")
        elif percentage>=20:
            await ctx.send("You can try but don't expect much. You are only " + str(percentage) + "% compatible")
        else:
            await ctx.send("No one would ever date a waste of sperm like you")

  
def setup(bot):
    """Adds the Class to the cog and logs to console"""
    bot.add_cog(GayStuff(bot))
    print('gaybot.py is loaded')
