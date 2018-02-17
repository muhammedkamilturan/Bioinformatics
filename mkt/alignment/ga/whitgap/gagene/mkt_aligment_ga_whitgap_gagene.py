import copy
import random
import datetime


class GaGene(object):
    random.seed(datetime.datetime.now())

    def __init__(self , fragment , tolerance = 0.85):
        self.__f = copy.deepcopy(fragment)
        maxl = int(len(fragment) * 0.85)
        self.__gene = []
        for i in range(maxl):
            self.__gene.append(random.randint(0 , len(fragment) - 1))
        self.__index = 0

    def apply(self):
        temp = sorted(self.__gene, reverse = True)
        temp = self[::]
        for i in temp:
            temp = self.__f[:i]+'-'+self.__f[i:]
        self.__f._seq = temp

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

