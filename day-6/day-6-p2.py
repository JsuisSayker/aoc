#!/usr/bin/env python3

def count_obstruction_positions(filename):
    with open(filename, 'r') as file:
        grid = [list(line.strip()) for line in file if line.strip()]

    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    direction_index = 0

    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] in "^>v<":
                start_row, start_col = r, c
                if grid[r][c] == "^":
                    direction_index = 0
                elif grid[r][c] == ">":
                    direction_index = 1
                elif grid[r][c] == "v":
                    direction_index = 2
                elif grid[r][c] == "<":
                    direction_index = 3
                grid[r][c] = '.'
                break

    def simulate_with_obstruction(obstruction_row, obstruction_col):
        grid[obstruction_row][obstruction_col] = '#'

        row, col = start_row, start_col
        direction_index = 0
        visited_states = set()

        while True:
            state = (row, col, direction_index)
            if state in visited_states:
                grid[obstruction_row][obstruction_col] = '.'
                return True
            visited_states.add(state)

            next_row, next_col = row + directions[
                direction_index][0], col + directions[direction_index][1]

            if 0 <= next_row < len(grid) and 0 <= next_col < len(
                    grid[0]) and grid[next_row][next_col] == "#":
                direction_index = (direction_index + 1) % 4
            else:
                row, col = next_row, next_col
                if not (0 <= row < len(grid) and 0 <= col < len(grid[0])):
                    grid[obstruction_row][obstruction_col] = '.'
                    return False

    loop_positions = 0
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == '.':  # Only consider empty spaces
                if simulate_with_obstruction(r, c):
                    loop_positions += 1

    return loop_positions


filename = "input1.txt"
result = count_obstruction_positions(filename)
print(result)
