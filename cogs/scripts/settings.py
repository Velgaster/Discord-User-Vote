# This concept will be more generalized for multi-server use in the future
from .utils import pickle_object, open_pickled_object
import discord


class Settings:
    def __init__(self):
        self.DESCRIPTION = "A simple helper to keep the chats friendly"
        self.ACTIVITY_MESSAGE = "keep the chat friendly"
        self.BOT_OWNER = None  # only this user can add or remove ADMINs using bot commands
        self.BOT_ADMINS = []  # any role that need permission to change bot settings
        self.LOG_CHANNEL = None  # To makes sense of it, set it to an isolated Admin-only channel
        self.PREFIX = ","

        # Vote Settings
        self.DAILY_VOTE_LIMIT = 24
        self.VOTE_COOLDOWN_MINUTES = 3
        self.VOTE_EMOTE = '❌'
        self.VOTES_UNTIL_DELETION = 5

        # Add forbidden words here
        self.BLACKLIST = []
        self.GRAYLIST = []

    def embed(self):
        embed = discord.Embed()
        embed.colour = discord.Colour.blue()
        embed.title = "Current Bot Settings"
        for setting, value in zip(self.__dict__, self.__dict__.values()):
            embed.add_field(name=setting, value=value, inline=True)
        return embed

    async def save(self, ctx):
        pickle_object(SETTINGS_FILE, self)
        await ctx.send("Setting Updated.")

    async def reset(self, ctx):
        tmp = Settings()
        self = tmp
        pickle_object(SETTINGS_FILE, self)
        await ctx.send("settings successfully reset.")


SETTINGS_FILE = 'settings.data'

try:
    SETTINGS = open_pickled_object(SETTINGS_FILE)

except FileNotFoundError:

    SETTINGS = Settings()
    pickle_object(SETTINGS_FILE, SETTINGS)
