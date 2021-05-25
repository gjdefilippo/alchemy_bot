from re import match
from ingredients_finder.commands.gather_ingredients import gather_ingredients
from data.commands import command_string, gather


async def parse_message(message, channel):
    content = message.content.lower()
    matches = match(command_string, content)
    if not matches:
        return

    command = matches.group(2)
    arg1 = matches.group(3)

    # rolling for ingredients
    if command == gather and arg1:
        ingredients = gather_ingredients(arg1)
        await channel.send(ingredients)
    return

