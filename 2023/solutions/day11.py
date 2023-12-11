from aoc import Day


class Day11(Day):

    def __init__(self):
        super().__init__(11)

    def part_one(self, raw_data: str) -> str:
        matrix = [list(row) for row in raw_data.split()]

        locations = []
        col_no_galaxy = []
        row_no_galaxy = []

        for x in range(len(matrix[0])):
            column = list(map(lambda row: row[x], matrix))
            galaxies = list(filter(lambda element: element == '#', column))
            if len(galaxies) == 0:
                col_no_galaxy.append(x)

        for y in range(len(matrix)):
            galaxies = list(filter(lambda element: element == '#', matrix[y]))
            if len(galaxies) == 0:
                row_no_galaxy.append(y)

        for y in range(len(matrix)):
            for x in range(len(matrix[y])):
                if matrix[y][x] == '#':
                    x_add = len(list(filter(lambda z: z <= x, col_no_galaxy)))
                    y_add = len(list(filter(lambda z: z <= y, row_no_galaxy)))
                    locations.append((x + x_add, y + y_add))

        distances = []
        for loc_1_x, loc_1_y in locations:
            for loc_2_x, loc_2_y in locations:
                distances.append(abs(loc_1_x - loc_2_x) + abs(loc_1_y - loc_2_y))
        return str(sum(distances) / 2)

    def part_two(self, raw_data: str) -> str:
        matrix = [list(row) for row in raw_data.split()]

        locations = []
        col_no_galaxy = []
        row_no_galaxy = []

        for x in range(len(matrix[0])):
            column = list(map(lambda row: row[x], matrix))
            galaxies = list(filter(lambda element: element == '#', column))
            if len(galaxies) == 0:
                col_no_galaxy.append(x)

        for y in range(len(matrix)):
            galaxies = list(filter(lambda element: element == '#', matrix[y]))
            if len(galaxies) == 0:
                row_no_galaxy.append(y)

        for y in range(len(matrix)):
            for x in range(len(matrix[y])):
                if matrix[y][x] == '#':
                    x_add = len(list(filter(lambda z: z <= x, col_no_galaxy)))
                    y_add = len(list(filter(lambda z: z <= y, row_no_galaxy)))
                    locations.append((x + x_add * (1_000_000 - 1), y + y_add * (1_000_000 - 1)))

        distances = []
        for loc_1_x, loc_1_y in locations:
            for loc_2_x, loc_2_y in locations:
                distances.append(abs(loc_1_x - loc_2_x) + abs(loc_1_y - loc_2_y))
        return str(sum(distances) / 2)

        pass


if __name__ == '__main__':
    Day11().run(False, False, True)