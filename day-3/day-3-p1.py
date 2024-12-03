#!/usr/bin/env python3

import re


def getMulPatternInCorruptedFile(file_path):
    uncorrupted = []
    total = 0
    with open(file_path, "r") as file:
        lines = file.readlines()
    for line in lines:
        uncorrupted.append(re.findall(r"mul\(\d+,\d+\)", line))
        for mul in uncorrupted[-1]:
            total += int(mul.split("(")[1].split(",")[0]) * int(
                mul.split(",")[1].split(")")[0])
    return total


file_path = 'input1.txt'
result = getMulPatternInCorruptedFile(file_path)
print(result)
