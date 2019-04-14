import discord
from discord.ext import commands

client = commands.Bot(command_prefix='>')


@client.event
async def on_ready():

    print("login")
    print(client.user.name)
    print(client.user.id)
    print("~~~~~~~~~~~~~~~~~")


@client.event
async def on_message(message):
    if message.content.startswith('!안녕'):
        await message.channel.send("안녕하세요?")


client.run('NTY2OTU0MzYyMjIwMzE0NjY1.XLMfnA.P1mz4ciraD1QqvL7Oe1lsvSdu0U')
