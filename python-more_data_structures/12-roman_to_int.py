#!/usr/bin/python
def roman_to_int(roman_string):
    a = 0
    for i in roman_string:
        if i == "I":
            a += 1
        elif i == "V":
            a += 5
        elif i == "X":
            a += 10
        elif i == "L":
            a += 50
        elif i == "C":
            a += 100
        elif i == "D":
            a += 500
        elif i == "M":
            a += 1000
    return a
