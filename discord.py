import discord
import os
import opus
OPUS_LIBS = ['libopus-0.x86.dll', 'libopus-0.x64.dll', 'libopus-0.dll', 'libopus.so.0', 'libopus.0.dylib']

def load_opus_lib(opus_libs=OPUS_LIBS):
    if opus.is_loaded():
        return True
    for opus_lib in opus_libs:
            try:
                opus.load_opus(opus_lib)
                return
            except OSError:
                pass

    raise RuntimeError('Could not load an opus lib. Tried %s' % (', '.join(opus_libs)))

load_opus_lib()

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
