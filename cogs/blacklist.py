from discord.ext import commands
from .scripts.settings import *
from .scripts.utils import event_log


def setup(client):
    client.add_cog(Voting(client))


class Voting(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.votes = {}


    @commands.Cog.listener()
    async def on_message(self, msg):
        if any(x in msg.content for x in BLACKLIST):
            ctx = await self.client.get_context(msg)
            await event_log(ctx, msg)
