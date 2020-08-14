from cogs.scripts import settings
from cogs.scripts.utils import admin
import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix=settings.COMMAND_PREFIX, description=settings.BOT_DESCRIPTION)


async def load(extension):
    await client.load_extension(f'cogs.{extension}')


async def unload(extension):
    await client.unload_extension(f'cogs.{extension}')


@client.command()
async def reload(ctx):
    await reload_all(ctx)


@admin
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
        client.load_extension(f'cogs.{filename[:-3]}')


@client.event
async def on_ready():
    print(f'Logged in as: {client.user.name}')
    print(f"Client ID: {client.user.id}")
    print('--------------------------')
    await client.change_presence(activity=discord.Game(name=settings.GAME_ACTIVITY_MESSAGE))

client.run(settings.TOKEN)

