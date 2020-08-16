from discord.ext import commands
from .scripts.utils import apply
from .scripts.settings import Settings
import os
import discord


def setup(client):
    client.add_cog(Manage(client))


class Manage(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.setting_msg = None

    @commands.command()
    @commands.is_owner()
    async def reset(self, ctx):
        rst = Settings()
        self.client.SETTINGS = rst
        await self.client.SETTINGS.save(ctx)
        await self.update()

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
            'add': lambda x, y: list.extend(self.client.SETTINGS.__getattribute__(x),
                                            [*map(lambda z: z.replace("-", ' '), list(y))]),
            'remove': lambda x, y: [list.remove(self.client.SETTINGS.__getattribute__(x), i) for i in y]
        }

        operation[mode](key, value)
        await self.try_del()
        self.setting_msg = await self.client.SETTINGS.save(ctx)
        await self.update()

    @commands.command(aliases=['rl'])
    @commands.has_permissions(administrator=True)
    async def reload(self, ctx):
        await self.reload_all()
        await self.update()

    async def load(self, extension):
        await self.client.load_extension(f'cogs.{extension}')

    async def unload(self, extension):
        await self.client.unload_extension(f'cogs.{extension}')

    async def reload_all(self):
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
        try:
            await self.setting_msg.delete()
        except Exception as e:
            print(e)

    async def update(self):
        await self.client.change_presence(activity=discord.Game(name=self.client.SETTINGS.ACTIVITY))
        self.client.description = self.client.SETTINGS.DESCRIPTION
        await self.reload_all()

