from mkt.alignment.ga.whitgap import GaChromosome, GaGene
from mkt.parser.fasta import Fasta

f = Fasta.from_file(r'/home/mkturan/Repository/bioinformatics/test/aligment/ga_whitgap/fragments.fasta')
chr = GaChromosome(f)

chr.apply()
