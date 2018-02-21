from mkt.alignment.ga.whitgap.gachromosome import GaChromosome
from mkt.parser.fasta import Fasta
import matplotlib.pyplot as plt
import numpy as np


fragments = Fasta.from_file(r'/home/mkturan/Repository/bioinformatics/test/aling_ga_genes/fragments.fasta')

result = []
for k in range(100):
    chr = GaChromosome(fragments)
    chr.apply()
    result.append(chr.score)


'''resultArr = np.asarray(result)
n, bins, patches = plt.hist(resultArr, 10, normed=1, facecolor='g', alpha=0.75)

plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title('Histogram of IQ')
plt.grid(True)
plt.show()'''



