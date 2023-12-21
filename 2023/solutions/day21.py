import datetime
import numpy as np
from aoc import Day


class Day21(Day):

    def __init__(self):
        super().__init__(21)

    def print_grid(self, grid: list, marked_tiles: list, rocks: list):
        for row_idx in range(len(grid)):
            for col_idx in range(len(grid[0])):
                if (col_idx, row_idx) in marked_tiles:
                    print('O', end="")
                elif (col_idx, row_idx) in rocks:
                    print('#', end="")
                else:
                    print('_', end="")
            print()

    def part_one(self, raw_data: str) -> str:
        grid = [list(row) for row in raw_data.splitlines()]

        garden_plots = []
        rocks = []

        x, y = -1, -1

        for row_idx, row in enumerate(grid):
            for col_idx, value in enumerate(row):
                if value == 'S':
                    x, y = col_idx, row_idx
                elif value == '.':
                    garden_plots.append((col_idx, row_idx))
                elif value == '#':
                    rocks.append((col_idx, row_idx))

        return str(self.fast(grid, len(grid), x, y, [64])[0])


    def fast(self, grid: list, size: int, x: int, y: int, values: list) -> list:
        recorded_nodes = {}
        marked_tiles = [(x, y)]

        v = []
        _v = []
        for i in range(max(values) + 1):

            new_marked_tiles = []
            for x, y in marked_tiles:
                if (x, y) not in recorded_nodes:
                    recorded_nodes[(x, y)] = i % 2
                for _x, _y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    tmp_x = x + _x
                    tmp_y = y + _y
                    if grid[tmp_y % size][tmp_x % size] != '#' and (tmp_x, tmp_y) not in new_marked_tiles and (tmp_x, tmp_y) not in recorded_nodes:
                        new_marked_tiles.append((tmp_x, tmp_y))

            marked_tiles = new_marked_tiles
            if i in values:
                v.append(len(list(filter(lambda x: x == i % 2, recorded_nodes.values()))))
        return v

    def part_two(self, raw_data: str) -> str:
        grid = [list(row) for row in raw_data.splitlines()]

        garden_plots = []
        rocks = []

        x, y = -1, -1

        for row_idx, row in enumerate(grid):
            for col_idx, value in enumerate(row):
                if value == 'S':
                    x, y = col_idx, row_idx
                elif value == '.':
                    garden_plots.append((col_idx, row_idx))
                elif value == '#':
                    rocks.append((col_idx, row_idx))

        y_values = self.fast(grid, len(grid), x, y, [65, 65 + 131, 65 + 262])

        n = 26501365 // len(grid)
        poly = np.rint(np.polynomial.polynomial.polyfit([0, 1, 2], y_values, 2)).astype(int).tolist()

        return str(sum(poly[i] * n ** i for i in range(3)))


if __name__ == '__main__':
    Day21().run(False, True, True)