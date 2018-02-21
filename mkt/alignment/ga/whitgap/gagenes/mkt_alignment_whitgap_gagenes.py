import copy
import datetime
import random
from mkt.core.types import Molecules
from mkt.core.fragment import Fragment


class GaGenes(object):

    random.seed(datetime.datetime.now())

    def __init__(self, fragment):
        self.__contain = []
        self.__f = copy.deepcopy(fragment)
        maxl = len(fragment)
        for i in range(random.randint(int(maxl/2), maxl-1)):
            self.__contain.append(random.randint(0, len(fragment) - 1))

    @property
    def contain(self):
        return self.__contain

    @contain.setter
    def contain(self, value):
        self.__contain = value

    def apply(self):
        f = Fragment(self.__f.symbol , self.__f.start , self.__f.contain , self.__f.title)
        for i in sorted(self.__contain, reverse = True):
            f.contain = f.contain[:i]+'-'+f.contain[i:]
        f._type = Molecules.ALIGMENT_FRAGMENT
        return f

    def increment(self):
        t1 = random.randint(0, len(self.__contain) - 1)
        if self.__contain[t1] < len(self.__f):
            self.__contain[t1] = self.__contain[t1] + 1

    def decrement(self):
        t1 = random.randint(0 , len(self.__contain) - 1)
        if self.__contain[t1] > 0:
            self.__contain[t1] = self.__contain[t1] - 1

    def deletion(self):
        if len(self.__contain) > 1:
            t1 = random.randint(0 , len(self.__contain) - 1)
            self.__contain.remove(self.__contain[t1])

    def duplication(self):
        t1 = random.randint(0 , len(self.__contain) - 1)
        self.__contain.append(self.__contain[t1])

    def auto_mutation(self):
        t1 = random.randint(0, 3)
        if t1 == 0:
            self.increment()
        elif t1 == 1:
            self.decrement()
        elif t1 == 2:
            self.deletion()
        elif t1 == 3:
            self.duplication()
