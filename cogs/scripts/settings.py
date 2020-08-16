from .utils import pickle_object, open_pickled_object
import discord

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! #
# ---------------------------------------- WARNING ------------------------------------------- #
# ---------- if you change default values here, make sure to use the same datatype ----------- #
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! #


class Settings:
    def __init__(self):
        self.DESCRIPTION = "A simple helper to keep the chats friendly"
        self.ACTIVITY = "keep the chat friendly"
        self.LOG_CHANNEL = 0  # To makes sense of it, set it to an isolated Admin-only channel.
        self.PREFIX = ","

        # vote Settings
        self.DAILY_VOTE_LIMIT = 24
        self.VOTE_COOLDOWN_MINUTES = 3
        self.VOTE_EMOTE = '❌'
        self.VOTES_UNTIL_DELETION = 5

        # unwanted phrases
        self.BLACKLIST = []
        self.GRAYLIST = []

    def set(self, key, value):
        print(key, value)
        obj = self.__getattribute__(key)
        try:
            self.__setattr__(key, type(obj)(value))  # breaks if vars not __init__() /w their required type!!!!!!
        except TypeError as e:
            print(e)
            raise

    def embed(self):
        embed = discord.Embed()
        embed.colour = discord.Colour.blue()
        embed.title = "Current Bot Settings"
        for setting, value in zip(self.__dict__, self.__dict__.values()):
            embed.add_field(name=setting, value=value, inline=True)
        return embed

    async def save(self, ctx):
        pickle_object(SETTINGS_FILE, self)
        return await ctx.send("Setting Updated.", embed=self.embed())


SETTINGS_FILE = 'settings.data'

try:
    SETTINGS = open_pickled_object(SETTINGS_FILE)

except FileNotFoundError:

    SETTINGS = Settings()
    pickle_object(SETTINGS_FILE, SETTINGS)
