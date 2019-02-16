import math

"""
16 bit integers:
    0-3: channel number
    4-7: time
    8-15: pulse height
"""


def pulseDecode(integer):
    if int(integer) > 65535:
        print("this is larger than 16 bits int, retry")
        return 0
    # assume input is in integer not binary already
    # turn integer to bits string
    allbits = format(int(integer), '#010b')[4:]
    chanBits = int(allbits[0:3], 2)
    timeBits = int(allbits[4:7], 2)
    pulseHeightBits = int(allbits[8:15], 2)

    print("In %d channel, at time %d, pulse height is %d" %
          (chanBits, timeBits, pulseHeightBits))


number = int(input("give me a number within 16bits"))
pulseDecode(number)
