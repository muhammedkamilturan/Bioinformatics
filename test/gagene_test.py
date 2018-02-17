from mkt.alignment.ga.whitgap.gagene import GaGene
from mkt.core.fragment import Fragment

f = Fragment('Teo1',5,'atgcatgcatgc')
print(f)

g = GaGene(f)

for i in g:
    print(i)

f1 = g.apply()
print(f1)

for i in range(100000):
    g.auto_mutatio()
f1 = g.apply()
print('İLK 100000 mutasyon')
print(f1)
for i in range(100000):
    g.auto_mutatio()


f1 = g.apply()

print(f1)

