from itertools import combinations

from prometheus_client.decorator import append

from aoc import Day

class Day08(Day):

    def __init__(self):
        super().__init__(year=2024, day=8)

    def _create_grid(self, data: str) -> dict:
        return {
            y+x*1j: value for y, row in enumerate(data.splitlines())
                          for x, value in enumerate(row.strip())
        }

    def _get_antenna_locations(self, grid: dict) -> dict:
        antennas = {}

        for loc, name in grid.items():
            if name == '.':
                continue

            if name not in antennas:
                antennas[name] = [loc]
            else:
                antennas[name].append(loc)

        return antennas

    def grid_size(self, grid: dict) -> (int, int):
        return int(max(map(lambda x: x.imag, grid.keys()))) + 1, int(max(map(lambda x: x.real, grid.keys()))) + 1

    def print_grid(self, grid: dict, an_locations: list):
        max_x, max_y = self.grid_size(grid)

        for y in range(max_y):
            for x in range(max_x):
                loc = y + x*1j
                if loc in an_locations:
                    print("#", end="")
                else:
                    print(grid[loc], end="")

            print()

    def part_one(self, data: str):
        grid = self._create_grid(data)

        an_locations = self._find_all_antinodes(grid, 1)

        return f"{len(an_locations)}"

    def _find_all_antinodes(self, grid: dict, distance: int) -> list:
        antennas = self._get_antenna_locations(grid)

        distance_list = [1]
        if distance != 1:
            distance_list = list(range(distance))

        an_locations = []

        for antenna_name, locations in antennas.items():
            for a_1, a_2 in combinations(locations, 2):
                vector_between = a_1 - a_2

                for multiplier in distance_list:
                    a_1_extension = a_1 + (multiplier * vector_between)
                    if a_1_extension not in an_locations and a_1_extension in grid:
                        an_locations.append(a_1_extension)

                    if a_1_extension not in grid: # Early exit 
                        break

                for multiplier in distance_list:
                    a_2_extension = a_2 - (multiplier * vector_between)

                    if a_2_extension not in an_locations and a_2_extension in grid:
                        an_locations.append(a_2_extension)

                    if a_2_extension not in grid: # Early exit
                        break

        return an_locations

    def part_two(self, data: str):
        grid = self._create_grid(data)
        max_x, max_y = self.grid_size(grid)

        an_locations = self._find_all_antinodes(grid, max(max_x, max_y))

        return f"{len(an_locations)}"

if __name__ == '__main__':
    Day08().run(demo=False, part_one=True, part_two=True)
