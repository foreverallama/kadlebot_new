import discord
from discord.ext import commands
import os
import random

TOKEN = os.environ.get('TOKEN',None)
## TOKEN required to run the bot
## Get at discordapp.com/developers/applications/me

bot = commands.Bot(command_prefix='kadle.',
                   description="",
                   case_insensitive=True,
                   owner_id=391864327398883329,
                   help_command=None
                   )

@bot.event
async def on_message(message):
##    So that the bot does not reply to itself
    if message.author == bot.user:
        return

    if message.content.startswith('kadle.'):
        await bot.process_commands(message)
                    
@bot.event
async def on_ready():
    """Logs to console once it is ready.
        Creates directories which will be used in other cogs"""
    game = discord.Game("kadle.help")
    await bot.change_presence(activity=game)
    print('Logged in')
    for guild in bot.guilds:
        os.mkdir(str(guild.id))
    print('Directories created')

## This function is used to handle errors. See discord.py docs for more details
##@bot.event
##async def on_command_error(error, ctx):
##    if isinstance(error, commands.CommandNotFound) and ctx.message.content.startswith("kadle.catch"):
##        return

@bot.command(name='load',
             help='Loads extensions',
             usage='kadle.load',
             hidden=True)
async def load(ctx, extension):
    """Loads a cog"""
    if ctx.message.author.id == 391864327398883329 and ctx.guild.id == 455640405371912204:
        bot.load_extension(extension)
        print(f'{extension} has been loaded')

@bot.command(name='unload',
             help='Unloads extensions',
             usage='kadle.unload',
             hidden=True)
async def unload(ctx, extension):
    """Unloads a cog"""
    if ctx.message.author.id == 391864327398883329 and ctx.guild.id == 455640405371912204:
        bot.unload_extension(extension)
        print(f'{extension} has been unloaded')

@bot.command(name='reload',
             help='Reloads extensions',
             usage='kadle.reload',
             hidden=True)
async def reload(ctx, extension):
    """Reloads a cog"""
    if ctx.message.author.id == 391864327398883329 and ctx.guild.id == 455640405371912204:
        bot.reload_extension(extension)
        print(f'{extension} has been reloaded')

@bot.command(name='clear',
             help='clears internal state of bot',
             usage='kadle.clear',
             hidden=True)
async def clear():
    """Clears the internal state of the bot"""
    if ctx.message.author.id == 391864327398883329 and ctx.guild.id == 455640405371912204:
        bot.clear()
        print('bot has been cleared')

        
## Load all my cogs
startup_extensions = []
for filename in os.listdir('./'):
	if filename.endswith('.py') and not filename.startswith('main'):
		startup_extensions.append(filename[:-3])

if __name__ == "__main__":
    """Loads all the cogs added to the bot"""
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__,e)
            print('Failed to load extension {}\n{}'.format(extension, exc))
                
bot.run(TOKEN)

