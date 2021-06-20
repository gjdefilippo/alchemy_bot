""" errors.py """
"""""""""""""""""""""""""""
Contains strings for errors involving user-typed commands
"""
invalid_role = 'Only bois with the **"Alchemy Master"** role can tell me what to do.' # user doesnt have correct role
invalid_command = "I don't recognize that command! You can view the list of valid commands by typing **\"/alchemy " \
                  "list commands\"** "  # bot doesn't recognize command
invalid_terrain = "I don't recognize that terrain! You can view the list of valid terrains by typing " \
                  "**\"/alchemy list terrains\"**"  # invalid terrain given for gather_ingredients
invalid_list = "I'm not sure what you're asking me to list here... Type **\"/alchemy list commands\"** to see all " \
                "the things I can list!"  # invalid list parameter given
