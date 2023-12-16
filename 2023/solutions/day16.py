from aoc import Day
from tqdm import tqdm

class Day16(Day):

    def __init__(self):
        super().__init__(16)
        self.grid = None

    def next_coord_from_direction(self, direction: str, x: int, y: int) -> (int, int):
        if direction == 'R':
            return x + 1, y
        elif direction == 'L':
            return x - 1, y
        elif direction == 'D':
            return x, y + 1
        elif direction == 'U':
            return x, y - 1

    def move_beam(self, direction: str, x: int, y: int) -> list[(str, int, int)]:
        tile_value = self.grid[y][x]
        if tile_value == '.' or (tile_value == '-' and direction in 'RL') or (tile_value == '|' and direction in 'UD'):
            return [(direction, *self.next_coord_from_direction(direction, x, y))]
        elif tile_value == '|':
            return [
                ('U', *self.next_coord_from_direction('U', x, y)),
                ('D', *self.next_coord_from_direction('D', x, y))
            ]
        elif tile_value == '-':
            return [
                ('L', *self.next_coord_from_direction('L', x, y)),
                ('R', *self.next_coord_from_direction('R', x, y))
            ]
        elif tile_value == '\\':
            if direction == 'R':
                return [('D', *self.next_coord_from_direction('D', x, y))]
            elif direction == 'L':
                return [('U', *self.next_coord_from_direction('U', x, y))]
            elif direction == 'D':
                return [('R', *self.next_coord_from_direction('R', x, y))]
            elif direction == 'U':
                return [('L', *self.next_coord_from_direction('L', x, y))]
        elif tile_value == '/':
            if direction == 'R':
                return [('U', *self.next_coord_from_direction('U', x, y))]
            elif direction == 'L':
                return [('D', *self.next_coord_from_direction('D', x, y))]
            elif direction == 'D':
                return [('L', *self.next_coord_from_direction('L', x, y))]
            elif direction == 'U':
                return [('R', *self.next_coord_from_direction('R', x, y))]
        return []

    def calc_energy(self, start_dir, start_x, start_y) -> int:
        visited_locations = []
        beams = [(start_dir, start_x, start_y)]
        while len(beams) > 0:
            b_dir, b_x, b_y = beams.pop()

            visited_locations.append((b_dir, b_x, b_y))

            result = self.move_beam(b_dir, b_x, b_y)

            result = list(filter(lambda x: 0 <= x[1] < len(self.grid) and 0 <= x[2] < len(self.grid[0]) and x not in visited_locations, result))
            beams.extend(result)
        return len(set(list(map(lambda x: (x[1], x[2]), visited_locations))))

    def part_one(self, raw_data: str) -> str:
        self.grid = [list(row) for row in raw_data.splitlines()]

        return str(self.calc_energy('R', 0 ,0))

    def part_two(self, raw_data: str) -> str:
        self.grid = [list(row) for row in raw_data.splitlines()]
        start_locations = [('R', 0, y) for y in range(len(self.grid))]
        start_locations += [('L', len(self.grid) - 1, y) for y in range(len(self.grid))]
        start_locations += [('D', x, 0) for x in range(len(self.grid[0]))]
        start_locations += [('U', x, len(self.grid[0]) - 1) for x in range(len(self.grid[0]))]

        values = []

        for start_loc, start_x, start_y in tqdm(start_locations):
            values.append(self.calc_energy(start_loc, start_x, start_y))

        return str(max(values))


if __name__ == '__main__':
    Day16().run(False, False,True)