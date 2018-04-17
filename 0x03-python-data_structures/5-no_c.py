#!/usr/bin/python3
def no_c(my_string):
    new_str = ""
    for ltr in my_string:
        if ltr != 'c' and ltr != 'C':
            new_str = new_str + ltr
    return new_str
