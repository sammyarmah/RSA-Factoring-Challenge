#!/usr/bin/python3
import sys


def factorize(numb):
    """ Generates 2 factors for a given number"""
    factor_1 = 2
    while (numb % factor_1):
        if (factor_1 <= numb):
            factor_1 += 1

    factor_2 = numb // factor_1
    return (factor_2, factor_1)


if len(sys.argv) != 2:
    sys.exit(f"Wrong usage: {sys.argv[0]} <file_path>")

filename = sys.argv[1]

file = open(filename, 'r')
lines = file.readlines()

for line in lines:
    numb = int(line.rstrip())
    factor_2, factor_1 = factorize(numb)
    print(f"{numb} = {factor_2} * {factor_1}")
