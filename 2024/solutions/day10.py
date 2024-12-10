from aoc import Day


class Day10(Day):

    def __init__(self):
        super().__init__(year=2024, day=10)

    def _create_grid(self, data: str) -> dict:
        return {
            y+x*1j: int(value) for y, row in enumerate(data.splitlines())
                          for x, value in enumerate(row.strip())
        }

    def _walk_grid(self, grid: dict, start_location: complex) -> list:
        possible_dirs = [1, -1, 1j, -1j]
        todos = [[start_location]]
        finished_paths = []
        while len(todos) > 0:
            path = todos.pop()

            last_location = path[-1]
            last_value = grid[last_location]

            if last_value == 9:
                finished_paths.append(path)

            possible_neighbors = [
                last_location + possible_dir
                for possible_dir in possible_dirs
                if last_location + possible_dir in grid and last_value + 1 == grid[last_location + possible_dir]
            ]

            if len(possible_neighbors) > 0:
                todos.extend([
                    path + [possible_neighbor] for possible_neighbor in possible_neighbors
                ])

        return finished_paths


    def part_one(self, data: str):
        grid = self._create_grid(data)

        trail_heads = list(map(lambda x: x[0], list(filter(lambda item: item[1] == 0, grid.items()))))

        total_tails = []

        for trail_head in trail_heads:
            paths = self._walk_grid(grid, trail_head)
            tails = []
            for path in paths:
                if path[-1] not in tails:
                    tails.append(path[-1])
            total_tails.append(len(tails))
        return f"{sum(total_tails)}"

    def part_two(self, data: str):
        grid = self._create_grid(data)

        trail_heads = list(map(lambda x: x[0], list(filter(lambda item: item[1] == 0, grid.items()))))

        num_paths = []

        for trail_head in trail_heads:
            paths = self._walk_grid(grid, trail_head)

            num_paths.append(len(paths))
        return f"{sum(num_paths)}"



if __name__ == '__main__':
    Day10().run(demo=False, part_one=True, part_two=True)
