from aoc import Day
from tqdm import tqdm

class Day14(Day):

    def __init__(self):
        super().__init__(14)

    def get_columns(self, grid: list[list[str]]) -> list[list[str]]:
        columns = [[] for _ in range(len(grid[0]))]

        for row in grid:
            for col_idx in range(len(row)):
                columns[col_idx].append(row[col_idx])
        return columns

    def move_rocks_in_column(self, column: str) -> str:
        num_rocks = sum(list(map(lambda x: x == 'O', column)))
        num_empty = len(column) - num_rocks
        return "".join(['O'] * num_rocks + ['.'] * num_empty)

    def shift_column(self, column: list[str]) -> list[str]:
        col_str = "".join(column)
        sub_cols = col_str.split("#")
        new_sub_cols = []
        for sub_col in sub_cols:
            new_sub_cols.append(self.move_rocks_in_column(sub_col))
        return list('#'.join(new_sub_cols))

    def count_values_in_grid(self, grid: list[list[str]]) -> list[int]:
        values = []

        for row_idx, row in enumerate(reversed(grid)):
            num_rocks = sum(list(map(lambda x: x == 'O', row)))
            values.append((row_idx + 1) * num_rocks)

        return values

    def part_one(self, raw_data: str) -> str:
        grid = [list(row) for row in raw_data.splitlines()]
        columns = self.get_columns(grid)

        columns = [self.shift_column(column) for column in columns]
        new_grid = self.get_columns(columns)

        # [print(''.join(row)) for row in new_grid]

        values = []

        for row_idx, row in enumerate(reversed(new_grid)):
            num_rocks = sum(list(map(lambda x: x == 'O', row)))
            values.append((row_idx + 1) * num_rocks)

        return str(sum(values))

    def rotate_grid_90_deg_right(self, grid: list[list[str]]) -> list[list[str]]:
        """
        123
        456
        789

        369
        258
        147

        (0,0) -> (0,2)
        (1,0) -> (0,1)
        (2,0) -> (0,0)
        """
        new_grid = [['.'] * len(grid[0])  for _ in range(len(grid))]

        for row_idx, row in enumerate(reversed(grid)):
            for col_idx, value in enumerate(row):
                new_grid[col_idx][row_idx] = value
        return new_grid


    def perform_flow(self, grid: list[list[str]]) -> list[list[str]]:
        columns = [self.shift_column(column) for column in self.get_columns(grid)]
        return self.get_columns(columns)

    def roll(self, grid: list[list[str]]) -> list[list[str]]:
        n_row = len(grid)
        n_col = len(grid[0])

        for col_idx in range(n_col):
            # Double to move all
            for _ in range(n_row):
                for row_idx in range(n_row):
                    if grid[row_idx][col_idx] == 'O' and row_idx > 0 and grid[row_idx - 1][col_idx] == '.':
                        grid[row_idx][col_idx] = '.'
                        grid[row_idx - 1][col_idx] = 'O'
        return grid

    def part_two(self, raw_data: str) -> str:
        grid = [list(row) for row in raw_data.splitlines()]

        cache = {}
        itters = 1_000_000_000
        i = 0
        while i < itters:
            i += 1
            for _ in range(4):
                grid = self.perform_flow(grid)
                grid = self.rotate_grid_90_deg_right(grid)
            key = ''.join([''.join(row) for row in grid])

            if key in cache:
                cycle_length = i - cache[key]
                reps = (itters - i) // cycle_length
                i += reps * cycle_length
            cache[key] = i

        # [print(''.join(row)) for row in grid]

        values = self.count_values_in_grid(grid)

        return str(sum(values))


if __name__ == '__main__':
    Day14().run(False, True, True)