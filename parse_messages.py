from discord.utils import find
from re import match
from ingredients_finder.commands.gather_ingredients import gather_ingredients
from ingredients_finder.commands.list import list_the
from data.commands import *
from data.errors import invalid_role, invalid_command
from data.bot_config import alch_role_name


async def parse_message(message, channel):
    content = message.content.lower()
    matches = match(command_string, content)
    if not matches:
        return

    # bois need Alchemy Master role to give commands
    guild_roles = message.guild.roles
    alch_role = find(lambda role: role.name.lower() == alch_role_name, guild_roles)
    if alch_role not in message.author.roles:
        return await channel.send(invalid_role)

    command = matches.group(2)
    arg1 = matches.group(3)

    embeds = []
    # rolling for ingredients
    if command == gather and arg1:
        response, embeds = gather_ingredients(arg1)
    # listing things
    elif command == list_command:
        response = list_the(arg1)
    # 'help' == alternate way to list commands
    elif command == alt_l_commands:
        response = list_the(l_commands)
    else:
        response = invalid_command

    await channel.send(response)
    for embed in embeds:
        await channel.send(embed=embed)
    return

