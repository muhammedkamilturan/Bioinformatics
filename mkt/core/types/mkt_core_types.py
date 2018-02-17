from enum import Enum

class Molecules(Enum):
    DNA = 0
    RNA = 1
    PROTEIN = 2
    FRAGMNET = 3
    ALIGMENT_FRAGMENT=4
    ALIGMENT_DNA = 5
    ALIGMENT_RNA = 6
    ALIGMNET_PROTEIN = 7

    def describe(self):
        return self.name , self.value

    def __str__(self):
        return '{}'.format(self.name)

