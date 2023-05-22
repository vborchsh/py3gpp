
def nrPDCCHConfigBase():
    def __init__():
        self._DMRSScramblingID = 2
        self._AggregationLevel = 8
        self._AllocatedCandidate = 1
        self._CCEOffset = []

    @property
    def DMRSScramblingID(self):
        return self._DMRSScramblingID

    @DMRSScramblingID.setter
    def DMRSScramblingID(self, dmrs_scr_id):
        assert dmrs_scr_id >= 0 and dmrs_scr_id <= 65535
        self._DMRSScramblingID = dmrs_scr_id

    @property
    def AggregationLevel(self):
        return self._AggregationLevel

    @AggregationLevel.setter
    def AggregationLevel(self, lvl):
        assert lvl in [1, 2, 4, 8, 16]
        self._AggregationLevel = lvl

    @property
    def AllocatedCandidate(self):
        return self._AllocatedCandidate

    @AllocatedCandidate.setter
    def AllocatedCandidate(self, cand):
        assert cand >= 1 and cand <= 8
        self._AllocatedCandidate = cand

    @property
    def CCEOffset(self):
        return self._CCEOffset

    @CCEOffset.setter
    def CCEOffset(self, offset):
        if len(offset) != 0:
            for x in offset:
                assert x >= 0
        self._CCEOffset = offset
        