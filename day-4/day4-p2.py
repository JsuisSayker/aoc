#!/usr/bin/env python3


def check_pattern(grid, i, j):
    directions = [
        ('horizontal', 0, 1),
        ('horizontal_reverse', 0, -1),
        ('vertical', 1, 0),
        ('vertical_reverse', -1, 0),
        ('diagonal_tl_br', 1, 1),
        ('diagonal_tr_bl', 1, -1),
        ('diagonal_reverse_tl_br', -1, 1),
        ('diagonal_reverse_tr_bl', -1, -1),
    ]

    def check_in_direction(i, j, di, dj, pattern):
        try:
            for k in range(4):
                if grid[i + k * di][j + k * dj] != pattern[k]:
                    return False
            return True
        except IndexError:
            return False

    # The pattern we're looking for is 'XMAS'
    pattern = "XMAS"
    count = 0

    # Check each direction
    for direction, di, dj in directions:
        if check_in_direction(i, j, di, dj, pattern):
            count += 1
        if check_in_direction(i, j, -di, -dj, pattern):
            count += 1

    return count


def cross_pattern(grid, i, j):
    return (
        (grid[i - 1][j - 1] == "M" and grid[i - 1][j + 1] == "S" and
         grid[i + 1][j - 1] == "M" and grid[i + 1][j + 1] == "S") or
        (grid[i - 1][j - 1] == "M" and grid[i - 1][j + 1] == "M" and
         grid[i + 1][j - 1] == "S" and grid[i + 1][j + 1] == "S") or
        (grid[i - 1][j - 1] == "S" and grid[i - 1][j + 1] == "M" and
         grid[i + 1][j - 1] == "S" and grid[i + 1][j + 1] == "M") or
        (grid[i - 1][j - 1] == "S" and grid[i - 1][j + 1] == "S" and
         grid[i + 1][j - 1] == "M" and grid[i + 1][j + 1] == "M")
    )


def count_cross_patterns(grid):
    cross_count = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(1, rows-1):
        for j in range(1, cols-1):
            # Check if the center is part of a valid "cross" pattern
            if grid[i][j] == "A" and cross_pattern(grid, i, j):
                cross_count += 1

    return cross_count


def read_grid_from_file(filename):
    with open(filename, 'r') as file:
        grid = [line.strip() for line in file if line.strip()]
    return grid


grid = read_grid_from_file("input1.txt")

cross_result = count_cross_patterns(grid)

print(cross_result)
