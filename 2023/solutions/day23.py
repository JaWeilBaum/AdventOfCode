from copy import copy

from aoc import Day


class Day23(Day):

    def __init__(self):
        super().__init__(23)

    def part_one(self, raw_data: str) -> str:
        grid = [list(row) for row in raw_data.splitlines()]
        start = (1, 0)
        goal = (len(grid[0]) - 2, len(grid) - 1)

        routes = [(*start, 'd', set())]
        oppo = {'l': 'r', 'r': 'l', 'u': 'd', 'd': 'u'}
        _dir = {'>': 'l', '<': 'r', 'v': 'd', '^': 'u'}
        while len(routes) > 0:
            c_x, c_y, c_d, visited_locations = routes.pop()
            next_locations = []
            if (c_x, c_y) == goal:
                print(len(visited_locations))
                break
            for _x, _y, _d in [(0, 1, 'd'), (1, 0, 'r'), (0, -1, 'u'), (-1, 0, 'l')]:
                n_x = c_x + _x
                n_y = c_y + _y
                if 0 <= n_x < len(grid[0]) and 0 <= n_y < len(grid):
                    if grid[n_y][n_x] in '.<>v^' and oppo[c_d] != _d and (n_x, n_y) not in visited_locations:
                        # if grid[n_y][n_x] in '<>v^' and _d == _dir[grid[n_y][n_x]] or (grid[n_y][n_x] == '.'):
                        next_locations.append((n_x, n_y, _d))

            if len(next_locations) == 1:
                routes.append((*next_locations[0], visited_locations.union({(c_x, c_y)})))
            else:
                for x, y, d in next_locations:
                    routes.append((x, y, d, copy(visited_locations).union({(c_x, c_y)})))
            # print()

            routes.sort(key=lambda x: len(x[-1]))


        pass


    def part_two(self, raw_data: str) -> str:
        pass


if __name__ == '__main__':
    Day23().run(True, True, False)