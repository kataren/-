import discord
import os


client = commands.Bot(command_prefix='>')


@client.event
async def on_ready():

    print("login")
    print(client.user.name)
    print(client.user.id)
    print("~~~~~~~~~~~~~~~~~")


@client.event
async def on_message(message):
    if message.content.startswith('>안녕'):
        await message.channel.send("안녕하세요?")


bot.run(os.environ['TOKEN'])
