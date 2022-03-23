from enum import Enum


class TableStatus(Enum):
    OCCUPIED = 'occupied'
    FREE = 'free'
    DIRTY = 'dirty'


class Table:

    """
           Klasa uzywana do reprezetancji obiektu Table.

           Atrybuty
           --------------
           TableStatus : enum
                dozwolone statusy stolika

           Metody
           --------------
           ToDo
    """

    def __init__(self, id, status):
        if status not in set(item.value for item in TableStatus):
            raise ValueError("table status not valid")
        self._status = status
        self._id = id


    @property
    def id(self):
        return self._id

    @property
    def status(self):
        return self._status

    @id.setter
    def id(self, value):
        self._id = value

    @status.setter
    def status(self, value):
        self._status = value
