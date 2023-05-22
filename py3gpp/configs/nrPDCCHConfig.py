
from .nrPDCCHConfigBase import nrPDCCHConfigBase
from .nrCORESETConfig import nrCORESETConfig
from .nrSearchSpaceConfig import nrSearchSpaceConfig

def nrPDCCHConfig(nrPDCCHConfigBase):
    def __init__():
        self._NStartBWP = 0
        self._NSizeBWP = 48
        self._CORESET = nrCORESETConfig
        self._SearchSpace = nrSearchSpaceConfig
        self._RNTI = 1

    @property
    def NStartBWP(self):
        return self._NStartBWP

    @NStartBWP.setter
    def NStartBWP(self, n):
        assert n >= 0 and n <= (2199+275-1)
        self._NStartBWP = n

    @property
    def NSizeBWP(self):
        return self._NSizeBWP

    @NSizeBWP.setter
    def NSizeBWP(self, n):
        assert n >= 0 and n <= 257
        self._NSizeBWP = n

    @property
    def CORESET(self):
        return self._CORESET

    @CORESET.setter
    def CORESET(self, coreset: nrCORESETConfig):
        self._CORESET = coreset

    @property
    def SearchSpace(self):
        return self._SearchSpace

    @SearchSpace.setter
    def SearchSpace(self, space: nrSearchSpaceConfig):
        self._SearchSpace = space

    @property
    def RNTI(self):
        return self._RNTI

    @RNTI.setter
    def RNTI(self, rnti):
        assert rnti >= 1 and rnti <= 65519
        self._RNTI = rnti
