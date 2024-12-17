#!/usr/bin/env python3

from math import gcd

def parse_map(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

def find_frequencies(grid):
    frequencies = {}
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            freq = grid[i][j]
            if freq == '.' or freq == '#':
                continue
            if freq not in frequencies:
                frequencies[freq] = []
            frequencies[freq].append((i, j))
    return frequencies

def compute_directional_positions_single(origin, dx, dy, max_x, max_y):
    ox, oy = origin
    diff = gcd(dx, dy)
    xd, yd = dx // diff, dy // diff

    positions = []
    step = 1
    while 0 <= ox + xd * step < max_x and 0 <= oy + yd * step < max_y:
        positions.append((ox + xd * step, oy + yd * step))
        step += 1
    return positions

def compute_antinodes_fixed(origin, others, max_x, max_y):
    direct_nodes = []
    extended_nodes = set()
    ox, oy = origin

    for tx, ty in others:
        dx, dy = tx - ox, ty - oy

        if 0 <= ox - dx < max_x and 0 <= oy - dy < max_y:
            direct_nodes.append((ox - dx, oy - dy))
        if 0 <= tx + dx < max_x and 0 <= ty + dy < max_y:
            direct_nodes.append((tx + dx, ty + dy))

        extended_nodes.update(compute_directional_positions_single((ox, oy), -dx, -dy, max_x, max_y))
        extended_nodes.update(compute_directional_positions_single((tx, ty), dx, dy, max_x, max_y))
        extended_nodes.update(compute_directional_positions_single((ox, oy), dx, dy, max_x, max_y))
        extended_nodes.update(compute_directional_positions_single((tx, ty), -dx, -dy, max_x, max_y))

    return direct_nodes, list(extended_nodes)

def find_all_antinodes(grid):
    frequencies = find_frequencies(grid)
    size_x, size_y = len(grid), len(grid[0])

    direct_antinodes = []
    extended_antinodes = []

    for freq, positions in frequencies.items():
        for i in range(len(positions) - 1):
            direct, extended = compute_antinodes_fixed(positions[i], positions[i + 1:], size_x, size_y)
            direct_antinodes += direct
            extended_antinodes += extended

    return direct_antinodes, extended_antinodes

def unique_positions(positions):
    return set(f"{x}|{y}" for x, y in positions)

def main():
    file_path = "input1.txt"  # Replace with your actual input file
    grid = parse_map(file_path)

    direct_antinodes, extended_antinodes = find_all_antinodes(grid)

    unique_direct = unique_positions(direct_antinodes)
    unique_extended = unique_positions(extended_antinodes)

    print(len(unique_direct))
    print(len(unique_extended))

if __name__ == "__main__":
    main()

