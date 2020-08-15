from discord.ext import commands
from .scripts.utils import event_log
from time import time

from client import client as c


def setup(client):
    client.add_cog(Voting(client))
    client.add_cog(KeyWordFilter(client))


class Voting(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.votes = {}

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        if user != self.client.user:
            if reaction.emoji == c.SETTINGS.VOTE_EMOTE:
                if user.id not in self.votes.keys():
                    self.votes[user.id] = time()
                elif time() - self.votes[user.id] > c.SETTINGS.USER_VOTE_COOLDOWN_TIME_MINUTES * 60:
                    self.votes[user.id] = time()
                if reaction.count >= c.SETTINGS.VOTES_REQURED_FOR_DELETION:
                    ctx = await self.client.get_context(reaction.message)
                    await event_log(ctx, reaction.message)
                    await reaction.message.delete()


class KeyWordFilter(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, msg):
        if any(x in msg.content for x in c.SETTINGS.BLACKLIST):
            ctx = await self.client.get_context(msg)
            await event_log(ctx, msg)
