import io
import traceback
import discord

from . import quote

client = discord.Client()


def send_exp(channel):
    s = io.StringIO()
    traceback.print_exc(file=s)
    print(s.getvalue())
    client.loop.create_task(client.send_message(channel, s.getvalue()))


@client.event
async def on_message(msg):
    if msg.author == client.user:
        return

    if not msg.content:
        return

    try:
        ret = await quote.run(client, msg)
        if ret:
            return

    except Exception:
        send_exp(msg.channel)




def run(key):
    client.run(key)
