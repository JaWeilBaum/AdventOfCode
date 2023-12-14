from aoc import Day


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

    def part_two(self, raw_data: str) -> str:
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


if __name__ == '__main__':
    Day14().run(True, False, True)