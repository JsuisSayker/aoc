#!/usr/bin/env python3

from collections import Counter


def similarity_score_from_file(file_path):
    """
    Calculate the similarity score between two lists provided in a file.
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

    # Count occurrences of each number in the right list
    right_count = Counter(right)

    # Calculate similarity score
    score = 0
    for num in left:
        score += num * right_count[num]

    return score


file_path = "input2.txt"


similarity_score = similarity_score_from_file(file_path)
print(f"Similarity score: {similarity_score}")
