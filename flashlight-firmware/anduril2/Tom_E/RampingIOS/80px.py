#!/usr/bin/env python

def main(args):
    values = [
    0,2,3,4,5,7,8,9,                    11,12,14,15,17,18,20,22,
    23,25,27,29,30,32,34,36,            38,40,42,44,47,49,51,53,
    56,58,60,63,66,68,71,73,            76,79,82,85,87,90,93,96,
    100,103,106,109,113,116,119,123,    126,130,134,137,141,145,149,153,
    157,161,165,169,173,178,182,186,    191,196,200,205,210,214,219,224,
    229,234,239,244,250,255
    ]

    values = [int(0.8 * v) for v in values]

    print(",".join(str(x) for x in values))

if __name__ == "__main__":
    import sys
    main(sys.argv[1:])

