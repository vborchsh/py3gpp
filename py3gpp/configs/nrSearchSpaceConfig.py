
class nrSearchSpaceConfig():
    def __init__(self):
        self._SearchSpaceID = 1
        self._Label = 'SearchSpace1'
        self._CORESETID = 1
        self._SearchSpaceType = 'ue'
        self._StartSymbolWithinSlot = 0
        self._SlotPeriodAndOffset = [1, 0]
        self._Duration = 1
        self._NumCandidates = [8, 8, 4, 2, 1]

    @property
    def SearchSpaceID(self):
        return self._SearchSpaceID

    @SearchSpaceID.setter
    def SearchSpaceID(self, nid):
        assert nid >= 0 , "The value must be in the >=0."
        self._SearchSpaceID = nid

    @property
    def Label(self):
        return self._Label

    @Label.setter
    def Label(self, label):
        assert type(label) == str, "The value must be a string."
        self._Label = label

    @property
    def CORESETID(self):
        return self._CORESETID

    @CORESETID.setter
    def CORESETID(self, nid):
        assert nid >= 0 and nid <= 12, "The value must be in the range 0..12."
        self._CORESETID = nid

    @property
    def SlotPeriodAndOffset(self):
        return self._SlotPeriodAndOffset

    @SlotPeriodAndOffset.setter
    def SlotPeriodAndOffset(self, val):
        assert len(val) == 2, "The value must be a list size 2."
        assert (val[1] <= val[0]) and val[1] >= 0, "The value must be a string."
        self._SlotPeriodAndOffset = val

    @property
    def SearchSpaceType(self):
        return self._SearchSpaceType

    @SearchSpaceType.setter
    def SearchSpaceType(self, val):
        assert val in ['ue', 'common'], "The value must be in ['ue', 'common']."
        self._SearchSpaceType = val

    @property
    def StartSymbolWithinSlot(self):
        return self._StartSymbolWithinSlot

    @StartSymbolWithinSlot.setter
    def StartSymbolWithinSlot(self, val):
        assert val >= 0 and val <= 13, "The value must be in 0..13."
        self._StartSymbolWithinSlot = val

    @property
    def Duration(self):
        return self._Duration

    @Duration.setter
    def Duration(self, duration):
        assert duration >= 0 and duration < 2560, "The duration must be in range 0..2559."
        self._Duration = duration

    @property
    def NumCandidates(self):
        return self._NumCandidates

    @NumCandidates.setter
    def NumCandidates(self, num):
        assert len(num) == 5, "The size of value must be 5."
        assert sum(num) != 0, "There is must be at least one candidate."
        self._NumCandidates = num
