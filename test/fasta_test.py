from mkt.parser import Fasta

f = Fasta.from_file(r'd:/py3/bioinformatics/test/PF00014.fasta')
for i in f:
    print(i, i.title)