from discord.ext import commands
from .scripts.utils import admin, owner


def setup(client):
    client.add_cog(Admin(client))


class Admin(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @owner
    async def change_bot_owner(self, ctx, *args):
        raise NotImplementedError

    @commands.command()
    @owner
    async def role(self, ctx, *args):
        raise NotImplementedError

    @commands.command()
    @admin
    async def set(self, ctx, *args):
        raise NotImplementedError
