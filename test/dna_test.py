from mkt.core.molecules.dna import Dna

d1 = Dna('Teo1', 5, 'attgggcccc', 'deneme dizisi', 10)
print(d1)
print('LENGTH:', len(d1))
print(d1[::])
r1 = d1.transcription()
print(r1)