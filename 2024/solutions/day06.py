from functools import cmp_to_key

from fontTools.misc.psOperators import ps_object
from mpmath import matrix
from s3transfer.compat import seekable

from aoc import Day

class Day06(Day):

    def __init__(self):
        super().__init__(year=2024, day=6)
        self.grid = {}

    def _create_grid(self, data: str):
        self.grid = {
            y+x*1j: value for y, row in enumerate(data.splitlines()) for x, value in enumerate(row.strip())
        }

    def part_one(self, data: str):
        self._create_grid(data)

        visited_locations = self._walk_grid(self.grid)[0]

        return f"{len(visited_locations)}"

    def _get_start_location(self):
        return min(loc for loc in self.grid if self.grid[loc] == "^")

    def _walk_grid(self, grid: dict) -> (set, bool):
        start_loc = self._get_start_location()

        direction = -1  # UP
        dir_change = -1j  # Turn Right
        position = start_loc
        visited_locs = set()

        while position in grid and (position, direction) not in visited_locs:
            visited_locs.add((position, direction))
            if grid.get(position + direction) == "#":
                direction *= dir_change
            else:
                position += direction

        return {loc for loc, _ in visited_locs}, (position, direction) in visited_locs

    def part_two(self, data: str):
        self._create_grid(data)
        visited_locs = self._walk_grid(self.grid)[0]
        start_loc = self._get_start_location()

        results = []

        for possible_loc in visited_locs:
            if possible_loc == start_loc:
                continue
            _g = self.grid.copy()
            _g[possible_loc] = '#'
            results.append(self._walk_grid(_g)[1])

        return f"{sum(results)}"

if __name__ == '__main__':
    Day06().run(demo=False, part_one=False, part_two=True)
