# This concept will be more generalized for multi-server use in the future

# General
BOT_DESCRIPTION = "A simple helper to keep the chats friendly"
GAME_ACTIVITY_MESSAGE = "keep the chat friendly"
TOKEN = ""
OWNER_ID = None  # only this user can add or remove ADMIN_ROLE_ID's using bot commands
ADMIN_ROLE_IDS = []  # any role that need permission to change bot settings
EVENT_LOG_CHANNEL_ID = None  # To makes sense of it, set it to an isolated Admin-only channel
COMMAND_PREFIX = ","

# Vote Settings
DAILY_USER_VOTE_LIMIT = 24
USER_VOTE_COOLDOWN_TIME_MINUTES = 3
VOTE_EMOTE = '❌'
VOTES_REQURED_FOR_DELETION = 5

# Add forbidden words here
BLACKLIST = []
