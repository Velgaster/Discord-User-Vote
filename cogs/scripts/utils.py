from discord.ext.commands import Bot
from .settings import *


async def apply(func, ctx, *args):
    await func(ctx, *parse(args)[0], **parse(args)[1])


def parse(args):
    kwarg_list = [arg for arg in args if "=" in arg]
    kwargs = dict(i.split('=') for i in kwarg_list)
    args = tuple([arg for arg in args if "=" not in arg])
    return args, kwargs


async def event_log(ctx, msg):
    raise NotImplementedError

# ------------------------------------------------------------------------------------
# Decorators
# ## use a @decorator before a function definition to apply it's effect
# ------------------------------------------------------------------------------------
#
# Permission check decorators:
# @owner -> only owner can execute the function
# @admin -> admin and owner can execute the function
# ------------------------------------------------------------------------------------


def owner(func):
    async def wrapper(*args):
        if args[0].message.author.id == OWNER_ID:
            await func(*args)
        else:
            await args[0].send("You don't have permission to use this command.")
    return wrapper


def admin(func):
    async def wrapper(*args):
        if args[0].message.author.id in [OWNER_ID, *ADMIN_ROLE_IDS]:
            await func(*args)
        else:
            await args[0].send("You don't have permission to use this command.")
    return wrapper


# utils decorators:
# @feedback_on_error -> will post the error message in chat
# ------------------------------------------------------------------------------------


def feedback_on_error(func):
    async def wrapper(*args):
        try:
            await func(*args)
        except Exception as e:
            await args[0].send(e)
    return wrapper
