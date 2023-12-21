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

    def solve(self, rocks: list, size: int, x: int, y: int, values: list) -> list:
        marked_tiles = [(x, y)]

        v = []
        for i in range(max(values)):

            new_marked_tiles = []
            for x, y in marked_tiles:
                for _x, _y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    tmp_x = x + _x
                    tmp_y = y + _y
                    if (tmp_x % size, tmp_y % size) not in rocks and (tmp_x, tmp_y) not in new_marked_tiles:
                        new_marked_tiles.append((tmp_x, tmp_y))

            marked_tiles = new_marked_tiles
            if i + 1 in values:
                print(f"{i + 1} {len(marked_tiles)}")
                v.append(marked_tiles)
        return v

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

        return str(len(self.solve(rocks, len(grid), x, y, [64])[0]))


    def fast(self, rocks: list, size: int, x: int, y: int, values: list) -> list:
        marked_tiles = []
        new_marked_tiles = [(x, y)]

        v = []
        for i in range(1, max(values) + 1):
            new_nodes = []
            while len(new_marked_tiles) > 0:
                x, y = new_marked_tiles.pop()
                marked_tiles.append((x, y, ('e' if i % 2 != 0 else 'o')))
                for _x, _y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    tmp_x = x + _x
                    tmp_y = y + _y
                    if (tmp_x % size, tmp_y % size) not in rocks and len(list(filter(lambda x: x[0] == tmp_x and x[1] == tmp_y, marked_tiles))) == 0:
                        new_nodes.append((tmp_x, tmp_y))
                        # new_marked_tiles.append()
            new_marked_tiles = new_nodes
            if i + 1 in values:
                print(f"{i + 1} {len(marked_tiles)}")
                v.append(marked_tiles)
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

        print(self.fast(rocks, len(grid), x, y, [64, 65, 65 + len(grid), 65 + (len(grid) * 2)]))


if __name__ == '__main__':
    Day21().run(True, False, True)