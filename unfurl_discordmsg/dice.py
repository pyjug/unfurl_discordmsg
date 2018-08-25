import random
import re
import discord


usage = '''%dice 1d6 <- ダイスを1つ振る
%dice 2d8+5 <- 8面ダイスを2つ振り、結果に5を足す
'''

async def error(client, msg):
    embed = discord.Embed(title='使い方:', 
        description=usage)
    await client.send_message(msg.channel, embed=embed)
    return

async def run(client, msg):
    src = msg.content.strip()
    m = re.match("^%dice\s+(?P<num>\d+)d(?P<max>\d+)(\+(?P<base>\d+))?$", src)

    if not m:
        await error(client, msg)
        return

    d = m.groupdict()
    num = int(d['num'])
    maxval = int(d['max'])
    base = d.get('base', None)

    if not num or not maxval:
        await error(client, msg)
        return

    values = [random.randrange(maxval) + 1 for i in range(num)]
    if base:
        values.append(int(base))


    result = f'{sum(values)} <- {values}' 

    embed = discord.Embed(title=src, 
        description=str(result))
    await client.send_message(msg.channel, embed=embed)
    return True
