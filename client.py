from cogs.scripts.settings import SETTINGS
import discord
from discord.ext import commands
import os


client = commands.Bot(command_prefix=SETTINGS.PREFIX, description=SETTINGS.DESCRIPTION)
client.SETTINGS = SETTINGS

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


@client.event
async def on_command_error(ctx, error):
    await ctx.send(error)


@client.event
async def on_ready():
    print(f'Logged in as: {client.user.name}')
    print(f"Client ID: {client.user.id}")
    print('--------------------------')
    await client.change_presence(activity=discord.Game(name=SETTINGS.ACTIVITY))

from YOUR_LOCAL_FILES import YOUR_BOT_TOKEN
for i, j in zip(SETTINGS.__dict__, SETTINGS.__dict__.values()):
    print(f"{i} : {j}")
client.run(YOUR_BOT_TOKEN)

