#!/usr/bin/python3
if __name__ == '__main__':
    import sys

    if len(sys.argv) == 1:
        print("0 arguments.")
    else:
        if len(sys.argv) == 2:
            print("1 argument:")
        else:
            print("{:d} arguments:".format(len(sys.argv) - 1))
        c = 1
        for arg in sys.argv[1:]:
            print("{:d}: {:s}".format(c, arg))
            c += 1
