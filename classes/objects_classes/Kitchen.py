class Kitchen:

    """
        Klasa uzywana do reprezetancji obiektu Kitchen.

        Atrybuty
        --------------

        Metody
        --------------
        ToDo
    """

    def __init__(self, activeOrders, finishedOrders):
        self._activeOrders = activeOrders
        self._finishedOrders = finishedOrders

    @property
    def activeOrders(self):
        return self._activeOrders

    @property
    def finishedOrders(self):
        return self._finishedOrders

    @activeOrders.setter
    def activeOrders(self, value):
        self._activeOrders = value

    @finishedOrders.setter
    def finishedOrders(self, value):
        self._finishedOrders = value

activeOrders = []
finishedOrders = []

kitchen = Kitchen(activeOrders, finishedOrders)
