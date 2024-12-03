#!/usr/bin/env python3

def total_distance_from_file(file_path):
    """
    Calculate the total distance between two lists provided in a file.
    Each line contains two integers separated by spaces.
    """
    left = []
    right = []

    # Read the file and parse the numbers
    with open(file_path, "r") as file:
        for line in file:
            parts = line.split()
            if len(parts) != 2:
                raise ValueError(f"Invalid line format: {line.strip()}")

            # Append numbers to respective lists
            left.append(int(parts[0]))
            right.append(int(parts[1]))

    # Sort the lists
    left.sort()
    right.sort()

    # Calculate the total distance
    return sum(abs(l - r) for l, r in zip(left, right))


file_path = "input1.txt"


distance = total_distance_from_file(file_path)
print(f"Total distance: {distance}")
