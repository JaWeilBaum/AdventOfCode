from copy import copy
import networkx as nx
import matplotlib.pyplot as plt
from aoc import Day
from tqdm import tqdm


class Day23(Day):

    def __init__(self):
        super().__init__(23)

    def find_nodes(self, grid: list[list[str]]) -> dict:
        nodes = {}
        for row_idx, row in enumerate(grid):
            for col_idx, value in enumerate(row):
                if row_idx == 0 or col_idx == 0 or row_idx == len(grid) - 1 or col_idx == len(grid[0]) - 1:
                    continue

                possible_directions = []
                for _x, _y, _s, _d in [(0, 1, 'v', 'd'), (0, -1, '^', 'u'), (1, 0, '>', 'r'), (-1, 0, '<', 'l')]:
                    if grid[row_idx + _y][col_idx + _x] == _s:
                        possible_directions.append((col_idx + _x, row_idx + _y, _d))
                    elif grid[row_idx + _y][col_idx + _x] == '.':
                        possible_directions = []
                        break

                if len(possible_directions) > 0:
                    nodes[(col_idx, row_idx)] = possible_directions

        return nodes


    def walk_on_grid(self, x, y, d, grid, nodes):
        counter = 0
        move = True
        oppo = {'l': 'r', 'r': 'l', 'u': 'd', 'd': 'u'}
        _dir = {'<': 'l', '>': 'r', 'v': 'd', '^': 'u'}

        while move:
            counter += 1
            move = False
            for _x, _y, _d in [(0, 1, 'd'), (1, 0, 'r'), (0, -1, 'u'), (-1, 0, 'l')]:
                n_x = x + _x
                n_y = y + _y
                if 0 <= n_x < len(grid[0]) and 0 <= n_y < len(grid):
                    if grid[n_y][n_x] in '.<>v^' and oppo[d] != _d:
                        if (n_x, n_y) in nodes:
                            return counter + 1, (n_x, n_y)
                        elif grid[n_y][n_x] == '.':
                            x, y, d = n_x, n_y, _d
                            move = True
                            break
                        elif _dir[grid[n_y][n_x]] == _d:
                            x, y, d = n_x, n_y, _d
                            move = True
                            break

        return -1

        pass

    def create_graph(self, grid: list[list[str]], directed=True) -> nx.Graph:
        start = (1, 0)
        goal = (len(grid[0]) - 2, len(grid) - 1)

        _dir = {'<': 'l', '>': 'r', 'v': 'd', '^': 'u'}

        if directed:
            G = nx.DiGraph()
        else:
            G = nx.Graph()

        nodes = self.find_nodes(grid)

        nodes[start] = [(1, 1, 'd')]
        nodes[goal] = []

        for (x, y), possible_locations in nodes.items():
            for s_x, s_y, s_d in possible_locations:
                length, (n_x, n_y) = self.walk_on_grid(s_x, s_y, s_d, grid, nodes.keys())
                G.add_edge(f"{x},{y}", f"{n_x},{n_y}", weight=length)

        return G

    def part_one(self, raw_data: str) -> str:
        grid = [list(row) for row in raw_data.splitlines()]

        G = self.create_graph(grid)

        l_p = nx.dag_longest_path_length(G)

        return str(l_p)


    def part_two(self, raw_data: str) -> str:
        grid = [list(row) for row in raw_data.splitlines()]
        start = f"1,0"
        goal = f"{len(grid[0]) - 2},{len(grid) - 1}"

        G = self.create_graph(grid, directed=False)

        max_length = 0

        for path in tqdm(nx.all_simple_paths(G, start, goal)):
            new_length = nx.path_weight(G, path, weight="weight")
            max_length = max(max_length, new_length)
            if new_length == max_length:
                print(new_length)

        return str(max_length)


if __name__ == '__main__':
    Day23().run(False, False, True)