from mkt.alignment.ga.whitgap.gachromosome.mkt_alignment_ga_whitgap_gachromosome import GaChromosome
import operator
import random
import datetime


class GaGenome(object):

    random.seed(datetime.datetime.now())

    def __init__(self, fragments, initial_size=100, mutation_rate=0.04, elitism_rate=0.4):
        self.__chrs = []
        for i in range(initial_size):
            self.__chrs.append(GaChromosome(fragments))
        self.__ms = -99999999999999
        self.__mr = mutation_rate
        self.__er = elitism_rate
        self.__is = initial_size

    @property
    def chromosomes(self):
        return self.__chrs

    @chromosomes.setter
    def chromosomes(self, value):
        self.__chrs = value

    def apply(self):
        self.__ms = -99999999999999
        for i in self.__chrs:
            i.apply()
            if i.score > self.__ms:
                self.__ms = i.score
        #score değerine göre sırala
        self.__chrs = sorted(self.__chrs , key = operator.attrgetter('score') , reverse = True)
        print(self.__ms)
        #elitik bireyler yeni popüğlasyona aktarılacak
        new_population = []
        for i in range(int(self.__is * self.__er)):
            new_population.append(self.__chrs[i])
        #recombinasyon yapılacak
        while(len(new_population) != self.__is-1):
            t1 = random.randint(0, len(new_population)-1)
            t2 = random.randint(0, len(new_population)-1)
            print(t1,t2, len(new_population),len(self.__chrs))
            print(type(new_population[t1]))
            r = new_population[t1].recombination(new_population[t2])
            new_population.append(r[0])
            new_population.append(r[1])
