from mkt.parser import Fasta

f = Fasta.from_file(r'/home/mkturan/Repository/bioinformatics/test/PF00014.fasta')
for i in f:
    print(i, i.title)