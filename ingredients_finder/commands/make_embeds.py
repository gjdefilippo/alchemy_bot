from discord.embeds import Embed
from ingredients_finder.data.read_ingredients_data import ingredients_table


def make_ingredient_embeds(ingredients):
    ingredient_embeddings = []
    for ingredient in ingredients:
        ingredient_info = ingredients_table[ingredient]
        name = ingredient
        _type = ingredient_info['type']
        rarity = ingredient_info['rarity']
        dc = ingredient_info['dc']
        terrain = ingredient_info['terrain']
        effects = ingredient_info['effects']
        description = ingredient_info['description']
        url = ingredient_info['pic_url']

        embed = Embed(title=('**' + name + ' x' + str(ingredients[ingredient]) + '**'))
        embed.set_image(url=url)
        embed.add_field(name='Type:', value=_type, inline=False)
        embed.add_field(name='Rarity:', value=rarity, inline=False)
        embed.add_field(name='Alchemy Modifier:', value=dc, inline=False)
        embed.add_field(name='Found in:', value=terrain, inline=False)
        embed.add_field(name='(Effects)', value=effects, inline=False)
        embed.add_field(name='Description:', value=description, inline=False)

        ingredient_embeddings.append(embed)

    return ingredient_embeddings
