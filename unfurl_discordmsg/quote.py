import re
import discord


def compose_embed(channel, msg):
    embed = discord.Embed(
        description=msg.content,
        timestamp=msg.timestamp)
    embed.set_author(
        name=msg.author.display_name,
        icon_url=msg.author.avatar_url)
    embed.set_footer(
        text=f'via {msg.channel.name}')
    return embed


DISCORD_URLS = re.compile(
    'https://discordapp.com/channels/'
    r'(?P<server>[\d]{18})/(?P<channel>[\d]{18})/(?P<msg>[\d]{18})'
)


async def run(client, msg):
    for m in DISCORD_URLS.finditer(msg.content):
        if msg.server.id == m.group('server'):
            channel = msg.server.get_channel(m.group('channel'))
            msg = await client.get_message(channel, m.group('msg'))

            embed = compose_embed(channel, msg)
            await client.send_message(msg.channel, embed=embed)
