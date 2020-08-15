from cogs.scripts.settings import SETTINGS
import discord
from discord.ext import commands
import os


client = commands.Bot(command_prefix=SETTINGS.PREFIX, description=SETTINGS.DESCRIPTION)
client.SETTINGS = SETTINGS


async def load(extension):
    await client.load_extension(f'cogs.{extension}')


async def unload(extension):
    await client.unload_extension(f'cogs.{extension}')


@client.command()
@commands.has_any_role(*SETTINGS.BOT_ADMINS)
async def reload(ctx):
    await reload_all(ctx)


async def reload_all(ctx):
    """reload all extensions. Admin command."""
    for name in os.listdir('./cogs'):
        if name.endswith('.py'):
            print('reloading ' + name)
            try:
                client.unload_extension(f'cogs.{name[:-3]}')
            except Exception as e:
                print(e)
            try:
                client.load_extension(f'cogs.{name[:-3]}')
            except Exception as e:
                print(e)
            print('ok')


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        print(filename[:-3])
        client.load_extension(f'cogs.{filename[:-3]}')


#@client.event
#async def on_command_error(ctx, error):
#    await ctx.send(error)


@client.event
async def on_ready():
    print(f'Logged in as: {client.user.name}')
    print(f"Client ID: {client.user.id}")
    print('--------------------------')
    await client.change_presence(activity=discord.Game(name=SETTINGS.ACTIVITY_MESSAGE))

from YOUR_LOCAL_FILES import YOUR_BOT_TOKEN
client.run(YOUR_BOT_TOKEN)

