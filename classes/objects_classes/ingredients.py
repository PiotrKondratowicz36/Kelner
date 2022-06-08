from dataclasses import dataclass


class Ingredients:
    """
    Klasa uzywana do reprezentacji obiektu Ingredient


    Atrybuty
    --------------

    Metody
    --------------
    ToDo
    """

    def __init__(self, name, origin, hasGluten):
        self._name = name
        self._origin = origin
        self._hasGluten = hasGluten


    @property
    def name(self):
        return self._name

    @property
    def origin(self):
        return self._origin

    @property
    def hasGluten(self):
        return self._hasGluten

    @name.setter
    def name(self, value):
        self._name = value

    @origin.setter
    def origin(self, value):
        self._origin = value

    @hasGluten.setter
    def hasGluten(self, value):
        self._hasGluten = value
