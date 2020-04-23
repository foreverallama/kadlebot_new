import discord
from discord.ext import commands

class Help(commands.Cog):
    """Contains the help command. To add this cog the default help command
        must be disabled first"""

    def __init__(self,bot):
        self.bot = bot

    @commands.command(name='help',
                      help='Displays help message',
                      usage='kadle.help',
                      hidden=True)
    async def help(self, ctx, payload=None):
        e = discord.Embed(type="rich", color=0x91f735)
       
        if payload is None:
            e.title = "List of commands"
            e.description = "These are all the available commands for Kadle Bot," \
                            " separated by category. All commands are case sensitive"
            
            e.set_footer(text="Type kadle.help [category] for more info about the category" 
                     ", or kadle.help [command] for more info about a command.")

            gaystuff = '```date          Date a User\n' \
                       'dateme        Date Kadle\n' \
                       'howgay        How gay are you\n' \
                       'image         Sends an image\n' \
                       'message       Sends a message\n' \
                       'say           Says what you want\n' \
                       'video         Sends a video\n' \
                       'whisper       Whispers a secret```'

            e.add_field(name='Category: GayStuff', value=gaystuff, inline=False)

            musicstuff = '```add           Add song to Queue\n' \
                          'join          Join voice channel\n' \
                          'leave         Leave voice channel\n' \
                          'next          Play next song\n' \
                          'pause         Pause the player\n' \
                          'play          Play a song\n' \
                          'queue         Display queue\n' \
                          'remove        Remove from queue\n' \
                          'resume        Resume player\n' \
                          'stop          Stop the player\n' \
                          'volume        Set the volume\n' \
                          'setsearch     Set search option```'

            e.add_field(name='Category: Music', value=musicstuff, inline=False)

            spawnstuff = '```spawn         Set spawn channel\n' \
                         'list          Displays your Kadledex\n' \
                         'select        Select a Kadle as your companion\n' \
                         'moves         List moves for your Kadle```'

            e.add_field(name='Category: Kadlemon', value=spawnstuff, inline=False)

##            otherstuff = '```videocall     Sends link to join a video call```'
##            e.add_field(name='Category: Others', value=otherstuff, inline=False)

        elif payload.upper() == "GAYSTUFF":
            e.title = "List of commands for Category: GayStuff"
            e.description = "These commands basically do gay stuff"
            
            e.set_footer(text="Type kadle.help [command] for more info about a command.")

            gaystuff = '```date          Date a User\n' \
                       'dateme        Date Kadle\n' \
                       'howgay        How gay are you\n' \
                       'image         Sends an image\n' \
                       'message       Sends a message\n' \
                       'say           Says what you want\n' \
                       'video         Sends a video\n' \
                       'whisper       Whispers a secret```'

            e.add_field(name='Category: GayStuff', value=gaystuff, inline=False)

        elif payload.upper() == "MUSIC":
            e.title = "List of commands for Category: Music"
            e.description = "These commands are used to play audio in your voice channel"
            e.set_footer(text="Type kadle.help [command] for more info about a command.")

            musicstuff = '```add           Add song to Queue\n' \
                          'join          Join voice channel\n' \
                          'leave         Leave voice channel\n' \
                          'next          Play next song\n' \
                          'pause         Pause the player\n' \
                          'play          Play a song\n' \
                          'queue         Display queue\n' \
                          'remove        Remove from queue\n' \
                          'resume        Resume player\n' \
                          'stop          Stop the player\n' \
                          'volume        Set the volume\n' \
                          'setsearch     Set search option```'

            e.add_field(name='Category: Music', value=musicstuff, inline=False)

        elif payload.upper() == "KADLEMON":
            e.title = "List of commands for Category: Kadlemon"
            e.description = "These commands are used to play Kadlemon." \
                            " This is still under development"
            
            e.set_footer(text="Type kadle.help [command] for more info about a command.")

            spawnstuff = '```spawn         Set spawn channel\n' \
                         'list          Displays your Kadledex\n' \
                         'select        Select a Kadle as your companion\n' \
                         'moves         List moves for your Kadle```'

            e.add_field(name='Category: Kadlemon', value=spawnstuff, inline=False)

