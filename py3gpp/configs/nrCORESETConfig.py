
import numpy as np

class nrCORESETConfig():
    def __init__(self):
        self._CORESETID = 1
        self._Label = 'CORESET1'
        self._FrequencyResources = 8*[1]
        self._Duration = 2
        self._CCEREGMapping = 'interleaved'
        self._REGBundleSize = 6
        self._InterleaverSize = 2
        self._ShiftIndex = 0
        self._PrecoderGranularity = 'sameAsREG-bundle'
        self._RBOffset = []

    @property
    def CORESETID(self):
        return self._CORESETID

    @CORESETID.setter
    def CORESETID(self, nid):
        assert nid >= 0 and nid <= 12, "The value must be in the range 0..12."
        self._CORESETID = nid

    @property
    def Label(self):
        return self._Label

    @Label.setter
    def Label(self, label):
        assert type(label) == str, "The value must be a string."
        self._Label = label

    @property
    def FrequencyResources(self):
        return self._FrequencyResources

    @FrequencyResources.setter
    def FrequencyResources(self, fr):
        assert len(fr) <= 45, "The length must <= 45."
        self._FrequencyResources = fr

    @property
    def Duration(self):
        return self._Duration

    @Duration.setter
    def Duration(self, duration):
        assert duration in [1, 2, 3], "The duration must be in range 1..3."
        self._Duration = duration

    @property
    def CCEREGMapping(self):
        return self._CCEREGMapping

    @CCEREGMapping.setter
    def CCEREGMapping(self, cceregmap):
        assert cceregmap in ['interleaved', 'noninterleaved'], "The value must be 'interleaved' or 'noninterleaved'."
        self._CCEREGMapping = cceregmap

    @property
    def REGBundleSize(self):
        return self._REGBundleSize

    @REGBundleSize.setter
    def REGBundleSize(self, bundlesize):
        assert bundlesize in [2, 3, 6], "The value must be in [2, 3, 6]"
        self._REGBundleSize = bundlesize

    @property
    def InterleaverSize(self):
        return self._InterleaverSize

    @InterleaverSize.setter
    def InterleaverSize(self, intersize):
        assert intersize in [2, 3, 6], "The value must be in [2, 3, 6]"
        self._InterleaverSize = intersize

    @property
    def ShiftIndex(self):
        return self._ShiftIndex

    @ShiftIndex.setter
    def ShiftIndex(self, shiftidx):
        assert shiftidx >= 0 and shiftidx <= 1007, "The value must be in 0..1007."
        self._ShiftIndex = shiftidx

    @property
    def PrecoderGranularity(self):
        return self._PrecoderGranularity

    @PrecoderGranularity.setter
    def PrecoderGranularity(self, granul):
        assert granul in ['sameAsREG-bundle', 'allContiguousRBs'], "The value must be 'sameAsREG-bundle' or 'allContiguousRBs'."
        self._PrecoderGranularity = granul

    @property
    def RBOffset(self):
        return self._RBOffset

    @RBOffset.setter
    def RBOffset(self, offset):
        assert offset >= 0 and offset <= 5, "The value must be in 0..5."
        self._RBOffset = offset

    # Each frequency resource bitmap bit represents a block of 6 PRB/REG, and 6 PRB/REG equals a CCE
    @property
    def NCCE(self):
        ncce = 0
        for x in self.FrequencyResources:
            if x:
                ncce += x*self.Duration
        return ncce

    # Output the REG bundles ordering, interleaved or not.
    def getCCEMapping(self):
        # Find the CCE-to-REG mapping
        crstCCEs = self.NCCE   # Number of CCE (groups of 6 REG/RB) in CORESET
        numREGs = 6*crstCCEs  # Number of REG/RB in CORESET
        if self.CCEREGMapping == 'interleaved':
            L = self.REGBundleSize
            R = self.InterleaverSize
            C = numREGs/(L*R)
            f = np.zeros(R*C) # Interleaved REG bundles
            for cIdx in range(C):
                for rIdx in range(R):
                    x = cIdx*R + rIdx
                    f[x+1] = (rIdx*C + cIdx + self.ShiftIndex) % (R*C)
        else # non-interleaved
            # Only L=6, 1 REG Bundle == 1 CCE == 6 RB
            L = 6
            f = np.array(range(crstCCEs))

        return [f, L]