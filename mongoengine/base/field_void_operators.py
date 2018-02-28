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


IGNORE = SpreadObject()
RESET_DEFAULT = SpreadObject()
