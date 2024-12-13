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
        corner_stones = [
            ([ 1, -1j],  1 -1j),
            ([-1, -1j], -1 -1j),
            ([-1,  1j], -1 +1j),
            ([ 1,  1j],  1 +1j),
        ]

        output_fences = {}

        for element in elements:

            for direction, fence_letter in directions:
                new_pos = element + direction
                if (new_pos not in elements):
                    output_fences[(new_pos * factor) - direction] = fence_letter

                for check_locations, corner_stone_location in corner_stones:
                    if all([(element + d not in elements) for d in check_locations]):
                        output_fences[(element * factor) + corner_stone_location] = '+'


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

    def get_grid_rows(self, grid: dict, rows: bool=False, columns: bool=False) -> int:
        min_x, min_y, max_x, max_y = self.grid_size(grid)

        data = []

        for y in range(min_y, max_y):
            row = []
            for x in range(min_x, max_x):
                loc = y + x*1j
                if value := grid.get(loc):
                    row.append(value)
                else:
                    row.append(' ')
            data.append(row)

        if rows:
            new_data = [''.join(row).strip().split('+') for row in data]
        if columns:
            new_data = []
            for col_idx in range(len(data[0])):
                new_row = []
                for row_idx in range(len(data)):
                    new_row.append(data[row_idx][col_idx])
                new_data.append(''.join(new_row).strip().split('+'))

        fences = []
        for row in new_data:
            for element in row:
                if len(element.strip()) == 0:
                    continue
                potential_elements = element.split('  ')
                for p_element in potential_elements:
                    if len(p_element.strip()) == 0:
                        continue
                    fences.append(p_element.strip())

        return len(fences)


    def part_one(self, data: str):

        grid = self.create_grid(data)
        fields = self.discover_fields(grid)

        price = []

        for key, vals in fields.items():
            for val in vals:
                price.append(len(val) * self.calculate_perimeter(val))

        return f"{sum(price)}"

    def num_fences(self, fence: dict) -> int:
        row_walls = self.get_grid_rows({k: v for k, v in fence.items() if v in ['-', '+']}, rows=True)
        col_walls = self.get_grid_rows({k: v for k, v in fence.items() if v in ['|', '+']}, columns=True)
        return row_walls + col_walls

    def part_two(self, data: str):

        grid = self.create_grid(data)
        fields = self.discover_fields(grid)

        price = []

        for key, vals in fields.items():
            for val in vals:
                fence = self.create_fences(val, factor=2)
                num_fences = self.num_fences(fence)
                price.append(len(val) * num_fences)

        return f"{sum(price)}"


if __name__ == '__main__':
    Day12().run(demo=True, part_one=False, part_two=True)
