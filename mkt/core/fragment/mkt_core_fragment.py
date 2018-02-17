from mkt.core.direction.mkt_core_direction import Direction
from mkt.core.types.mkt_core_types import Molecules


class Fragment(Direction):

    def __init__(self, symbol='', start=5, seq='', title='', start_point=-1):
        super().__init__(start)
        self.__symbol = symbol
        self.__seq = seq.upper()
        self.__title = title
        self.__sp = start_point
        self.__ep = start_point + len(self.__seq)
        self.__index = 0
        self._type = Molecules.FRAGMNET

    @property
    def contain(self):
        return self.__seq

    @contain.setter
    def contain(self, value):
        self.__seq = value.upper()

    @property
    def symbol(self):
        return self.__symbol

    @symbol.setter
    def symbol(self, value):
        self.__symbol = value

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        self.__title = value

    @property
    def start_point(self):
        return self.__sp

    @start_point.setter
    def start_point(self, value):
        self.__sp = value

    @property
    def end_point(self):
        return self.__ep

    def __len__(self):
        return len(self.__seq)

    def __iter__(self):
        return self

    def __next__(self):
        if self.__index < len(self):
            self.__index = self.__index + 1
            return self.__seq[self.__index - 1]
        else:
            raise StopIteration

    def __getitem__(self, item):
        return self.__seq[item]

    def __eq__(self, other):
        return (self.start == other.start) and (self[::] == other[::])

    def __repr__(self):
        return "{} {}: {} <{}> [{}]".format(self.__symbol,
                                            super().__repr__(),
                                            self.__seq,
                                            len(self),
                                            self._type)