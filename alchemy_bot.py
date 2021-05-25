import discord
import json
from parse_messages import parse_message

try:
    with open('data/bot_config.json', encoding="utf-8") as file:
        config = json.load(file)
except FileNotFoundError:
    print("Data file not found")

client = discord.Client()


@client.event
async def on_ready():
    channel = client.get_channel(config['deus_vult'])
    # await channel.send('I, {}, have arrived'.format(client.user.name))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    channel = message.channel
    await parse_message(message, channel)


client.run(config['api_key'])
