import os
import shutil
from os import system
import discord
import youtube_dl
from discord.ext import commands
from discord.utils import get
import random
import json

## Use this if you are going to upload this on Heroku
if not discord.opus.is_loaded():
    discord.opus.load_opus('./libopus.so')

## Global variable storing queue info of all the servers its on
## Changes to files on heroku do not get saved if the dyno restarts
## Hence, a global variable is used here. A file can also be used
## To ensure data is saved across dynos, you need to link your bot to a database
## Look up mongodb or others
song_list_queue = {}

def __init__(self, bot):
    self.bot = bot

class MusicBot(commands.Cog):
    """Commands for Category: Music

    Commands
    --------
    add:
        Adds a song to the queue
    join:
        Joins a voice channel
    leave:
        Leaves the voice channel
    play:
        Plays a song
    stop:
        Stops playing
    resume:
        Resumes playing
    pause:
        Pauses the player
    queue:
        Displays the queue
    next:
        Plays next song
    volume:
        Adjusts volume
    setsearch:
        Sets search option as either Spotify or YouTube

    """
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='Join',
                      description='Join voice',
                      brief='Joins  a voice channel',
                      help='Joins the voice channel the user is in',
                      pass_context=True,
                      usage='kadle.join',
                      cog='MusicBot')
    async def join(self, ctx):
        if ctx.message.author.voice is None:
            await ctx.send("You need to join a voice channel first")
            return
        
        channel = ctx.message.author.voice.channel
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        
        if voice is not None:
            return await voice.move_to(channel)

        await channel.connect()

        await ctx.send(f"Now ready to play bhajans on {channel}")

## Used the bot to send a video call link within the server voice channel
## This was done before the feature was pushed onto all servers

##    @commands.command(name='videocall')
##    async def videocall(self, ctx):
##        if ctx.message.author.voice is None:
##            await ctx.send("You need to join a voice channel first")
##            return
##
##        url = "https://discordapp.com/channels/" + str(ctx.guild.id) + "/" + str(ctx.message.author.voice.channel.id)
##
##        e = discord.Embed(type="rich", color=0x91f735)
##        e.title = "Video Call on Voice Channel: " + ctx.message.author.voice.channel.name
##        e.description = "Click on the link below to join an ongoing video call. You should be connected to the voice channel first"
##        e.set_footer(text="For more info on my commands, type kadle.help")
##        e.add_field(name="Link", value=url)
##
##        await ctx.send(embed=e)        


    @commands.command(name='Leave',
                      description='Leaves voice',
                      brief='Leaves voice channel',
                      help='Leaves the voice channel it is in',
                      pass_context=True,
                      usage='kadle.leave',
                      cog='MusicBot'
                      )
    async def leave(self, ctx):
        voice = get(self.bot.voice_clients, guild=ctx.guild)

        if voice and voice.is_connected():
            await voice.disconnect()
            await ctx.send(f"No more bhajans for today")
        else:
            await ctx.send("Amman where you want me to leave from?")


    @commands.command(name='Play',
                      description='Plays a song from YouTube',
                      brief='Plays  song',
                      help='Plays a song specified by keyword or url',
                      pass_context=True,
                      usage='kadle.play [url/song_name]',
                      cog='MusicBot'
                      )
    async def play(self, ctx, *url: str):
        global song_list_queue

        voice = get(self.bot.voice_clients, guild=ctx.guild)
        
        if voice is None:
            await ctx.send("You have to add me to a voice channel first")
            return

##        List of predifined URLs to download from if user does not specify a song
        list_of_bhajans = ['https://www.youtube.com/watch?v=iW16WWmWZL4',
               'https://www.youtube.com/watch?v=2yAzgg3zEjM',
               'https://www.youtube.com/watch?v=Ezhdk82sR1Y',
               ]
        if not url:
            url = random.choice(list_of_bhajans)
            
        """
            A downloaded song is added to a folder named by the server ID
            and named as 'song.mp3'
            Songs in queue are added to a folder 'Queue' within this folder
            and are named as 'song1.mp3', 'song2.mp3' and so on
        """
        def check_queue():
            Queue_infile = os.path.isdir("./" + str(ctx.guild.id) + "/Queue")
            if Queue_infile is True:
                DIR = os.path.abspath(os.path.realpath(str(ctx.guild.id) + "/Queue"))
                length = len(os.listdir(DIR))
                still_q = length - 1            
                try:
                    first_file = os.listdir(DIR)[0]
                except:
##                    print("No more queued song(s)\n")                    
                    removed_value = song_list_queue.pop(ctx.guild.id, 'No Key Found')
                    return
                main_location = os.path.dirname(os.path.realpath(__file__))
                main_location += "/" + str(ctx.guild.id)                
                song_path = os.path.abspath(os.path.realpath(str(ctx.guild.id) + "/Queue") + "/" + first_file)
                
                if length != 0:
