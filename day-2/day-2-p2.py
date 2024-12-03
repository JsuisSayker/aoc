#!/usr/bin/env python3

def verify_list(numbers):
    increasing = None
    for i in range(1, len(numbers)):
        diff = numbers[i] - numbers[i - 1]

        if increasing is None:
            increasing = diff > 0

        if (diff > 0 and not increasing) or (diff < 0 and increasing):
            return False

        if abs(diff) < 1 or abs(diff) > 3:
            return False

    return True


def try_removals(numbers):
    for i in range(len(numbers)):
        reduced = numbers[:i] + numbers[i + 1:]
        if verify_list(reduced):
            return True
    return False


def get_safe_report(file_path):
    safe_report = []
    unsafe_report = []

    with open(file_path, "r") as file:
        for line in file:
            numbers = list(map(int, line.strip().split()))

            if verify_list(numbers):
                safe_report.append(numbers)
            elif try_removals(numbers):
                safe_report.append(numbers)
            else:
                unsafe_report.append(numbers)

    return safe_report, unsafe_report


file_path = "input2.txt"
safe, unsafe = get_safe_report(file_path)
print(f"Safe reports: {len(safe)}")
print(f"Unsafe reports: {len(unsafe)}")
