

class Meal:

    """
       Klasa uzywana do reprezetancji obiektu Meal.

       Atrybuty
       --------------

       Metody
       --------------
       ToDo
    """

    def __init__(self, name, prepareTime, ingredientsList):
        self._name = name
        self._prepareTime = prepareTime
        self._ingredientsList = ingredientsList


    @property
    def name(self):
        return self._name

    @property
    def prepareTime(self):
        return self._prepareTime

    @property
    def ingredientsList(self):
        return self._ingredientsList

    @name.setter
    def name(self, value):
        self._name = value

    @prepareTime.setter
    def prepareTime(self, value):
        self._prepareTime = value

    @ingredientsList.setter
    def ingredientsList(self, value):
        self._ingredientsList = value
