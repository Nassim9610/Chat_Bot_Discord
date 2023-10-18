import discord
import json
from discord.ext import commands
import youtube_dl
import os


with open('data.json') as repuser:
    data = json.load(repuser)

default_intents = discord.Intents.default()
default_intents.members = True
client = discord.Client(intents=default_intents)


client = discord.Client()
#on commanec par choisr le preffixe
client = commands.Bot(command_prefix="!")
@client.event
async def on_ready():
    print("hello je suis le bot pour vous servir")

@client.event
async def on_message(message):
    message.content = message.content.lower()
    if message.author == client.user:
        return
    if message.content == "hello":
        await message.channel.send("Bonjour je vais vous aider car je suis Masterbot")
    if message.content == "relax":
        await message.channel.send("Je vous propose ceci : https://www.youtube.com/watch?v=qlXoh54zock")
    if message.content == "help":
        await message.channel.send("Bonjour le bot proposera une trés grnad large de choix de langages informatique avec des leçons ainsi que des vidéos vous permettrant de mieux les comprendre")
    if message.content == "del" :
        await message.channel.purge(limit=50)
    await client.process_commands(message)
@client.event
async def on_member_join(member):
    general_channel: discord.TextChannel = client.get_channel(978500515170222090)
    await general_channel.send(content=f"Welcome dans le meileur serveur {member.display_name} !")
#En cas d'erreur dans la commande
async def on_command_error(ctx,error):
    if isinstance(error,commands.CommandNotFound):
        await ctx.reply("Commande erroné")
    else :
        raise error
#Déconnexion
@client.command(name="exit")
async def exit(ctx):
    reponse="Ciao"
    await ctx.reply(reponse)
    await client.close()
    print(f"reponse à un message {ctx.message.id} : {reponse}")
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
    #on va stocker les questions et lz documentation dna sun fichier et séparer les videos et les tuto avec des listes
    class Node :
        def __init__(self, question, keyword, list_child_node) :    
            self.question = question
            self.keyword = keyword
            self.list_child_node = list_child_node
    
    def user_reponse(self):
        print(self.question)
        txt = input()
        for child in self.list_child_node : 
            if child .keyword in txt:
                child.user_response
    lesson_list = []
    cours_list= []

    #On initialise notre premiere branche la branche racine
    racine_node = Node(
        "Salutation, jeune HETICIENS, je vais te guider que souhaites-tu?\n je propose des lessons et des videos pour commencer tape '!list'", "start",
        [
     Node("Sur quel language tu as besoin d'un tuto?" , "tuto" , lesson_list),
     Node("Sur quel language tu as besoin d'une documentation?" ,"documentation" ,cours_list)
    ])
 

client.run("OTgxODcxMzA3Mjg3MzAyMjE0.GZqqnZ.E547KMBOHmS5CrJZ39UlkpI5DPz1GlTCKm4fYo")