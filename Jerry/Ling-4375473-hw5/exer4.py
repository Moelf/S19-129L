import math

"""
16 bit integers:
    0-3: channel number
    4-7: time
    8-15: pulse height
"""


def pulseDecode(integer):
    if int(integer) > 65535:
        print("this is not an unsigned 16 bits int, retry")
        return 0
    # assume input is in integer not binary already
    # turn integer to bits string
    allbits = bin(int(integer))[2:]
    # fix length
    leading_zeros = "0" * (16-len(allbits))
    allbits = leading_zeros+allbits
    # [a:b] includes a not b
    chan= int(allbits[0:4], 2)
    time= int(allbits[4:8], 2)
    pulseHeight= int(allbits[8:16], 2)

    print("In %d channel, at time %d, pulse height is %d" %
          (chan, time, pulseHeight))


number = int(input("give me a number within 0-65535: "))
pulseDecode(number)
