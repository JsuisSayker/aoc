#!/usr/bin/env python3

from itertools import product

def evaluate_equation(test_value, numbers):
    num_count = len(numbers)
    operator_count = num_count - 1
    operators = ['+', '*']

    for operator_combination in product(operators, repeat=operator_count):
        result = numbers[0]
        for i in range(operator_count):
            if operator_combination[i] == '+':
                result += numbers[i + 1]
            elif operator_combination[i] == '*':
                result *= numbers[i + 1]
        if result == test_value:
            return True
    return False

def total_calibration_result_from_content(content):
    total = 0

    for line in content.splitlines():
        line = line.strip()
        if not line:
            continue

        test_value, numbers_str = line.split(':')
        test_value = int(test_value.strip())
        numbers = list(map(int, numbers_str.strip().split()))

        if evaluate_equation(test_value, numbers):
            total += test_value

    return total

with open('input1.txt', 'r') as file:
    content = file.read()

result = total_calibration_result_from_content(content)
print(result)
