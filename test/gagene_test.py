from mkt.alignment.ga.whitgap.gagene import GaGene
from mkt.core.fragment import Fragment

f = Fragment('Teo1',5,'atgcatgcatgc')
print(f)

g = GaGene(f)

for i in g:
    print(i)

f1 = g.apply()

print(f1)

