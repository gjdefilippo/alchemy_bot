""" commands.py """
"""""""""""""""""""""""""""
Contains strings for bot commands
"""
command_prefix = '/alchemy'  # string used to use bot commands
command_string = r'^(\/alchemy) (\S+) ?(\S+)?'  # regex pattern that the bot recognizes as commands
gather = 'gather_ingredients'  # command to gather ingredients
list_command = 'list'  # command to list stuff
l_commands = 'commands'  # argument for list command that lists all valid commands
alt_l_commands = 'help'  # alternate command to list all valid commands
l_terrains = 'terrains'  # argument for list command that lists all valid terrains
l_ingredients = 'ingredients'  # argument for list command that lists all ingredients
"""""""""""""""""""""""""""
LISTS
"""
command_list = [ # list of all valid bot commands
    'gather_ingredients *[terrain]*  ::  Search for ingredients in specified terrain',
    'list (commands | terrains | ingredients)'
]
valid_terrains = [  # for error checking in gather_ingredients
    'arctic',
    'coastal',
    'underwater',
    'desert',
    'forest_day',
    'forest_night',
    'grasslands',
    'hills',
    'mountain',
    'mountains',
    'cave',
    'swamp',
    'rainy_swamp',
    'underdark'
]
terrains_list = [  # for the listing terrains command
    'arctic',
    'coastal',
    'underwater',
    'desert',
    'forest_day',
    'forest_night   *(Has special rules different from "forest_day")*',
    'grasslands',
    'hills',
    'mountain   *(Same as "mountains")*',
    'mountains   *(Same as "mountain")*',
    'cave   *(Has special rules different from "mountain(s)")*',
    'swamp',
    'rainy_swamp   *(Has special rules different from "swamp")*',
    'underdark'
]


