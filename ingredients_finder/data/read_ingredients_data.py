import json

ingredients_data = "./ingredients_finder/data/ingredients.json"
rules_data = "./ingredients_finder/data/rules.json"
terrains_data = "./ingredients_finder/data/terrains.json"

try:
    with open(ingredients_data, encoding="utf-8") as file:
        ingredients_table = json.load(file)
    with open(rules_data, encoding="utf-8") as file:
        rules_table = json.load(file)
    with open(terrains_data, encoding="utf-8") as file:
        terrains_table = json.load(file)
        common_ingredients = terrains_table["common"]
except FileNotFoundError:
    print('Data file ' + file.name + ' not found')