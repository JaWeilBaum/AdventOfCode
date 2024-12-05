from functools import cmp_to_key
from aoc import Day

class Day04(Day):

    def __init__(self):
        super().__init__(year=2024, day=4)
        self.matrix = None
        self.letter = "XMAS"
    # XMAS

    def _valid_coords(self, x, y) -> bool:
        return 0 <= y < len(self.matrix) and 0 <= x < len(self.matrix[y])

    def _vertical(self, x, y) -> int:
        x_diff = [0, 0, 0, 0]
        y_diff = [0, 1, 2, 3]
        y_diff_rev = [0, -1, -2, -3]
        return sum(list(map(int, [
            self._validate_seq(x, y, x_diff, y_diff),
            self._validate_seq(x, y, x_diff, y_diff_rev)
        ])))


    def _horizontal(self, x, y) -> int:
        x_diff = [0, 1, 2, 3]
        x_diff_rev = [0, -1, -2, -3]
        y_diff = [0, 0, 0, 0]
        return sum(list(map(int, [
            self._validate_seq(x, y, x_diff, y_diff),
            self._validate_seq(x, y, x_diff_rev, y_diff)
        ])))

    def _left_up_right_down(self, x, y) -> int:
        x_diff = [0, 1, 2, 3]
        x_diff_rev = [0, -1, -2, -3]
        y_diff = [0, 1, 2, 3]
        y_diff_rev = [0, -1, -2, -3]
        return sum(list(map(int, [
            self._validate_seq(x, y, x_diff, y_diff),
            self._validate_seq(x, y, x_diff_rev, y_diff_rev)
        ])))

    def _left_down_right_up(self, x, y) -> int:
        x_diff = [0, 1, 2, 3]
        x_diff_rev = [0, -1, -2, -3]
        y_diff = [0, -1, -2, -3]
        y_diff_rev = [0, 1, 2, 3]
        return sum(list(map(int, [
            self._validate_seq(x, y, x_diff, y_diff),
            self._validate_seq(x, y, x_diff_rev, y_diff_rev)
        ])))

    def _validate_seq(self, x, y, x_diff, y_diff) -> bool:
        for _x, _y, letter in zip(x_diff, y_diff, self.letter):
            if not self._valid_coords(x + _x, y + _y):
                return False

            if self.matrix[y + _y][x + _x] != letter:
                return False

        return True


    def part_one(self, data: str):
        self.matrix = [list(x) for x in data.splitlines()]

        found_xmas = 0

        for y in range(len(self.matrix)):
            for x in range(len(self.matrix[y])):
                found_at_coord = sum([
                    self._horizontal(x, y),
                    self._vertical(x, y),
                    self._left_up_right_down(x, y),
                    self._left_down_right_up(x, y)
                ])
                found_xmas += found_at_coord

        return f"{found_xmas}"

    def _mas_0_deg(self, x, y) -> bool:
        letters = [
            'M', '.', 'S',
            '.', 'A', '.',
            'M', '.', 'S'
        ]
        return self._validate_matrix(x, y, letters)

    def _mas_90_deg(self, x, y) -> bool:
        letters = [
            'M', '.', 'M',
            '.', 'A', '.',
            'S', '.', 'S'
        ]
        return self._validate_matrix(x, y, letters)

    def _mas_180_deg(self, x, y) -> bool:
        letters = [
            'S', '.', 'M',
            '.', 'A', '.',
            'S', '.', 'M'
        ]
        return self._validate_matrix(x, y, letters)

    def _mas_270_deg(self, x, y) -> bool:
        letters = [
            'S', '.', 'S',
            '.', 'A', '.',
            'M', '.', 'M'
        ]
        return self._validate_matrix(x, y, letters)

    def _validate_matrix(self, x, y, matrix) -> bool:
        x_diff = [0, 1, 2] * 3
        y_diff = [0] * 3 + [1] * 3 + [2] * 3
        for _x, _y, letter in zip(x_diff, y_diff, matrix):
            if letter == '.':
                continue
            if not self._valid_coords(x + _x, y + _y):
                return False

            if self.matrix[y + _y][x + _x] != letter:
                return False

        return True

    def part_two(self, data: str):
        self.matrix = [list(x) for x in data.splitlines()]

        found_xmas = 0

        for y in range(len(self.matrix)):
            for x in range(len(self.matrix[y])):
                found_at_coord = sum(list(map(int, [
                    self._mas_0_deg(x, y),
                    self._mas_90_deg(x, y),
                    self._mas_180_deg(x, y),
                    self._mas_270_deg(x, y),
                ])))
                found_xmas += found_at_coord

        return f"{found_xmas}"

if __name__ == '__main__':
    Day04().run(demo=False, part_one=False, part_two=True)