##                    print("Song done, playing next queued\n")
##                    print(f"Songs still in queue: {still_q}")
                    song_there = os.path.isfile(str(ctx.guild.id) + "/song.mp3")
                    if song_there:
                        os.remove(str(ctx.guild.id) + "/song.mp3")
                    shutil.move(song_path, main_location)
                    for file in os.listdir("./" + str(ctx.guild.id)):
                        if file.endswith(".mp3"):
                            os.rename(str(ctx.guild.id) + "/" + file, str(ctx.guild.id) + "/song.mp3")

                    removed_value = song_list_queue.setdefault(ctx.guild.id, []).pop(0)

                    voice.play(discord.FFmpegPCMAudio(str(ctx.guild.id) + "/song.mp3"), after=lambda e: check_queue())
                    voice.source = discord.PCMVolumeTransformer(voice.source)
                    voice.source.volume = 0.2

                else:
                    removed_value = song_list_queue.pop(ctx.guild.id, 'No Key Found')                    
                    return

            else:               
                removed_value = song_list_queue.pop(ctx.guild.id, 'No Key Found')                            
##                print("No songs were queued before the ending of the last song\n")



        song_there = os.path.isfile(str(ctx.guild.id) + "/song.mp3")        
        try:
            if song_there:
                os.remove(str(ctx.guild.id) + "/song.mp3")           
                removed_value = song_list_queue.pop(ctx.guild.id, 'No Key Found')                
##                print("Removed old song file")
        except PermissionError:
##            print("Trying to delete song file, but it's being played")
            await ctx.send("A song is already playing. Type kadle.queue [song] to add a song to the queue. To delete the queue, type kadle.stop")
            return


        Queue_infile = os.path.isdir("./" + str(ctx.guild.id) + "/Queue")        
        try:
            Queue_folder = "./" + str(ctx.guild.id) + "/Queue"            
            if Queue_infile is True:
##                print("Removed old Queue Folder")
                shutil.rmtree(Queue_folder)
        except:
