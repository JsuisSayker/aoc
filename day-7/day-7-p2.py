#!/usr/bin/env python3
from itertools import product

def evaluate_equation(test_value, numbers):
    num_count = len(numbers)
    operator_count = num_count - 1
    operators = ['+', '*', '||']

    for operator_combination in product(operators, repeat=operator_count):
        result = numbers[0]
        for i in range(operator_count):
            if operator_combination[i] == '+':
                result += numbers[i + 1]
            elif operator_combination[i] == '*':
                result *= numbers[i + 1]
            elif operator_combination[i] == '||':
                result = int(str(result) + str(numbers[i + 1]))
        if result == test_value:
            return True
    return False

def total_calibration_result(filename):
    total = 0

    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue

            test_value, numbers_str = line.split(':')
            test_value = int(test_value.strip())
            numbers = list(map(int, numbers_str.strip().split()))

            if evaluate_equation(test_value, numbers):
                total += test_value

    return total

filename = "input1.txt"
result = total_calibration_result(filename)
print(f"Total calibration result: {result}")

