from anyio import value
from pandas import Flags

from aoc import Day


class Day12(Day):

    def __init__(self):
        super().__init__(year=2024, day=12)

    def create_grid(self, data: str) -> dict:
        return {
            y + x * 1j: value for y, row in enumerate(data.splitlines())
            for x, value in enumerate(row.strip())
        }

    def discover_fields(self, grid: dict) -> dict:
        directions = [1, -1, 1j, -1j]
        all_fields = [x for x in grid.keys()]

        store = {}

        while len(all_fields) > 0:
            start_field = all_fields.pop(0)
            fields_to_visit = [start_field]
            field_letter = grid[start_field]

            discovered_fields = []

            while len(fields_to_visit) > 0:
                current_field = fields_to_visit.pop(0)
                discovered_fields.append(current_field)

                valid_neighbours = []

                for direction in directions:
                    potential_location = current_field + direction
                    if ((potential_location in grid) and
                            (potential_location in all_fields) and
                            (grid[potential_location] == field_letter)):
                        valid_neighbours.append(potential_location)
                        all_fields.remove(potential_location)

                fields_to_visit.extend(valid_neighbours)

            if field_letter in store:
                store[field_letter].append(discovered_fields)
            else:
                store[field_letter] = [discovered_fields]

        return store

    def calculate_perimeter(self, field: list) -> int:
        directions = [1, -1, 1j, -1j]
        total_perimeter = 0
        for element in field:
            found_neighbours = [
                element + direction for direction in directions
                if (element + direction in field)
            ]
            total_perimeter += 4 - len(found_neighbours)
        return total_perimeter

    def create_fences(self, elements: dict, factor: int = 2) -> dict:
        directions = [(1, '-'), (-1, '-'), (1j, '|'), (-1j, '|')]


        output_fences = {}

        for element in elements:

            for direction, fence_letter in directions:
                new_pos = element + direction
                if (new_pos not in elements):
                    output_fences[(new_pos * factor) - direction] = fence_letter

        return output_fences

    def grid_size(self, grid: dict) -> (int, int, int, int):
        return (int(min(map(lambda x: x.imag, grid.keys()))),
                int(min(map(lambda x: x.real, grid.keys()))),
                int(max(map(lambda x: x.imag, grid.keys()))) + 1,
                int(max(map(lambda x: x.real, grid.keys()))) + 1)

    def print_grid(self, grid: dict, filter_x: bool = False, filter_y: bool = False) -> None:
        min_x, min_y, max_x, max_y = self.grid_size(grid)

        for y in range(min_y, max_y):
            if y % 2 != 0 and filter_y:
                continue
            for x in range(min_x, max_x):
                if x % 2 != 0 and filter_x:
                    continue
                loc = y + x*1j
                if value := grid.get(loc):
                    print(value, end="")
                else:
                    print(".", end="")

            print()

    def part_one(self, data: str):

        grid = self.create_grid(data)
        fields = self.discover_fields(grid)

        price = []

        for key, vals in fields.items():
            for val in vals:
                price.append(len(val) * self.calculate_perimeter(val))

        return f"{sum(price)}"

    def consolidate_fences(self, fences: dict) -> int:
        fences_locations = [x for x in fences.items()]

        expected_element = {
            "-": [1j, -1j],
            "|": [ 1,  -1]
        }

        c_fences = []

        while len(fences_locations) > 0:
            location, direction  = fences_locations.pop(0)
            tmp_c_fence = [location]
            for diff in expected_element[direction]:
                new_element_found = True
                counter = 1
                while new_element_found:
                    new_element_found = False
                    potential_location = location + (counter * diff * 2)
                    if (potential_location in fences) and (direction == fences[potential_location]):
                        tmp_c_fence.append(potential_location)
                        fences_locations.remove((potential_location, direction))
                        new_element_found = True
                    counter += 1
            c_fences.append(tmp_c_fence)

        return len(c_fences)

    def part_two(self, data: str):
        data = """AAAAAA
AAABBA
AAABBA
ABBAAA
ABBAAA
AAAAAA"""
        grid = self.create_grid(data)
        fields = self.discover_fields(grid)
        print()

        price = []

        A_field = fields["A"][0]

        fence = self.create_fences(A_field, factor=2)
        self.print_grid({x: "A" for x in A_field})
        print()
        self.print_grid({k: v for k,v in fence.items() if v == '|'}, filter_y=True)
        print()
        self.print_grid({k: v for k,v in fence.items() if v == '-'}, filter_x=True)

        # Filter the expanded filed and in the other direction of fences
        # For every row / column count the number of fences which are there


        for key, vals in fields.items():
            for val in vals:
                fences = self.create_fences(val)
                num_fences = self.consolidate_fences(fences)

                print(f"{key} {len(val) * num_fences} ({num_fences=})")
                price.append(len(val) * num_fences)

        print()
        return f"{sum(price)}"
    # In the example above the walls are consolidated which should not be consolidated.
    #
    # A |
    # A v
    # - + -
    #   ^ A
    #   | A
    # 835520 -> too low

if __name__ == '__main__':
    Day12().run(demo=False, part_one=False, part_two=True)
