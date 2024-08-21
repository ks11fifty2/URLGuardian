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
    
    await client.process_commands(message)

@client.command()
async def hello(ctx):
    await ctx.send("Hello! I am URLGuardian.\nI scan links being sent in the Discord chat and exile malicious ones :D")

@client.command()
@commands.has_role("Admin")
async def clear(ctx):
    async for message in ctx.channel.history(limit=1000):
        if message.author == client.user:
            try:
                await message.delete()
            except discord.Forbidden:
                await ctx.send("I don't have permission to delete messages!")
            except discord.HTTPException as e:
                await ctx.send(f"Failed to delete message: {e}")

@client.command()
@commands.has_role("Admin")
async def shutdown(ctx):
    if ctx.author.guild_permissions.administrator:
        print("Shutting down!")
        await ctx.send("Shutting down the bot.")
        await client.close()
    else:
        await ctx.send("You do not have permission to shut down the bot.")

@client.command()
async def info(ctx):
    await ctx.send("**URLGuardian Commands:**\n\n**!hello:** This command makes the bot introduce itself and explain that it’s here to protect the server by scanning links.\n\n**Admin Commands:**\n\n**!clear:** This command deletes the bot's own messages from the chat, useful for cleaning up.\n**!shutdown:** This command turns the bot off, but only server admins can use this command to prevent unauthorized shutdowns.")


client.run(TOKEN)