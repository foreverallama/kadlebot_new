# kadlebot_new
A simple discord bot written in Python (discord.py rewrite)

Requirements
===========
* Python 3 (written in Python 3.6 within a Conda environment)
* `discord` 1.3.3: `pip install discord.py`
* `discord[voice]` 1.3.0: `pip install discord.py[voice]` (More info [here](https://discordpy.readthedocs.io/en/latest/intro.html "Discord.py docs")
* `youtube-dl` 2020.3.24: `pip install youtube-dl`
* `spotdl` 1.2.6: `pip install spotdl`
* `numpy` 1.18.2: `pip install numpy`
* `libopus.so` opus library if you're using linux (included by default for windows)(optional, voice only)
* FFmpeg is required to stream audio. It can be downloaded from [here](https://www.ffmpeg.org/download.html "FFmpeg")
* The files `runtime.txt`, `requirements.txt`, `Procfile` and `libopus.so` are required to deploy it on Heroku. Check the [Heroku Docs](https://devcenter.heroku.com/categories/command-line "Heroku CLI") to find out how to deploy this on Heroku
* The _updates_ folder contains Cogs which will be added sometime in the future

**Note1**: To host the bot on Heroku, you need the ffmpeg buildpack. Click [here](https://elements.heroku.com/buildpacks/jonathanong/heroku-buildpack-ffmpeg-latest) and follow the instructions to add the buildpack
**Note2**: Files in the folder `kadlemon` and `kadlepics` have been removed to respect privacy. Image files were named as `IMG1`, `IMG2` and so on while video files were named `VID1`, `VID2` and so on. Video files uploaded to discord need to be below 8MB.
**Note3**: Your bot requires a Token to run, which can be obtained at _discordapp.com/developers/applications/me_
**Note3**: If you're wondering what a _Kadle_ is, it's my friend's nickname. This bot was basically built to mock him

`mainbot.py`
===========
* Creates the bot with prefix **kadle.**
* Loads files `gaybot.py`, `musicbot.py`, `message_filter.py`, `help.py`, `spawnbot.py`
* The default help command has been removed and a new one was created and added to a cog **Help**

`gaybot.py`
==========
**Cog:** GayStuff

Commands
--------------
- **kadle.message**  
Sends a random message from given list into the same channel as requested by the user

- **kadle.image**  
Sends a random image from the given list into the same channel as requested by the user

- **kadle.video**  
Sends a random video from the given list into the same channel as requested by the user

- **kadle.howgay**  
Replies back to the user saying how gay they are (Replies with 100% gay only for kadle)

- **kadle.say**  
Repeats back the text entered by the user

- **kadle.whisper**  
DM's the user with a random secret defined in the list

- **kadle.date**
Returns the percentage compatibility with the mentioned user

- **kadle.dateme**
Returns the percentage compatibility with Kadle himself

`musicbot.py`
==========
**Cog:** Music

Commands
--------------
- **kadle.join**  
Joins the voice channel the user is in

- **kadle.play**  
Plays the song searched for (searches either through Spotify or YouTube, default is YouTube). If no song is mentioned, it plays one randomly from a pre-defined list of URLs

- **kadle.volume**  
Adjusts the volume of the music being played 
(An integer between 0 to 100)

- **kadle.pause**  
Pauses audio

- **kadle.resume**  
Resumes audio

- **kadle.stop**  
Stops playing any audio

- **kadle.add**
Adds the searched song to the queue

- **kadle.leave**
Leaves the voice channel

- **kadle.queue**
Displays the queue

- **kadle.next**
Plays the next song in queue

- **kadle.setsearch**
Sets the search option as either Spotify or YouTube

`message_filter.py`
==========
**Cog:** Message

Runs a chat filter for certain _swear words_ and the word _wonderla_

`spawnbot.py`
==========
**Cog:** Spawn

This Cog is a basic implementation trying to mimic Pokecord. Check out Pokecord [here](https://www.pokecord.com/ "Pokecord").
Everytime a message is sent on a server a random number between 1 to 1000 is generated. If the number is greater than 920, it spawns a Kadle. Different images spawn with different probabilities as defined by the list `weights` under the function `spawn_image`

Commands
--------------
- **kadle.spawn**  
Sets the text channel for Kadle to spawn in (basically to avoid spam in one channel)

- **kadle.list**
Displays all the Kadles caught till now

- **kadle.select**
Selects a Kadle as your active companion for battles, levelling up, etc (to be introduced in future updates)

- **kadle.moves**
Lists all the moves of your selected Kadle

**Note**: `kadle.catch kadle` is used to catch a Kadle. However, this is not included as a command

`help.py`
==========
**Cog:** Help

This is the replacement for the default help command. It sends an elegantly formatted embed, which for some reason is lacking in the default help command. 
