import pickle
# ------------------------------------------------------------------------------------
# utils -> helper functions
# ------------------------------------------------------------------------------------


def pickle_object(path, obj):
    with open(path, 'wb') as handle:
        pickle.dump(obj, handle, protocol=pickle.HIGHEST_PROTOCOL)


def open_pickled_object(path):
    with open(path, 'rb') as handle:
        return pickle.load(handle)


async def apply(func, ctx, *args):
    await func(ctx, *parse(args)[0], **parse(args)[1])


def parse(args):
    kwarg_list = [arg for arg in args if "=" in arg]
    kwargs = dict(i.split("=") for i in kwarg_list)
    args = tuple([arg for arg in args if "=" not in arg])
    return args, kwargs
