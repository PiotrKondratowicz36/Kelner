from enum import Enum
from Table import Table


class OrderStatus(Enum):
    COMPLETED = 'completed'
    IN_PROGRESS = 'inprogress'


class Order:

    """
        Klasa uzywana do reprezetancji obiektu Order.

        Atrybuty
        --------------

        Metody
        --------------
        ToDo
    """

    def __init__(self, listOfMeals, status, table):
        if status not in set(item.value for item in OrderStatus):
            raise ValueError("order status not valid")
        self._status = status
        self._listOfMeals = listOfMeals
        self._table = table


    @property
    def listOfMeals(self):
        return self._listOfMeals

    @property
    def status(self):
        return self._status

    @property
    def table(self):
        return self._table

    @listOfMeals.setter
    def listOfMeals(self, value):
        self._listOfMeals = value

    @status.setter
    def status(self, value):
        self._status = value

    @table.setter
    def table(self, value):
        self._table = value
