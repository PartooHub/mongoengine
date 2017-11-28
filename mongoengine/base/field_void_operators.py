# -*- coding: utf-8 -*-


class SpreadObject(object):
    """
    An object such that list(*obj()) == [] ; dict(**obj()) == {}
    """
    def keys(self):
        return []

    def __getitem__(self, item):
        return self

    def __iter__(self):
        return self

    def next(self):
        raise StopIteration

    def __eq__(self, other):
        return True

    def __ne__(self, other):
        return True

    def __ge__(self, other):
        return True

    def __le__(self, other):
        return True


IGNORE = SpreadObject()
RESET_DEFAULT = SpreadObject()
