
import numpy as np

def getRelativeNSlotAndSFN(NSlotA, NFrameA, SlotsPerFrame):
    # Calculate the appropriate frame number (0...1023) based on the absolute slot number
    NFrameR = np.mod(NFrameA + np.fix(NSlotA/SlotsPerFrame), 1024)
    # Relative slot number (0...slotsPerFrame-1)
    NSlotR = np.mod(NSlotA, SlotsPerFrame)

    return [NSlotR, NFrameR]