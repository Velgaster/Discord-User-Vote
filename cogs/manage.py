from discord.ext import commands
from .scripts.utils import apply

from client import client as c


def setup(client):
    client.add_cog(Manage(client))


class Manage(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.is_owner()
    async def change_bot_owner(self, ctx, *args):
        raise NotImplementedError

    @commands.command()
    @commands.is_owner()
    async def reset(self, ctx):
        await c.SETTINGS.reset(ctx)

    @commands.command()
    @commands.is_owner()
    async def settings(self, ctx):
        await ctx.send(embed=c.SETTINGS.embed())

    @commands.command()
    @commands.is_owner()
    async def admin(self, ctx, *args):
        await apply(self.admin_manager, ctx, *args)

    async def admin_manager(self, ctx, cmd, ID):
        if cmd == "add":
            c.SETTINGS.BOT_ADMINS.append(ID)
            await c.SETTINGS.save(ctx)
            await ctx.send(f"role {ID} has now permission to manage bot settings.")
        if cmd == "remove":
            c.SETTINGS.BOT_ADMINS.remove(ID)
            await c.SETTINGS.save(ctx)
            await ctx.send(f"role {ID} has no longer permission to manage bot settings.")

    @commands.command()
    @commands.has_any_role(*c.SETTINGS.BOT_ADMINS)
    async def manage(self, ctx, *args):
        raise NotImplementedError
