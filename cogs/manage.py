from discord.ext import commands
from .scripts.utils import apply
from .scripts.settings import Settings
import os


def setup(client):
    client.add_cog(Manage(client))


class Manage(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.is_owner()
    async def reset(self, ctx):
        rst = Settings()
        self.client.SETTINGS = rst
        self.client.SETTINGS.SERVER_OWNER = str(ctx.guild.owner)
        await self.client.SETTINGS.save(ctx)

    @commands.command()
    @commands.is_owner()
    async def settings(self, ctx):
        await self.try_del()
        self.setting_msg = await ctx.send(embed=self.client.SETTINGS.embed())

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def set(self, ctx, key, *args):
        await apply(self.manager, ctx, 'set', f'key={key}', *args)

    @commands.command(aliases=['gl'])
    @commands.has_permissions(administrator=True)
    async def graylist(self, ctx, mode, *args):
        await apply(self.manager, ctx, mode, 'key=GRAYLIST', *args)

    @commands.command(aliases=['bl'])
    @commands.has_permissions(administrator=True)
    async def blacklist(self, ctx, mode, *args):
        await apply(self.manager, ctx, mode, 'key=BLACKLIST', *args)

    async def manager(self, ctx, mode, *value, key):
        key = key.upper()

        operation = {
            'set': lambda x, y: self.client.SETTINGS.set(x, list(y) if len(y) > 1 else y[0]),
            'add': lambda x, y: list.extend(self.client.SETTINGS.__getattribute__(x), list(y)),
            'remove': lambda x, y: [list.remove(self.client.SETTINGS.__getattribute__(x), i) for i in y]
        }

        operation[mode](key, value)
        await self.try_del()
        self.setting_msg = await self.client.SETTINGS.save(ctx)

    @commands.command(aliases=['rl'])
    @commands.has_permissions(administrator=True)
    async def reload(self, ctx):
        await self.reload_all(ctx)

    async def load(self, extension):
        await self.client.load_extension(f'cogs.{extension}')

    async def unload(self, extension):
        await self.client.unload_extension(f'cogs.{extension}')

    async def reload_all(self, ctx):
        """reload all extensions. Admin command."""
        for name in os.listdir('./cogs'):
            if name.endswith('.py'):
                print('reloading ' + name, end='...')
                try:
                    self.client.unload_extension(f'cogs.{name[:-3]}')
                except Exception as e:
                    print(e)
                try:
                    self.client.load_extension(f'cogs.{name[:-3]}')
                except Exception as e:
                    print(e)
                print('ok')

    async def try_del(self):
        if hasattr(self, "setting_msg"):
            await self.setting_msg.delete()

