import copy
import datetime
import random
from mkt.alignment.ga.whitgap.gagene.mkt_aligment_ga_whitgap_gagene import GaGene
from mkt.core.types.mkt_core_types import Molecules


class GaChromosome(object):

    random.seed(datetime.datetime.now())

    #SCORE MATRIX
    __ns = {'AA': 10, 'AC': -1, 'AG': -2, 'AT': -3, 'A-': -4, 'AN': 10, 'NA': 10,
          'CA': -1, 'CC': 20, 'CG': -1, 'CT': -2, 'C-': -3, 'CN': 10, 'NC': 10,
          'GA': -2, 'GC': -1, 'GG': 20, 'GT': -4, 'G-': -3, 'GN': 10, 'NG': 10,
          'TA': -3, 'TC': -2, 'TG': -4, 'TT': 10, 'T-': -1, 'TN': 10, 'NT': 10,
          '-A': -4, '-C': -3, '-G': -3, '-T': -1, '--': -5, '-N': -2, 'N-': 2, 'NN': 10}

    def __init__(self, fragments):
        self.__fs = copy.deepcopy(fragments)
        self.__genes = []
        for i in range(len(self.__fs)):
            self.__genes.append(GaGene(self.__fs[i]))
        self.__score = 0

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        self.__score = value

    @property
    def genes(self):
        return self.__genes

    @genes.setter
    def genes(self, value):
        self.__genes = value

    def apply(self):
        #Genler fragmentlere uygulanacak ve nihayi uzunlukları aynı olsun diye max length maxl bulunacak
        contain = []
        maxl = -1
        for i in self.__genes:
            f1 = i.apply()
            if maxl < len(f1):
                maxl = len(f1)
            contain.append(f1.contain)
        #solutions boyları maxl 'da eşitlenecek ve bu sayede hepsinin boyu aynı olacak ve scorelanabilecekler
        for i in range(len(contain)):
            contain[i] = contain[i] + '-'*(maxl - len(contain[i]))
            self.__fs[i].contain = contain[i]
            self.__fs[i]._type = Molecules.ALIGMENT_FRAGMENT
        tr_contain = []
        #uygulma matrisinin transpozesi alınacak ve her dikey satır scorelanacak ve toplanarak CHR SCORE oluşturulacak
        for i in range(maxl):
            temp = ''
            for j in range(len(self.__genes)):
                temp = temp + contain[j][i]
            tr_contain.append(temp)
        self.__score = 0
        for k in tr_contain:
            for i in range(len(k)):
                for j in range(i+1, len(k)):
                    self.__score = self.__score + self.__ns[k[i]+k[j]]




