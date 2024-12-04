#!/usr/bin/env python3


def count_word_occurrences(grid, word):
    rows = len(grid)
    cols = len(grid[0])
    word_length = len(word)
    directions = [
        (0, 1),
        (1, 0),
        (1, 1),
        (1, -1),
        (0, -1),
        (-1, 0),
        (-1, -1),
        (-1, 1)
    ]

    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols

    def check_direction(x, y, dx, dy):
        for i in range(word_length):
            nx, ny = x + i * dx, y + i * dy
            if not is_valid(nx, ny) or grid[nx][ny] != word[i]:
                return False
        return True

    count = 0
    for x in range(rows):
        for y in range(cols):
            for dx, dy in directions:
                if check_direction(x, y, dx, dy):
                    count += 1
    return count


def read_grid_from_file(filename):
    with open(filename, 'r') as file:
        return [list(line.strip()) for line in file.readlines()]


filename = "input1.txt"

word = "XMAS"

grid = read_grid_from_file(filename)

result = count_word_occurrences(grid, word)
print(f"The word '{word}' appears {result} times.")
