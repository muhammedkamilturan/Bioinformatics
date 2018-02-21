from mkt.alignment.ga.whitgap.gagenes.mkt_alignment_whitgap_gagenes import GaGenes
import random
import datetime
import copy

class GaChromosome(object):

    #SCORE MATRIX
    __ns = {'AA': 10, 'AC': -1, 'AG': -2, 'AT': -3, 'A-': -4, 'AN': 10, 'NA': 10,
          'CA': -1, 'CC': 20, 'CG': -1, 'CT': -2, 'C-': -3, 'CN': 10, 'NC': 10,
          'GA': -2, 'GC': -1, 'GG': 20, 'GT': -4, 'G-': -3, 'GN': 10, 'NG': 10,
          'TA': -3, 'TC': -2, 'TG': -4, 'TT': 10, 'T-': -1, 'TN': 10, 'NT': 10,
          '-A': -4, '-C': -3, '-G': -3, '-T': -1, '--': -5, '-N': -2, 'N-': 2, 'NN': 10}

    random.seed(datetime.datetime.now())

    def __init__(self, fragments):
        self.__f = fragments
        self.__chr = []
        for i in fragments:
            self.__chr.append(GaGenes(i))
        self.__score = 0

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        self.__score = value

    @property
    def genes(self):
        return self.__chr

    @genes.setter
    def genes(self, value):
        self.__chr = value

    def recombination(self, other):
        t1 = random.randint(0, len(self.__chr)-1)
        break_point = min(len(self.__chr[t1].contain), len(other.genes[t1].contain))
        g1C = self.__chr[t1].contain[:break_point] + other.genes[t1].contain[break_point:]
        g2C = other.genes[t1].contain[:break_point] + self.__chr[t1].contain[break_point:]
        self.__chr.remove(self.__chr[t1])
        other.genes.remove(other.genes[t1])
        g1 = GaGenes(self.__f[t1])
        g2 = GaGenes(self.__f[t1])
        g1.contain = copy.deepcopy(g1C)
        g2.contain = copy.deepcopy(g2C)
        return (g1, g2)

    def apply(self):
        self.__score = 0
        f = []
        maxl = -1
        #fragmentlere gen çözümleri uygulanıyor
        for i in self.__chr:
            tempf = i.apply()
            if len(tempf) > maxl:
                maxl = len(tempf)
            f.append(tempf)
        #sonuç boyları eşitleniyor
        for i in f:
            if len(i) < maxl:
                i.contain = i.contain + "-"*(maxl - len(i))
        #score hesaplamak için transposeleri alınacak
        t_f = []
        for i in range(len(f[0])):
            temp = []
            for j in range(len(f)):
                temp.append(f[j].contain[i])
            t_f.append(temp)
        #score hesaplanıyor
        for k in t_f:
            for i in range(len(k)):
                for j in range(i+1, len(k)):
                    self.__score = self.__score + self.__ns[k[i] + k[j]]
