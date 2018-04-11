#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
outp = "Last digit of {:d} is {:d} "
if number >= 0:
    if number % 10 > 5:
        outp = outp + "and is greater than 5"
    elif number % 10 == 0:
        outp = outp + "and is 0"
    else:
        outp = outp + "and is less than 6 and not 0"
    print(outp.format(number, number % 10))
else:
    if number % 10 == 0:
        outp = outp + "and is 0"
        print(outp.format(number, number % 10))
    else:
        outp = outp + "and is less than 6 and not 0"
        print(outp.format(number, -(10 - number % 10)))
