import discord
from data.bot_config import api_key
from parse_messages import parse_message

client = discord.Client()


@client.event
async def on_ready():
    #channel = client.get_channel(852723675098120192)
    #await channel.send('Who is this dude')
    return


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    return await parse_message(message, message.channel)


client.run(api_key)
