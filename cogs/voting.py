from discord.ext import commands
from .scripts.settings import *
from .scripts.utils import event_log
from time import time

def setup(client):
    client.add_cog(Voting(client))


class Voting(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.votes = {}

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        if user != self.client.user:
            if reaction.emoji == VOTE_EMOTE:
                if user.id not in self.votes.keys():
                    self.votes[user.id] = time()
                elif time() - self.votes[user.id] > USER_VOTE_COOLDOWN_TIME_MINUTES * 60:
                    self.votes[user.id] = time()
                if reaction.count >= VOTES_REQURED_FOR_DELETION:
                    ctx = await self.client.get_context(reaction.message)
                    await event_log(ctx, reaction.message)
                    await reaction.message.delete()