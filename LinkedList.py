"""
Доделать связанный список
"""


class LinkedList:

    def __int__(self):
        self._begin = None

    def insert(self, x):
        self._begin = [x, self._begin]

    def pop(self):
        if self._begin is None:
            raise "Список пуст"
        x = self._begin[0]
        self._begin = self._begin[1]
        return x