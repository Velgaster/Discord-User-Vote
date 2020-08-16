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
        if any(x in msg.content.split() for x in self.client.SETTINGS.BLACKLIST):
            ctx = await self.client.get_context(msg)
            await self.event_log(ctx, msg, "A blacklisted phrase was used!")
            await msg.delete()

    async def event_log(self, ctx, msg, event):
        embed = discord.Embed()
        embed.colour = discord.Colour.red()
        embed.title = event
        embed.add_field(name='User', value=msg.author, inline=True)
        embed.add_field(name='Channel', value=msg.channel.name, inline=True)
        embed.add_field(name='Message', value=f"> {msg.content}", inline=False)
        await self.log_ch.send(embed=embed)
