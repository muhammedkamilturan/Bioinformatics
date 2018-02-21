from mkt.alignment.ga.whitgap.gagenome import GaGenome
from mkt.parser.fasta import Fasta

fragments = Fasta.from_file(r'/home/mkturan/Repository/bioinformatics/test/aling_ga_genes/fragments.fasta')

g = GaGenome(fragments, 100)
g.apply()
print(g.chromosomes[0].score)
g.chromosomes[0].recombination(g.chromosomes[1])