##            print("No old Queue folder")
            pass

        await ctx.send("Getting things ready. Please wait")
        
        ## Check docs of youtube-dl for more info
        ydl_opts = {
            'format': 'bestaudio/best',
            'quiet': False,
            'outtmpl': "./" + str(ctx.guild.id) + "/song.mp3",
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

        if isinstance(url, str):
            song_search = "".join(url)
        else:
            song_search = " ".join(url)

        with open('server_settings/search_options.json', 'r') as jsonFile:
            try:
                data = json.load(jsonFile)
                print("Data:\n")
                print(data)
            except:
                data = {}
                data[str(ctx.guild.id)] = "YOUTUBE"

        search_method = data[str(ctx.guild.id)]
        print("Search Method: " + search_method)

        if search_method == "YOUTUBE":

            try:
                with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                    print("Downloading audio now\n")
                    ydl.download([f"ytsearch1:{song_search}"])
                    info_dict = ydl.extract_info(f"ytsearch1:{song_search}", download=False, ie_key='YoutubeSearch')
                    song_title = None
                    for res in info_dict.get('entries'):
                        if 'title' in res.keys():
                            song_title = res['title']
                            break
                    song_list_queue.setdefault(ctx.guild.id, []).append(song_title)

            except:
                print("Error in YouTube download")
                await ctx.send("Sorry. I encountered an error. Please try again later")
                return

        else:
            
            try:                
                c_path = os.path.dirname(os.path.realpath(__file__))
                c_path += "/" + str(ctx.guild.id) 
                system("spotdl -f " + '"' + c_path + '"' + " -s " + song_search)
                for file in os.listdir("./" + str(ctx.guild.id)):
                    if file.endswith(".mp3"):
                        song_title = file[:-4]
                        song_list_queue.setdefault(ctx.guild.id, []).append(song_title)
                        os.rename(str(ctx.guild.id) + "/" + file, str(ctx.guild.id) + "/song.mp3")

            except:
                print("Error in Spotify download")
                await ctx.send("Sorry. I encountered an error. Please try again later")
                return
            

        voice.play(discord.FFmpegPCMAudio(str(ctx.guild.id) + "/song.mp3"), after=lambda e: check_queue())
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = 0.2

        if song_title is None:
            await ctx.send("Could not find the song")
        else:
            await ctx.send("Now playing " + song_title)

    @commands.command(name='Pause',
                      description='Pauses the player',
                      brief='Pauses the song',
                      help='Pauses the player',
                      pass_context=True,
                      usage='kadle.pause',
                      cog='MusicBot'
                      )
    async def pause(self, ctx):

        voice = get(self.bot.voice_clients, guild=ctx.guild)

        if voice and voice.is_playing():
            voice.pause()
            await ctx.send("Music has been paused")
        else:
            await ctx.send("I'll pause you if you simply call me")


    @commands.command(name='Resume',
                      description='Resumes audio',
                      brief='Resumes audio',
                      help='Resumes playing the audio track',
                      pass_context=True,
                      usage='kadle.resume',
                      cog='MusicBot'
                      )
    async def resume(self, ctx):

        voice = get(self.bot.voice_clients, guild=ctx.guild)

        if voice and voice.is_paused():
            voice.resume()
            await ctx.send("Resumed the player")
        else:
            await ctx.send("Resume your ass")


    @commands.command(name='Stop',
                      description='Stops the player',
                      brief='Stops audio',
                      help='Stops the player',
                      pass_context=True,
                      usage='kadle.stop',
                      cog='MusicBot'
                      )
    async def stop(self, ctx):
        global song_list_queue
        
        voice = get(self.bot.voice_clients, guild=ctx.guild)
     
        removed_value = song_list_queue.pop(ctx.guild.id, 'No Key Found')                

        queue_infile = os.path.isdir("./" + str(ctx.guild.id) + "/Queue")
        if queue_infile is True:
            shutil.rmtree("./" + str(ctx.guild.id) + "/Queue")

        if voice and voice.is_playing():
            voice.stop()
            await ctx.send("Music has been stopped and queue has been cleared")
        else:
            await ctx.send("There is nothing to stop")

    @commands.command(name='Queue',
                      description='Lists all the songs in queue',
                      brief='Lists queue',
                      help='Lists all the songs remaining in the queue',
                      pass_context=True,
                      usage='kadle.queue',
                      cog='MusicBot'
                      )
    async def queue(self, ctx):
        global song_list_queue

        if ctx.guild.id in song_list_queue.keys():
            song_list = song_list_queue[ctx.guild.id]
        else:
            await ctx.send("There are no songs in queue")
            return
        length = len(song_list)
        song_list = '\n'.join(song_list)

        await ctx.send(f"There are {length} song(s) in the queue. Songs in the list are:\n{song_list}")


    @commands.command(name='Add',
                      description='Adds to queue',
                      brief='Adds a song to the queue',
                      help='Adds song to the queue',
                      pass_context=True,
                      usage='kadle.add [url/song_name]',
                      cog='MusicBot'
                      )
    async def add(self, ctx, *url: str):
        global song_list_queue

        voice = get(self.bot.voice_clients, guild=ctx.guild)
        
        if voice is None:
            await ctx.send("Play a song first using kadle.play. Use this command to add songs to the queue")
            return

        list_of_bhajans = ['https://www.youtube.com/watch?v=iW16WWmWZL4',
               'https://www.youtube.com/watch?v=2yAzgg3zEjM',
               'https://www.youtube.com/watch?v=Ezhdk82sR1Y',
               ]
        if not url:
            url = random.choice(list_of_bhajans)
          
        Queue_infile = os.path.isdir("./" + str(ctx.guild.id) + "/Queue")        
        if Queue_infile is False:
            os.mkdir(str(ctx.guild.id) + "/Queue")
        DIR = os.path.abspath(os.path.realpath(str(ctx.guild.id) + "/Queue"))        
        q_num = len(os.listdir(DIR))
        q_num += 1

        queue_path = os.path.abspath(os.path.realpath(str(ctx.guild.id) + "/Queue") + f"/song{q_num}.%(ext)s")

        ydl_opts = {
            'format': 'bestaudio/best',
            'quiet': True,
            'outtmpl': queue_path,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

        if isinstance(url, str):
            song_search = "".join(url)
        else:
            song_search = " ".join(url)

        await ctx.send("Getting Things ready. Please Wait")

        with open('server_settings/search_options.json') as jsonFile:
            try:
                data = json.load(jsonFile)
            except:
                data = {}
                data[str(ctx.guild.id)] = "YOUTUBE"

        search_method = data[str(ctx.guild.id)]

        if search_method == "YOUTUBE":

            try:
                with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ##                print("Downloading audio now\n")
                    ydl.download([f"ytsearch1:{song_search}"])
                    info_dict = ydl.extract_info(f"ytsearch1:{song_search}", download=False, ie_key='YoutubeSearch')
                    song_title = None
                    for res in info_dict.get('entries'):
                        if 'title' in res.keys():
                            song_title = res['title']
                            break
                    song_list_queue.setdefault(ctx.guild.id, []).append(song_title)

            except:
                print("Error in YouTube download")
                await ctx.send("Sorry. I encountered an error. Please try again later")
                return

        else:
                
            try:
##                print("FALLBACK: youtube-dl does not support this URL, using Spotify (This is normal if Spotify URL)")
                q_path = os.path.abspath(os.path.realpath(str(ctx.guild.id) + "/Queue"))
                system(f"spotdl -f " + '"' + q_path + '"' + " -s " + song_search)
                for file in os.listdir("./" + str(ctx.guild.id) + "/Queue"):
                    if file.endswith(".mp3"):
                        song_title = file[:-4]
                        song_list_queue.setdefault(ctx.guild.id, []).append(song_title)
                        os.rename(str(ctx.guild.id) + "/Queue/" + file, str(ctx.guild.id) + "/Queue/song" + str(q_num) + ".mp3")

            except:
                print("Error in Spotify download")
                await ctx.send("Sorry. I encountered an error. Please try again later")
                return

        if song_title is None:
            await ctx.send("Could not find the song")
        else:
            await ctx.send("Added " + song_title + " to the queue")


        print("Song added to queue\n")


    @commands.command(name='Next',
                      description='Plays next song in queue',
                      brief='Plays next song',
                      help='Plays the next song in queue',
                      pass_context=True,
                      usage='kadle.next',
                      cog='MusicBot'
                      )
    async def next(self, ctx):
        voice = get(self.bot.voice_clients, guild=ctx.guild)

        Queue_infile = os.path.isdir("./" + str(ctx.guild.id) + "/Queue")        
        if Queue_infile is False:
            await ctx.send("There are no more songs in queue")
            return
        else:
            DIR = os.path.abspath(os.path.realpath(str(ctx.guild.id) + "/Queue"))
            length = len(os.listdir(DIR))
            if length == 0:
                await ctx.send("There are no more songs in queue")
                return

        if voice and voice.is_playing():
            voice.stop()
            await ctx.send("Playing the next song in queue")
        else:
            await ctx.send("There are no songs in queue")


    @commands.command(name='Volume',
                      description='Adjusts the player volume',
                      brief='Adjust the volume',
                      help='Adjust the volume of the audio track',
                      pass_context=True,
                      usage='kadle.volume [0-100]',
                      cog='MusicBot'
                      )
    async def volume(self, ctx, volume: int):

        if ctx.voice_client is None:
            return await ctx.send("Not connected to voice channel")

        print(volume/100)

        ctx.voice_client.source.volume = volume / 100
        await ctx.send(f"Changed volume to {volume}%")

    @commands.command(name='Remove',
                      description='Removes a song from the queue',
                      brief='Remove from queue',
                      help='Removes a song from the queue',
                      pass_context=True,
                      usage='kadle.remove [track number]',
                      cog='MusicBot')
    async def remove(self, ctx, track_no: int):

        Queue_infile = os.path.isdir("./" + str(ctx.guild.id) + "/Queue")
        if Queue_infile is False:
            await ctx.send("There are no songs in the queue to remove")
            return
        else:
            DIR = os.path.abspath(os.path.realpath(str(ctx.guild.id) + "/Queue"))
            length = len(os.listdir(DIR))
            if length == 0:
                await ctx.send("There are no songs in queue")
                return
            if track_no > length + 1:
                await ctx.send("There aren't that many tracks in the queue")
                return

            song_there = os.path.isfile("./" + str(ctx.guild.id) + "/Queue/song" + str(track_no-1) + ".mp3")
            if song_there:
                os.remove("./" + str(ctx.guild.id) + "/Queue/song" + str(track_no-1) + ".mp3")
                removed_value = song_list_queue.setdefault(ctx.guild.id, []).pop(track_no-1)
                await ctx.send(f"The track {removed_value} has been removed from the queue")

    @commands.command(name='setsearch',
                      description='Set music search option as Spotify or Youtube',
                      brief='Set search option',
                      help='Set the search option as Spotify/YouTube (default is YouTube',
                      pass_context=True,
                      usage='kadle.setsearch spotify',
                      cog='MusicBot')
    async def setsearch(self, ctx, payload = None):

        if payload is None:
            await ctx.send("Set to what?")
            return

        available_opts = ['SPOTIFY', 'YOUTUBE']

        if any(word in payload.upper() for word in available_opts):
            with open('server_settings/search_options.json', 'r') as jsonFile:
                try:
                    data = json.load(jsonFile)
                except:
                    data = {}

            data[str(ctx.guild.id)] = payload.upper()
            print("Set search data:\n")
            print(data)

            with open('server_settings/search_options.json', 'w') as jsonFile:
                json.dump(data, jsonFile)
            
            await ctx.send(f"Search option has been set to {payload}")

        else:
            await ctx.send("That is not an available option")
        
                
def setup(bot):
    bot.add_cog(MusicBot(bot))
    print('musicbot.py is loaded')



