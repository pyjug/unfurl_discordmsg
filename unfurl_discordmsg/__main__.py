import os
from . import bot

if __name__ == '__main__':
    key = open(os.environ['DISCORD_BOT_KEYFILE']).read().strip()
    bot.run(key)