##        elif payload.upper() == "OTHERS":
##            e.title = "List of commands for Category: Others"
##            e.description = "These commands don't belong to the other categories"                        
##            e.set_footer(text="Type kadle.help [command] for more info about a command.")
##
##            otherstuff = '```videocall     Sends link to join a video call```'
##            e.add_field(name='Category: Others', value=otherstuff, inline=False)

        elif payload.upper() == "DATE":
            e.set_author(name="Category: GayStuff")
            e.title = "Command: date"
            e.description = "Kadle checks your compatibility with another user"
            e.add_field(name='Usage', value='```kadle.date @mention```', inline=False)
            e.add_field(name='Example', value='```kadle.date @Kadle Bot#5024```', inline=False)

        elif payload.upper() == "DATEME":
            e.set_author(name="Category: GayStuff")
            e.title = "Command: dateme"
            e.description = "Kadle decides if you're worthy enough to go on a date with him"
            e.add_field(name='Usage', value='```kadle.dateme```', inline=False)
            e.add_field(name='Example', value='```kadle.dateme```', inline=False)

        elif payload.upper() == "HOWGAY":
            e.set_author(name="Category: GayStuff")
            e.title = "Command: howgay"
            e.description = "Tells you how gay you are"
            e.add_field(name='Usage', value='```kadle.howgay```', inline=False)
            e.add_field(name='Example', value='```kadle.howgay```', inline=False)

        elif payload.upper() == "IMAGE":
            e.set_author(name="Category: GayStuff")
            e.title = "Command: image"
            e.description = "Sends an image of Kadle"
            e.add_field(name='Usage', value='```kadle.image```', inline=False)
            e.add_field(name='Example', value='```kadle.image```', inline=False)

        elif payload.upper() == "MESSAGE":
            e.set_author(name="Category: GayStuff")
            e.title = "Command: message"
            e.description = "Kadle tells you something"
            e.add_field(name='Usage', value='```kadle.message```', inline=False)
            e.add_field(name='Example', value='```kadle.message```', inline=False)

        elif payload.upper() == "SAY":
            e.set_author(name="Category: GayStuff")
            e.title = "Command: say"
            e.description = "Kadle says what you want, in his voice"
            e.add_field(name='Usage', value='```kadle.say [text]```', inline=False)
            e.add_field(name='Examples', value='```kadle.say hello```\n```kadle.say goodbye```', inline=False)

        elif payload.upper() == "VIDEO":
            e.set_author(name="Category: GayStuff")
            e.title = "Command: video"
            e.description = "Sends a video of Kadle"
            e.add_field(name='Usage', value='```kadle.video```', inline=False)
            e.add_field(name='Example', value='```kadle.video```', inline=False)

        elif payload.upper() == "WHISPER":
            e.set_author(name="Category: GayStuff")
            e.title = "Command: whisper"
            e.description = "Kadle whispers to you one of his deepest, darkest secrets"
            e.add_field(name='Usage', value='```kadle.whisper```', inline=False)
            e.add_field(name='Example', value='```kadle.whisper```', inline=False)

        elif payload.upper() == "ADD":
            e.set_author(name="Category: Music")
            e.title = "Command: add"
            e.description = "Adds a song to the play queue"
            e.add_field(name='Usage', value='```kadle.add [song name]```', inline=False)
            e.add_field(name='Examples', value='```kadle.add never gonna give you up rick astley```\n```kadle.add all star smash mouth```', inline=False)

        elif payload.upper() == "JOIN":
            e.set_author(name="Category: Music")
            e.title = "Command: join"
            e.description = "Joins the voice channel the user is in. Note that you should have joined a voice channel first"
            e.add_field(name='Usage', value='```kadle.join```', inline=False)
            e.add_field(name='Example', value='```kadle.join```', inline=False)

        elif payload.upper() == "LEAVE":
            e.set_author(name="Category: Music")
            e.title = "Command: leave"
            e.description = "Disconnects from the voice channel"
            e.add_field(name='Usage', value='```kadle.leave```', inline=False)
            e.add_field(name='Example', value='```kadle.leave```', inline=False)

        elif payload.upper() == "NEXT":
            e.set_author(name="Category: Music")
            e.title = "Command: next"
            e.description = "Plays the next song in queue"
            e.add_field(name='Usage', value='```kadle.next```', inline=False)
            e.add_field(name='Example', value='```kadle.next```', inline=False)

        elif payload.upper() == "PAUSE":
            e.set_author(name="Category: Music")
            e.title = "Command: pause"
            e.description = "Pauses the audio player"
            e.add_field(name='Usage', value='```kadle.pause```', inline=False)
            e.add_field(name='Example', value='```kadle.pause```', inline=False)

        elif payload.upper() == "PLAY":
            e.set_author(name="Category: Music")
            e.title = "Command: play"
            e.description = "Plays a song. Note that Kadle Bot should have joined a voice channel first." \
                            " Note: For best results with spotify search, use the format [artist] - [track name]"
            e.add_field(name='Usage', value='```kadle.play [song name]```', inline=False)
            e.add_field(name='Examples', value='```kadle.play never gonna give you up rick astley```\n```kadle.play all star smash mouth```', inline=False)

        elif payload.upper() == "QUEUE":
            e.set_author(name="Category: Music")
            e.title = "Command: queue"
            e.description = "Displays the playing Queue"
            e.add_field(name='Usage', value='```kadle.queue```', inline=False)
            e.add_field(name='Example', value='```kadle.queue```', inline=False)

        elif payload.upper() == "REMOVE":
            e.set_author(name="Category: Music")
            e.title = "Command: remove"
            e.description = "Removes a song from the queue. The song is specified by the track number in the playing queue. Any song except for the one that is currently playing can be removed"
            e.add_field(name='Usage', value='```kadle.remove [track number]```', inline=False)
            e.add_field(name='Example', value='```kadle.remove 4```', inline=False)

        elif payload.upper() == "RESUME":
            e.set_author(name="Category: Music")
            e.title = "Command: resume"
            e.description = "Resumes the audio player"
            e.add_field(name='Usage', value='```kadle.resume```', inline=False)
            e.add_field(name='Example', value='```kadle.resume```', inline=False)

        elif payload.upper() == "STOP":
            e.set_author(name="Category: Music")
            e.title = "Command: stop"
            e.description = "Stops playing audio and clears the queue"
            e.add_field(name='Usage', value='```kadle.stop```', inline=False)
            e.add_field(name='Example', value='```kadle.stop```', inline=False)

        elif payload.upper() == "VOLUME":
            e.set_author(name="Category: Music")
            e.title = "Command: volume"
            e.description = "Adjusts the volume of the audio player. Volume is between 0-100"
            e.add_field(name='Usage', value='```kadle.volume [volume]```', inline=False)
            e.add_field(name='Example', value='```kadle.volume 69```', inline=False)

        elif payload.upper() == "SETSEARCH":
            e.set_author(name="Category: Music")
            e.title = "Command: setsearch"
            e.description = "Sets the website to stream audio from. Currently supported options are Spotify and YouTube. If not set, it is YouTube by default"          
            e.add_field(name='Usage', value='```kadle.setsearch [website]```', inline=False)
            e.add_field(name='Examples', value='```kadle.setsearch spotify```\n```kadle.setsearch youtube```', inline=False)

        elif payload.upper() == "SPAWN":
            e.set_author(name="Category: Kadlemon")
            e.title = "Command: spawn"
            e.description = "Sets the text-channel for Kadlemon to spawn in"
            e.add_field(name='Usage', value='```kadle.spawn [text-channel-name]```', inline=False)
            e.add_field(name='Example', value='```kadle.spawn general```', inline=False)

        elif payload.upper() == "LIST":
            e.set_author(name="Category: Kadlemon")
            e.title = "Command: list"
            e.description = "Displays all Kadles you've caught"
            e.add_field(name='Usage', value='```kadle.list```', inline=False)
            e.add_field(name='Example', value='```kadle.list```', inline=False)

        elif payload.upper() == "SELECT":
            e.set_author(name="Category: Kadlemon")
            e.title = "Command: select"
            e.description = "Selects a Kadle as your active companion"
            e.add_field(name='Usage', value='```kadle.select [number]```', inline=False)
            e.add_field(name='Example', value='```kadle.select 4 ``', inline=False)

        elif payload.upper() == "MOVES":
            e.set_author(name="Category: Kadlemon")
            e.title = "Command: moves"
            e.description = "Lists all the moves of your selected Kadle"
            e.add_field(name='Usage', value='```kadle.moves```', inline=False)
            e.add_field(name='Example', value='```kadle.moves```', inline=False)

##        elif payload.upper() == "VIDEOCALL":
##            e.set_author(name="Category: Others")
##            e.title = "Command: videocall"
##            e.description = "Sends a link for users to start or join a video call on a voice channel"
##            e.add_field(name='Usage', value='```kadle.videocall```', inline=False)
##            e.add_field(name='Example', value='```kadle.videocall```', inline=False)

        else:
            await ctx.send("That command does not exist (yet)")
            return

        await ctx.send(embed=e, delete_after=300)
        

def setup(bot):
    bot.add_cog(Help(bot))
    print('help.py is loaded')
