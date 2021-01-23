import discord
from config import *

client = discord.Client()


async def parse_message(message):
    channel = message.channel


@client.event
async def on_ready():
    channel = client.get_channel(deus_vult)
    # await channel1.send('I, {}, have arrived'.format(client.user.name))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    return await parse_message(message)


client.run(api_key)
