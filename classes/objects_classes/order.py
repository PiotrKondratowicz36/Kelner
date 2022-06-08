from enum import Enum
from classes.objects_classes.table import Table


class order_status(Enum):
    COMPLETED = 'completed'
    IN_PROGRESS = 'inprogress'


class order:

    """
        Klasa uzywana do reprezetancji obiektu Order.

        Atrybuty
        --------------

        Metody
        --------------
        ToDo
    """

    def __init__(self, listOfMeals, status, table):
        if status not in set(item.value for item in order_status):
            raise ValueError("order status not valid")
        self._status = status
        self._listOfMeals = listOfMeals
        self._table = table


    @property
    def list_of_meals(self):
        return self._listOfMeals

    @property
    def status(self):
        return self._status

    @property
    def table(self):
        return self._table

    @list_of_meals.setter
    def list_of_meals(self, value):
        self._listOfMeals = value

    @status.setter
    def status(self, value):
        self._status = value

    @table.setter
    def table(self, value):
        self._table = value
