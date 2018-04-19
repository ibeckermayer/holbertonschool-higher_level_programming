#!/usr/bin/python3
def roman_to_int(roman_string):
    answer = 0
    if isinstance(roman_string, str):
        roms = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10,
                'XL': 40, 'L': 50, 'XC': 90, 'C': 100, 'CD': 400,
                'D': 500, 'CM': 900, 'M': 1000}

        last = 1
        for i in range(len(roman_string) - 1):
            key = roman_string[i] + roman_string[i + 1]
            if key in roms:
                last = 0
                answer += roms[key]
            else:
                last = 1
                answer += roms[roman_string[i]]
        if last:
            answer += roms[roman_string[len(roman_string) - 1]]

    return answer
