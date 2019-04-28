import re
import io
import traceback
import discord

from . import quote, dice

client = discord.Client()


async def send_exp(channel):
    s = traceback.format_exc()
    print(s)
    await channel.send(s)


@client.event
async def on_message(msg):
    if msg.author == client.user:
        return

    if not msg.content:
        return

    try:
        if msg.content.startswith('%dice'):
            ret = await dice.run(client, msg)
            if ret:
                return

        ret = await quote.run(client, msg)
        if ret:
            return

    except Exception:
        await send_exp(msg.channel)




def run(key):
    client.run(key)
