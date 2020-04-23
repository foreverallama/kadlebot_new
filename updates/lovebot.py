import asyncio
import discord
from discord.ext import commands
import random

def __init__(self, bot):
        self.bot = bot

class Love(commands.Cog):
    """Commands for the Category: Rainbow

    Commands
    --------
    
    """
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='date',
                      brief='Checks compatibility',
                      description='Checks your compatibility with another user',
                      help='Tells if you and a user are compatible enough to go on a date',
                      pass_context=True
                      )
    async def date(self, ctx):
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

    @commands.command(name='eqtest',
                      brief='How dateable you are',
                      description='Checks how dateable you are by assessing your personality',
                      help='Asks 5 questions to determine your personality and tells how dateable you are',
                      pass_context=True,
                      no_pm=True)
    async def eqtest(self, ctx):
        await ctx.send(f"{ctx.message.author.mention}, I will ask you 5 yes-no questions to determine your personality."
                           "Answer honestly illa andre dengbidthini\n\n"
                           "__Instructions__\n\n"
                           "1. Type `kadle.start` to start the test\n"
                           "2. Answer each question with `kadle.yes` or `kadle.no`\n"
                           "3. Wait for results\n"
                           "4. You can cancel anytime by not answering for 60 seconds")
        def check(m):
                if m.content == 'kadle.start' and m.author == ctx.message.author and m.channel == ctx.message.channel:
                        return True

        msg = await self.bot.wait_for('message',timeout=60, check = check)
        if msg: 
            list_of_questions = [["`Consider a scenario where you, your first wife and second wife are being hanged. "
                                  "You can save only two, including yourself. Will you save your first wife?`",
                                  "`Will you save your second wife?`", 
                                  "`Would you be willing to do anything for your gay friend, even if it meant indulging in gay sex?`",
                                  "`Do you milk your cow everyday?`",
                                  "`Will you carry your team in Rainbow?`"
                                      ]]
            question_bank = random.randint(0,0)
            current_questions = list_of_questions[question_bank]
            answers = []
            def check1(m):
                print(str(m.author))
                print(str(ctx.message.author))
                if m.author == ctx.message.author and m.channel == ctx.message.channel:
                        if str(m.content) == "kadle.yes":
                            return 'YES'
                        elif str(m.content) == "kadle.no":
                            return 'NO'
                                
            for i in range(0,5):
                await ctx.send(current_questions[i])
                msg = await self.bot.wait_for(timeout=60, check = check1)
                if msg:
                    answers.append(str(msg.content))
                else:
                    await ctx.send(f"{ctx.message.author.mention}, Answer madalla andre time waste madbeda goobe")

            if question_bank == 0:
                if answers[0] == 'kadle.yes' and answers[1] == 'kadle.yes' and answers[2] == 'kadle.yes' and answers[3] == 'kadle.yes' and answers[4] == 'kadle.yes':
                    msg = "Olle huduga who bends over regularly. But you demand too much milk. 7/10 would marry"
                    await ctx.send(ctx.message.author.mention + msg)
                elif answers[0] == 'kadle.yes' and answers[1] == 'kadle.yes' and answers[2] == 'kadle.yes' and answers[3] == 'kadle.yes' and answers[4] == 'kadle.no':
                    msg = "Olle huduga who bends over regularly. But you over-milk your cows without caring for them. 5/10 would marry"
                    await ctx.send(ctx.message.author.mention + msg)
                elif answers[0] == 'kadle.yes' and answers[1] == 'kadle.yes' and answers[2] == 'kadle.yes' and answers[3] == 'kadle.no' and answers[4] == 'kadle.yes':
                    msg = "Olle huduga who bends over regularly and drinks the right amount of milk. But you don't share your milk. 6/10 would marry"
                    await ctx.send(ctx.message.author.mention + msg)
                elif answers[0] == 'kadle.yes' and answers[1] == 'kadle.yes' and answers[2] == 'kadle.yes' and answers[3] == 'kadle.no' and answers[4] == 'kadle.no':
                    msg = "Olle huduga who bends over regularly and drinks the right amount of milk. You also bring enough milk for everyone. 10/10 would marry"
                    await ctx.send(ctx.message.author.mention + msg)
                elif answers[0] == 'kadle.yes' and answers[1] == 'kadle.yes' and answers[2] == 'kadle.no' and answers[3] == 'kadle.yes' and answers[4] == 'kadle.yes':
                    msg = "Parvagilla. You don't care about cows, but still help them. 5/10 would marry"
                    await ctx.send(ctx.message.author.mention + msg)
                elif answers[0] == 'kadle.yes' and answers[1] == 'kadle.yes' and answers[2] == 'kadle.no' and answers[3] == 'kadle.yes' and answers[4] == 'kadle.no':
                    msg = "Waste neenu. You don't care about cows at all. Would rather eat them instead. 3/10 would marry"
                    await ctx.send(ctx.message.author.mention + msg)
                elif answers[0] == 'kadle.yes' and answers[1] == 'kadle.yes' and answers[2] == 'kadle.no' and answers[3] == 'kadle.no' and answers[4] == 'kadle.yes':
                    msg = "Parvagilla. You look after cows' needs but not your gay friends'. But you would still let them peek when it spawns. 5/10 would marry"
                    await ctx.send(ctx.message.author.mention + msg)
                elif answers[0] == 'kadle.yes' and answers[1] == 'kadle.yes' and answers[2] == 'kadle.no' and answers[3] == 'kadle.no' and answers[4] == 'kadle.no':
                    msg = "Parvagilla. You look after cows' needs but not your gay friends'. You don't even let them peek when it spawns because you die immediately. 4/10 would marry"
                    await ctx.send(ctx.message.author.mention + msg)
                elif answers[0] == 'kadle.yes' and answers[1] == 'kadle.no' and answers[2] == 'kadle.yes' and answers[3] == 'kadle.yes' and answers[4] == 'kadle.yes':
                    msg = "Thu. You are still love your first wife more than your second wife and your cows. But plus points for loyalty. 6/10 would marry"
                    await ctx.send(ctx.message.author.mention + msg)
                elif answers[0] == 'kadle.yes' and answers[1] == 'kadle.no' and answers[2] == 'kadle.yes' and answers[3] == 'kadle.yes' and answers[4] == 'kadle.no':
                    msg = "Thu. You are still love your first wife more than your second wife and your cows. But you don't love her enough to carry. 3/10 would marry"
                    await ctx.send(ctx.message.author.mention + msg)
                elif answers[0] == 'kadle.yes' and answers[1] == 'kadle.no' and answers[2] == 'kadle.yes' and answers[3] == 'kadle.no' and answers[4] == 'kadle.yes':
                    msg = "Thu. You are still love your first wife more than your second wife, probably because she's a cow. 7/10 would marry"
                    await ctx.send(ctx.message.author.mention + msg)
                elif answers[0] == 'kadle.yes' and answers[1] == 'kadle.no' and answers[2] == 'kadle.yes' and answers[3] == 'kadle.no' and answers[4] == 'kadle.no':
                    msg = "Thu. You are still love your first wife more than your second wife, probably because she's a cow. But you also know you're gay and don't care for her. 6/10 would marry"
                    await ctx.send(ctx.message.author.mention + msg)
                elif answers[0] == 'kadle.yes' and answers[1] == 'kadle.no' and answers[2] == 'kadle.no' and answers[3] == 'kadle.yes' and answers[4] == 'kadle.yes':
                    msg = "Waste body. Don't care about cows, friends or second wife. But would still carry them. 3/10 would marry"
                    await ctx.send(ctx.message.author.mention + msg)
                elif answers[0] == 'kadle.yes' and answers[1] == 'kadle.no' and answers[2] == 'kadle.no' and answers[3] == 'kadle.yes' and answers[4] == 'kadle.no':
                    msg = "Waste body. Don't care about cows, friends or second wife. 1/10 would marry"
                    await ctx.send(ctx.message.author.mention + msg)
                elif answers[0] == 'kadle.yes' and answers[1] == 'kadle.no' and answers[2] == 'kadle.no' and answers[3] == 'kadle.no' and answers[4] == 'kadle.yes':
                    msg = "Thu. You protest against gay rights but are okay with beastality... 2/10 would marry"
                    await ctx.send(ctx.message.author.mention + msg)
                elif answers[0] == 'kadle.yes' and answers[1] == 'kadle.no' and answers[2] == 'kadle.no' and answers[3] == 'kadle.no' and answers[4] == 'kadle.no':
                    msg = "You are almost completely useless. 1/10 would marry"
                    await ctx.send(ctx.message.author.mention + msg)
                elif answers[0] == 'kadle.no' and answers[1] == 'kadle.yes' and answers[2] == 'kadle.yes' and answers[3] == 'kadle.yes' and answers[4] == 'kadle.yes':
                    msg = "Good. You let that cheating wife of yours die like you wanted to. But you milked your cow too hard. 4/10 would marry"
                    await ctx.send(ctx.message.author.mention + msg)
                elif answers[0] == 'kadle.no' and answers[1] == 'kadle.yes' and answers[2] == 'kadle.yes' and answers[3] == 'kadle.yes' and answers[4] == 'kadle.no':
                    msg = "Good. You let that cheating wife of yours die like you wanted to. But you demand too much milk from your wife. 2/10 would marry"
                    await ctx.send(ctx.message.author.mention + msg)
                elif answers[0] == 'kadle.no' and answers[1] == 'kadle.yes' and answers[2] == 'kadle.yes' and answers[3] == 'kadle.no' and answers[4] == 'kadle.yes':
                    msg = "Good. You let that cheating wife of yours die like you wanted to. But you should tell your wife that you're gay. 7/10 would marry"
                    await ctx.send(ctx.message.author.mention + msg)
                elif answers[0] == 'kadle.no' and answers[1] == 'kadle.yes' and answers[2] == 'kadle.yes' and answers[3] == 'kadle.no' and answers[4] == 'kadle.no':
                    msg = "Good. You let that cheating wife of yours die like you wanted to. But you don't tell your wife you're gay because you're afraid that she'll team kill you. 6/10 would marry"
                    await ctx.send(ctx.message.author.mention + msg)
                elif answers[0] == 'kadle.no' and answers[1] == 'kadle.yes' and answers[2] == 'kadle.no' and answers[3] == 'kadle.yes' and answers[4] == 'kadle.yes':
                    msg = "You secretly enjoy gay sex with cows. Nothing more to say here. 1/10 would marry"
                    await ctx.send(ctx.message.author.mention + msg)
                elif answers[0] == 'kadle.no' and answers[1] == 'kadle.yes' and answers[2] == 'kadle.no' and answers[3] == 'kadle.yes' and answers[4] == 'kadle.no':
                    msg = "You secretly engaged in gay sex just because you wanted to see how it feels. But you don't care about others' feelings. 2/10 would marry"
                    await ctx.send(ctx.message.author.mention + msg)
                elif answers[0] == 'kadle.no' and answers[1] == 'kadle.yes' and answers[2] == 'kadle.no' and answers[3] == 'kadle.no' and answers[4] == 'kadle.yes':
                    msg = "Good. You love your second wife as much as your cows. 6/10 would marry"
                    await ctx.send(ctx.message.author.mention + msg)
                elif answers[0] == 'kadle.no' and answers[1] == 'kadle.yes' and answers[2] == 'kadle.no' and answers[3] == 'kadle.no' and answers[4] == 'kadle.no':
                    msg = "You love your second wife as much as your cow, but you don't love both enough to carry them. 6/10 would marry"
                    await ctx.send(ctx.message.author.mention + msg)
                elif answers[0] == 'kadle.no' and answers[1] == 'kadle.no' and answers[2] == 'kadle.yes' and answers[3] == 'kadle.yes' and answers[4] == 'kadle.yes':
                    msg = "You are a selfish gay bastard who drinks too much milk and still somehow carries. 2/10 would marry"
                    await ctx.send(ctx.message.author.mention + msg)
                elif answers[0] == 'kadle.no' and answers[1] == 'kadle.no' and answers[2] == 'kadle.yes' and answers[3] == 'kadle.yes' and answers[4] == 'kadle.no':
                    msg = "You are a selfish gay bastard who only drinks milk. 0/10 would marry"
                    await ctx.send(ctx.message.author.mention + msg)
                elif answers[0] == 'kadle.no' and answers[1] == 'kadle.no' and answers[2] == 'kadle.yes' and answers[3] == 'kadle.no' and answers[4] == 'kadle.yes':
                    msg = "You should have been born a cow. 10/10 would marry even if I was a cow cause I'm gay"
                    await ctx.send(ctx.message.author.mention + msg)
                elif answers[0] == 'kadle.no' and answers[1] == 'kadle.no' and answers[2] == 'kadle.yes' and answers[3] == 'kadle.no' and answers[4] == 'kadle.no':
                    msg = "You should have been born a cow. That way you can't snipe anymore. 0/10 would marry"
                    await ctx.send(ctx.message.author.mention + msg)
                elif answers[0] == 'kadle.no' and answers[1] == 'kadle.no' and answers[2] == 'kadle.no' and answers[3] == 'kadle.yes' and answers[4] == 'kadle.yes':
                    msg = "You don't care about anyone or anything except carryying. 1/10 would marry"
                    await ctx.send(ctx.message.author.mention + msg)
                elif answers[0] == 'kadle.no' and answers[1] == 'kadle.no' and answers[2] == 'kadle.no' and answers[3] == 'kadle.yes' and answers[4] == 'kadle.no':
                    msg = "Why are you even alive? -10/10 would marry"
                    await ctx.send(ctx.message.author.mention + msg)
                elif answers[0] == 'kadle.no' and answers[1] == 'kadle.no' and answers[2] == 'kadle.no' and answers[3] == 'kadle.no' and answers[4] == 'kadle.yes':
                    msg = "Rainbow is life, am I right? :rainbow:/10 would marry"
                    await ctx.send(ctx.message.author.mention + msg)
                elif answers[0] == 'kadle.no' and answers[1] == 'kadle.no' and answers[2] == 'kadle.no' and answers[3] == 'kadle.no' and answers[4] == 'kadle.no':
                    msg = "What is life? 1/10 would marry"
                    await ctx.send(ctx.message.author.mention + msg)
                    

        else:
                    await ctx.send(ctx.message.author.mention + " Answer madalla andre time waste madbeda goobe")
            
def setup(bot):
    """Adds the Class to the cog and logs to console"""
    bot.add_cog(Love(bot))
    print('lovebot is loaded')
