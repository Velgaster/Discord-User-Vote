from discord.ext import commands
from .scripts.utils import check_permission


def setup(client):
    client.add_cog(Admin(client))


class Admin(commands.Cog):
    def __init__(self, client):
        self.client = client

    @check_permission
    @commands.command()
    async def set(self, ctx, *args):
        raise NotImplementedError
