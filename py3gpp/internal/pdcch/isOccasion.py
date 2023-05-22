
from .nrCarrierConfig import nrCarrierConfig
from .nrPDCCHConfig import nrPDCCHConfig

def isOccasion(carrier: nrCarrierConfig, pdcch: nrPDCCHConfig):
    # Get the monitoring occasion in a slot
    slotsPerFrame = carrier.SlotsPerFrame
    ssPeriodOffset = pdcch.SearchSpace.SlotPeriodAndOffset
    ssDuration = pdcch.SearchSpace.Duration

    # Extract time counters
    absNSlot = carrier.NSlot  # Absolute slot number
    NFrame   = carrier.NFrame # Absolute frame number

    # Get relative slot number and relative frame number
    [slotNum, frameNum] = getRelativeNSlotAndSFN(absNSlot, NFrame, carrier.SlotsPerFrame)

    ssPeriod = ssPeriodOffset[0]

    # Slot number measured from SS slot offset + d, where d = (0...ssDuration-1).
    # SS slot offset + d is limited to the SS period.
    # slotOffsets = ssPeriodOffset[1]+(0:ssDuration-1)
    slotOffsets = [x+ssPeriodOffset[1] for x in range(0:ssDuration)]
    # slots = frameNum * slotsPerFrame + slotNum - slotOffsets(slotOffsets < ssPeriod)
    slots = [(frameNum * slotsPerFrame + slotNum - x) for x in slotOffsets if (x < ssPeriod)]
    
    # If any of these slot numbers are a multiple of the SS period, this is
    # a PDCCH monitoring occasion.
    return np.any(np.mod(slots, ssPeriod) == 0)
    