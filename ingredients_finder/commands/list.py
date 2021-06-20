from data.commands import *
from data.errors import invalid_list
from ingredients_finder.data.read_ingredients_data import ingredients_table


def list_the(what):
    the_list = '\n'
    if what == l_commands:
        the_list += 'Here\'s a list of commands I can do!\n\n'
        for command in command_list:
            the_list += '❥ ' + command_prefix + ' ' + command + '\n'
    elif what == l_terrains:
        the_list += 'Here\'s a list of all the terrains!\n\n'
        for terrain in terrains_list:
            the_list += '❥ ' + terrain + '\n'
    elif what == l_ingredients:
        the_list += 'Here\'s a list of all the ingredients!\n\n'
        for ingredient in ingredients_table:
            the_list += '❥ ' + ingredient + '\n'
    else:
        the_list = invalid_list
    return the_list
