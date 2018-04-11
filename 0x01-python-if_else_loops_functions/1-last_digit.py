#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
outp = "Last digit of {:d} is {:d} "
if abs(abs(number) % 10) > 5:
    outp = outp + "and is greater than 5"
elif abs(abs(number) % 10) == 0:
    outp = outp + "and is zero"
else:
    outp = outp + "and is less than 6 and not 0"
print(outp.format(number, abs(abs(number) % 10)))
