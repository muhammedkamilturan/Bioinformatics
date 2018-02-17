from mkt.core.fragment.mkt_core_fragment import Fragment
from mkt.core.types.mkt_core_types import Molecules

class Dna(Fragment):

    def __init__(self, symbol='', start=5, seq='', title='', start_point=-1):
        super().__init__(symbol, start, seq, title, start_point)
        self._type = Molecules.DNA

    def transcription(self):
        from mkt.core.molecules.rna.mkt_core_molecules_rna import Rna
        table = str.maketrans('ATGC', 'TACG')
        temp = Rna(self.symbol, self.start, self[::].translate(table), self.title, self.start_point)
        temp.complementary()
        return temp



