from functools import cmp_to_key

from mpmath import matrix

from aoc import Day

class Day06(Day):

    def __init__(self):
        super().__init__(year=2024, day=6)
        self.matrix = []

    def _find_start(self) -> (int, int):
        for y, row in enumerate(self.matrix):
            if "^" in row:
                return row.index("^"), y

    def _valid_coord(self, x, y) -> bool:
        return 0 <= y < len(self.matrix) and x < len(self.matrix[y])

    def part_one(self, data: str):
        self.matrix = [list(x) for x in data.splitlines()]

        s_x, s_y = self._find_start()

        directions = ["U", "R", "D", "L"]
        steps = [(0, -1), (1, 0), (0, 1), (-1, 0)]

        direction = directions[0]
        visited_locs = set()

        while True:
            print(s_x, s_y)
            visited_locs.add(f"{s_x}#{s_y}")
            _x, _y = steps[directions.index(direction)]
            if not self._valid_coord(s_x + _x, s_y + _y):
                break
            if self.matrix[_y + s_y][_x + s_x] == "#":
                direction = directions[(directions.index(direction) + 1) % len(directions)]
            else:
                s_x += _x
                s_y += _y

        return f"{len(visited_locs)}"

    def part_two(self, data: str):

        return f""

if __name__ == '__main__':
    Day06().run(demo=False, part_one=True, part_two=True)
