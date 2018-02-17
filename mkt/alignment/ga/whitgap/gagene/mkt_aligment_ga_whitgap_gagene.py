import copy
import random
import datetime
from mkt.core.types.mkt_core_types import Molecules

class GaGene(object):
    random.seed(datetime.datetime.now())

    def __init__(self , fragment):
        self.__f = copy.deepcopy(fragment)
        maxl = len(fragment)
        self.__gene = []
        for i in range(maxl):
            self.__gene.append(random.randint(0 , len(fragment) - 1))
        self.__index = 0

    def apply(self):
        temp = sorted(self.__gene, reverse = True)
        for i in temp:
            self.__f.contain = self.__f[:i]+'-'+self.__f[i:]
        self.__f._type = Molecules.ALIGMENT_FRAGMENT
        return self.__f

    def increment(self):
        t1 = random.randint(0, len(self.__gene) - 1)
        if self.__gene[t1] < len(self.__f):
            self.__gene[t1] = self.__gene[t1] + 1

    def decrement(self):
        t1 = random.randint(0 , len(self.__gene) - 1)
        if self.__gene[t1] > 0:
            self.__gene[t1] = self.__gene[t1] - 1

    def deletion(self):
        if len(self.__gene) > 1:
            t1 = random.randint(0 , len(self.__gene) - 1)
            self.__gene.remove(self.__gene[t1])

    def duplicate(self):
        t1 = random.randint(0 , len(self.__gene) - 1)
        self.__gene.append(random.randint(0 , len(self.__f) - 1))

    def auto_mutatio(self):
        t1 = random.randint(0 , 4)
        if t1 == 0:
            self.increment()
        elif t1 == 1:
            self.decrement()
        elif t1 == 2:
            self.deletion()
        elif t1 == 3:
            self.duplicate()

    def __iter__(self):
        return self

    def __next__(self):
        if self.__index < len(self.__gene):
            self.__index = self.__index + 1
            return self.__gene[self.__index - 1]
        else:
            raise StopIteration

    def __getitem__(self , item):
        return self.__gene[item]

