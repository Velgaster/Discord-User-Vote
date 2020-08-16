from discord.ext import commands
import discord


def setup(client):
    client.add_cog(KeyWordFilter(client))


class KeyWordFilter(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.log_ch = self.client.get_channel(int(self.client.SETTINGS.LOG_CHANNEL))


    @commands.Cog.listener()
    async def on_message(self, msg):
        if any(x in msg.content for x in self.client.SETTINGS.BLACKLIST):
            ctx = await self.client.get_context(msg)
            await self.event_log(ctx, msg, "a blacklisted phrase was used!")
            await msg.delete()

    async def event_log(self, ctx, msg, event):
        embed = discord.Embed()
        embed.colour = discord.Colour.red()
        embed.title = event
        embed.description = f'> `{msg}`'
        for setting, value in zip(ctx.__dict__, ctx.__dict__.values()):
            embed.add_field(name=setting, value=value, inline=True)
        await self.log_ch.send(embed=embed)
