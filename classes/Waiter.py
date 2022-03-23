class Waiter:

    """
        Klasa uzywana do reprezetancji obiektu Waiter.

        Atrybuty
        --------------

        Metody
        --------------
        ToDo
    """

    def __init__(self, listOfOrders, listOfTables):
        self._listOfOrders = listOfOrders
        self._listOfTables = listOfTables


    @property
    def listOfOrders(self):
        return self._listOfOrders

    @property
    def listOfTables(self):
        return self._listOfTables

    @listOfOrders.setter
    def listOfOrders(self, value):
        self._listOfOrders = value

    @listOfTables.setter
    def listOfTables(self, value):
        self._listOfTables = value

listOfOrders = []
listOfTables = []

waiter = Waiter(listOfOrders, listOfTables)
