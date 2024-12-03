#!/usr/bin/env python3

import re


def getMulPatternInCorruptedFileWithCondition(file_path):
    uncorrupted = []
    total = 0
    action = True
    with open(file_path, "r") as file:
        lines = file.readlines()
    for line in lines:
        uncorrupted.append(re.findall(
            r"mul\(\d+,\d+\)|don't\(\)|do\(\)", line))
        for mul in uncorrupted[-1]:
            if "do()" in mul:
                action = True
            elif "don't()" in mul:
                action = False
            elif action:
                total += int(mul.split("(")[1].split(",")[0]) * int(
                    mul.split(",")[1].split(")")[0])
    return total


file_path = 'input1.txt'
result2 = getMulPatternInCorruptedFileWithCondition(file_path)
print(result2)
