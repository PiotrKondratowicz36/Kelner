from Ingredients import Ingredients
from Meal import Meal
import json

"""
      Klasa uzywana do reprezetancji Menu, dziedziczaca z listy.

      Atrybuty
      --------------

      Metody
      --------------
      create_menu()
            tworzy nowy obiekt menu dodajac do niego wszystkie posilki z pliku
            posilki.json
"""


class Menu(list):
    pass


def create_menu():
    new_menu = Menu()
    f = open('posilki.json')
    json_meals = json.load(f)
    meals = json_meals["meals"]
    for x in range(len(meals)):
        listOfIngredients = list()
        for y in range(len(meals[x]["ingredientsList"])):
            listOfIngredients.append(Ingredients(meals[x]["ingredientsList"][y]["name"],
                                                 meals[x]["ingredientsList"][y]["origin"],
                                                 meals[x]["ingredientsList"][y]["hasGluten"]))
        new_menu.append(Meal(meals[x]["name"],
                             meals[x]["prepareTime"],
                             listOfIngredients))
        print(listOfIngredients[0].hasGluten)
    f.close()
    return new_menu


menu = create_menu()