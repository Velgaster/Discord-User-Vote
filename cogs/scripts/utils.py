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


# --------------------------------------------------------------
# Decorator


def check_permission(func):
    async def wrapper(*args):
        if args[0].message.author.id in [OWNER_ID, *ADMIN_IDS]:
            await func(*args)
        else:
            await args[0].send("You don't have permission to use this command.")
    return wrapper
