
# 1710. Maximum Units on a Truck


def maxUnits(boxTypes, truckSize):

    boxTypes.sort(key=lambda x: x[1], reverse=True)
    total_units = 0
    for numBox, units in boxTypes:
        if truckSize <= numBox:
            total_units += truckSize*units
            break

        total_units += numBox * units

        truckSize -= numBox

    return total_units
