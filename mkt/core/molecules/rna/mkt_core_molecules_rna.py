from mkt.core.fragment.mkt_core_fragment import Fragment
from mkt.core.types.mkt_core_types import Molecules
from mkt.core.tables import CodonToAminoacid


class Rna(Fragment):

    def __init__(self, symbol='', start=5, seq='', title='', start_point=-1):
        super().__init__(symbol, start, seq, title, start_point)
        self._type = Molecules.RNA

    def reverse_transcription(self):
        from mkt.core.molecules.dna.mkt_core_molecules_dna import Dna
        table = str.maketrans('AUGC', 'TACG')
        temp = Dna(self.symbol, self.start, self[::].translate(table), self.title, self.start_point)
        temp.complementary()
        return temp

    def translation(self):
        from mkt.core.molecules.protein.mkt_core_molecules_protein import Protein
        temp_seq = ''
        for i in range(0, len(self), 3):
            codon = self[::][i:i+3]
            temp_seq = temp_seq + CodonToAminoacid[codon]
        temp = Protein(self.symbol, temp_seq, self.title, self.start_point)
        return temp

    def orfs(self):
        import re
        result = []
        regex = r"(?=AUG((?:.{3})+?)U(?:AG|AA|GA))"
        matches = re.finditer(regex, self[::])
        for matchNum, match in enumerate(matches):
            matchNum = matchNum + 1
            for groupNum in range(0, len(match.groups())):
                groupNum = groupNum + 1
                nrna = Rna('ORF{}'.format(matchNum),self.start, 'AUG'+match.group(groupNum))
                nrna.start_point = match.start(groupNum) -3
                result.append(nrna)
                del(nrna)
        return result

