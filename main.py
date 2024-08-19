#Local Imports
import url_extractor
import url_scanner
from apikeys import *

#Libs
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix = '!',intents=intents)

@client.event
async def on_ready():
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("URLGuardian Running!")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if "http://" in message.content or "https://" in message.content:
        url = url_extractor.extract_url(message.content)
        if url_scanner.scan_url(url) > 3:
            await message.delete()
            await message.channel.send(f"{message.author.mention}, your message was deleted because it contained a suspicious URL.")
            print(f"Malicious URL\nDeleting Message by User: {message.author.mention}")
            print("----------------------------------------------------------------------------------------")
        else:
            print("Safe URL")
            print("----------------------------------------------------------------------------------------")

@client.command()
async def hello(ctx):
    await ctx.send("Hello! I am URLGuardian.\nI scan links being sent in the Discord chat and exile malicious ones :D")

client.run(TOKEN)