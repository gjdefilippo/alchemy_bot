from d20 import roll

import ingredients_finder.commands.make_embeds
from data.commands import valid_terrains
from data.errors import invalid_terrain
from ingredients_finder.data.read_ingredients_data import *
from ingredients_finder.commands.make_embeds import make_ingredient_embeds
import random

""" gather_ingredients.py """
"""""""""""""""""""""""""""
Rolls 1d4 dice to determine how many ingredients are found by the player.
Then rolls 2d6 per each ingredient found to determine type
of ingredients are found according to the terrain the player is in.
"""


# deals with additional rules that affect ingredient count
def count_multiplier(ingredient):
    rules = ingredient['rules']
    # Find 2x the rolled amount
    if rules == '2x':
        return 2
    # Find 1-2x the rolled amount
    elif rules == '1-2x':
        return random.randint(1, 2)
    else:
        return 1


# creates the pretty message for the discord
def make_ingredients_message(ingredients):
    ingredients_dict = {}  # ingredients list dictionary with counts
    num_ingredients = 0  # total number of ingredients found

    # populates the ingredients dictionary with counts
    for ingredient in ingredients:
        name = ingredient['name']
        count = 1 * count_multiplier(ingredient)
        num_ingredients += count
        if name in ingredients_dict:
            ingredients_dict[name] += count
        else:
            ingredients_dict[name] = count

    # gets full info from ingredients json and makes message
    if num_ingredients > 1:
        ingredients_found_message = '**You found ' + str(num_ingredients) + ' ingredients!**\n'
    else:
        ingredients_found_message = '**You found ' + str(num_ingredients) + ' ingredient!**\n'
    embeds = make_ingredient_embeds(ingredients_dict)

    return ingredients_found_message, embeds


# roll on the common table
def roll_common():
    common_roll = roll("2d6").total

    # bloodgrass rerolled if not tracking provisions
    if common_roll == 7 and rules_table["track_provisions"] == "False":
        return roll_common()
    else:
        return common_ingredients[str(common_roll)]


# roll a single ingredient
def roll_ingredient(terrain):
    dice_roll = roll("2d6").total
    common_range = range(6, 9)  # dice roll range for the common ingredients table
    elem_water_range = [2, 3, 4, 10, 11, 12]  # dice roll range for elemental water chance

    # roll common
    if dice_roll in common_range:
        print('Rolling on common table')
        ingredient = roll_common()
    # roll normal
    else:
        ingredient = terrain[str(dice_roll)]

    # ingredient replaced with elemental water
    if dice_roll in elem_water_range and roll("d100").total >= 75:
        print(ingredient['name'] + ' replaced with Elemental Water!')
        ingredient = terrains_table['elemental_water']

    return ingredient


# gather multiple ingredients
def gather_ingredients(terrain):

    if terrain not in valid_terrains:
        return invalid_terrain
    terrain_ecosystem = terrains_table[terrain]
    print('Gathering ingredients in terrain: ' + terrain)

    # ingredient array of dictionaries is returned
    ingredients = []
    num_ingredients = roll("1d4").total  # number of ingredients found by player
    print('Number of ingredients rolled: ' + str(num_ingredients))
    for i in range(num_ingredients):
        print('\nRolling ingredient ' + str(i + 1) + '')
        # this while loop is for the forest_day "Wisp Stalks" edge case
        while True:
            ingredient = roll_ingredient(terrain_ecosystem)
            if ingredient['name'] != 'Reroll':
                break
        print('Rolled: ' + ingredient['name'])

        # add ingredient to dict
        ingredients.append(ingredient)

        # desert voidroot comes with 1 elemental water
        if ingredient['name'] == 'Voidroot' and terrain == 'desert':
            ingredients.append(terrains_table['elemental_water'])
    print('------------------------------------------------------')
    return make_ingredients_message(ingredients)

