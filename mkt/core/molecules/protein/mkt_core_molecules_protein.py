from mkt.core.fragment.mkt_core_fragment import Fragment
from mkt.core.types.mkt_core_types import Molecules

class Protein(Fragment):

    def __init__(self, symbol='', seq='', title='', start_point=-1):
        super().__init__(symbol, 5, seq, title, start_point)
        self._type = Molecules.PROTEIN

    def __repr__(self):
        return "{} N->C: {} <{}> [{}]".format(self.symbol,
                                            self[::],
                                            len(self),
                                            self._type)