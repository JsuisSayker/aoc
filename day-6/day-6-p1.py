#!/usr/bin/env python3
def predict_guard_path_from_file(filename):
    with open(filename, 'r') as file:
        grid = [line.strip() for line in file if line.strip()]

    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    direction_index = 0
    visited_positions = set()

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
                grid[r] = grid[r][:c] + '.' + grid[r][c+1:]
                break

    row, col = start_row, start_col
    visited_positions.add((row, col))

    while 0 <= row < len(grid) and 0 <= col < len(grid[0]):
        next_row, next_col = row + directions[
            direction_index][0], col + directions[direction_index][1]

        if 0 <= next_row < len(grid) and 0 <= next_col < len(
                grid[0]) and grid[next_row][next_col] == "#":
            direction_index = (direction_index + 1) % 4
        else:
            row, col = next_row, next_col
            if 0 <= row < len(grid) and 0 <= col < len(grid[0]):
                visited_positions.add((row, col))
            else:
                break

    return len(visited_positions)


filename = "input1.txt"
result = predict_guard_path_from_file(filename)
print(result)
