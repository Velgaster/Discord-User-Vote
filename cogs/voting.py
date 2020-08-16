from discord.ext import commands
from time import time
import discord


def setup(client):
    client.add_cog(Voting(client))


class Voting(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.votes = {}
        self.log_ch = self.client.get_channel(self.client.SETTINGS.LOG_CHANNEL)

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        if user != self.client.user:
            if reaction.emoji == self.client.SETTINGS.VOTE_EMOTE:
                if user.id not in self.votes.keys():
                    self.votes[user.id] = time()
                elif time() - self.votes[user.id] > self.client.SETTINGS.USER_VOTE_COOLDOWN_TIME_MINUTES * 60:
                    self.votes[user.id] = time()
                if reaction.count >= self.client.SETTINGS.VOTES_REQURED_FOR_DELETION:
                    ctx = await self.client.get_context(reaction.message)
                    await self.event_log(ctx, reaction.message, "a post was outvoted.")
                    await reaction.message.delete()

    async def event_log(self, ctx, msg, event):
        embed = discord.Embed()
        embed.colour = discord.Colour.red()
        embed.title = event
        embed.description = f'{msg.author} said:\n> `{msg.content}`'
        for setting, value in zip(ctx.__dict__, ctx.__dict__.values()):
            embed.add_field(name=setting, value=value, inline=True)
        self.log_ch.send(embed=embed)
