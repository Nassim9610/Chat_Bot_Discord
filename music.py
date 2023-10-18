import discord
import json
from discord.ext import commands
import youtube_dl
import os

client = commands.Bot(command_prefix="!")
@client.command()
async def play(ctx, url : str):
     song_there = os.path.isfile("song.mp3")
     try:
        if song_there:
            os.remove("song.mp3")
     except PermissionError:
         await ctx.send("le son va se lancer use 'stop' command")
         return

     voicechannel =discord.utils.get(ctx.guild.voice_channels, name='General')
     await voicechannel.connect()
     voice =discord.utils.get(client.voice_clients, guild=ctx.guild)
     
     ydl_opts = {
         'format': 'bestaudio/best',
         'postprocessors': [{
             'key': 'FFmpegExtractAudio',
             'preferredcodec': 'mp3',
             'preferredquality': '192',
         }],
     }
     with youtube_dl.YoutubeDL(ydl_opts) as ydl:
         ydl.download([url])
     for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.rename(file, "song.mp3")
     voice.play(discord.FFmpegAudio("song.mp3"))

@client.command()
async def leave(ctx):
        voice =discord.utils.get(client.voice_clients, guild=ctx.guild)
        if not voice.is_connected():
            await voice.disconnected()
        else:
            await ctx.send("le bot n'est pas connecté")

@client.command()
async def pause(ctx):
     voice =discord.utils.get(client.voice_clients, guild=ctx.guild)
     if voice.is_playing():
         voice.pause()
     else:
         await ctx.send("le son n'est pas en pause")

@client.command()
async def stop(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.stop()

client.run("OTgxODcxMzA3Mjg3MzAyMjE0.GZqqnZ.E547KMBOHmS5CrJZ39UlkpI5DPz1GlTCKm4fYo")