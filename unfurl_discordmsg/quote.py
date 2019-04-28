import re
import discord


def compose_embed(channel, msg):
    embed = discord.Embed(
        description=msg.content,
        timestamp=msg.created_at)
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
        if msg.guild.id == int(m.group('server')):
            channel = client.get_channel(int(m.group('channel')))
            if not channel:
                continue
            orgmsg = await channel.fetch_message(int(m.group('msg')))
            if not orgmsg:
                continue

            embed = compose_embed(channel, orgmsg)
            await msg.channel.send(embed=embed)
