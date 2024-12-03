#!/usr/bin/env python3


def get_safe_report(file_path):
    """
    Get the total number of reports that are safe in the provided file.
    Each line contains a sequence of numbers separated by spaces.
    A report is considered safe if the levels are either  increasing or
    decreasing, and every adjacent pair of numbers differs by at
    least 1 and at most 3.
    """
    safe_report = []
    unsafe_report = []

    with open(file_path, "r") as file:
        for line in file:
            parts = line.split()
            if len(parts) < 2:
                unsafe_report.append(line.strip())
                continue

            numbers = [int(n) for n in parts]
            print(numbers)

            safe = True
            increasing = True

            for i in range(1, len(numbers)):
                if i == 1:
                    diff = numbers[i] - numbers[i - 1]
                    if diff < 0:
                        increasing = False
                    elif diff > 0:
                        increasing = True
                diff = numbers[i] - numbers[i - 1]

                if diff > 0 and increasing is False:
                    safe = False
                    break
                elif diff < 0 and increasing is True:
                    safe = False
                    break

                if diff < 0:
                    diff = -diff
                print(diff)

                if diff < 1 or diff > 3:
                    safe = False
                    break
                safe = True

            if safe is True:
                safe_report.append(numbers)
            else:
                unsafe_report.append(numbers)

    return safe_report, unsafe_report


file_path = "input1.txt"

safe, unsafe = get_safe_report(file_path)
print(f"Safe reports: {len(safe)}")
print(f"Unsafe reports: {len(unsafe)}")
