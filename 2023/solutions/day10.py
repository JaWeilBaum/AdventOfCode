from aoc import Day


class Day10(Day):

    def __init__(self):
        super().__init__(10)
        self.grid = [[]]
        self.visited_nodes = []

    def get_possible_directions(self, x: int, y: int) -> (int, int, str):
        elements = []
        current_tile = self.grid[y][x]

        outgoing_directions = ""
        if current_tile == '|':
            outgoing_directions = 'UD'
        elif current_tile == '-':
            outgoing_directions = 'LR'
        elif current_tile == 'L':
            outgoing_directions = 'UR'
        elif current_tile == 'J':
            outgoing_directions = 'LU'
        elif current_tile == 'F':
            outgoing_directions = 'DR'
        elif current_tile == '7':
            outgoing_directions = 'DL'
        else:
            outgoing_directions = 'UDLR'

        if 'D' in outgoing_directions and y + 1 < len(self.grid) and self.grid[y + 1][x] in "|JLS":
            elements.append((x, y + 1, 'D'))
        if 'U' in outgoing_directions and y - 1 >= 0 and self.grid[y - 1][x] in "|F7S":
            elements.append((x, y - 1, 'U'))
        if 'R' in outgoing_directions and x + 1 < len(self.grid[y]) and self.grid[y][x + 1] in "-7JS":
            elements.append((x + 1, y, 'R'))
        if 'L' in outgoing_directions and x - 1 >= 0 and self.grid[y][x - 1] in "-FLS":
            elements.append((x - 1, y, 'L'))

        elements = list(filter(lambda x: (x[0], x[1]) not in list(map(lambda x: (x[0], x[1]), self.visited_nodes)), elements))

        if len(elements) == 0:
            return (None, None, '')
        return elements[0]

    def part_one(self, raw_data: str) -> str:
        self.grid = [list(x) for x in raw_data.splitlines()]

        x, y, current_direction = -1 , -1, ''

        for i, row in enumerate(self.grid):
            for j, element in enumerate(row):
                if element == 'S':
                    x = j
                    y = i
                    break

        self.visited_nodes.append((x, y, 'S'))

        x, y, current_direction = self.get_possible_directions(x, y)
        current_tile = self.grid[y][x]

        self.visited_nodes.append((x, y, current_tile))

        while current_tile != 'S':
            x, y, current_direction = self.get_possible_directions(x, y)
            if not x and not y:
                break
            current_tile = self.grid[y][x]

            self.visited_nodes.append((x, y, current_tile))

        return str(len(self.visited_nodes) // 2)

    def part_two(self, raw_data: str) -> str:
        if len(self.visited_nodes) == 0:
            self.part_one(raw_data)

        empty_grid = [list(' ' * len(row) * 3) for row in self.grid * 3]

        for x, y, tile in self.visited_nodes:
            x = (x * 3) + 1
            y = (y * 3) + 1
            empty_grid[y][x] = 'X'

            if tile == '|':
                empty_grid[y - 1][x] = '|'
                empty_grid[y][x] = '|'
                empty_grid[y + 1][x] = '|'
            elif tile == '-':
                empty_grid[y][x - 1] = '-'
                empty_grid[y][x] = '-'
                empty_grid[y][x + 1] = '-'
            elif tile == 'L':
                empty_grid[y - 1][x] = '|'
                empty_grid[y][x] = 'L'
                empty_grid[y][x + 1] = '-'
            elif tile == 'J':
                empty_grid[y - 1][x] = '|'
                empty_grid[y][x] = 'J'
                empty_grid[y][x - 1] = '-'
            elif tile == 'F':
                empty_grid[y][x + 1] = '-'
                empty_grid[y][x] = 'F'
                empty_grid[y + 1][x] = '|'
            elif tile == '7':
                empty_grid[y][x - 1] = '-'
                empty_grid[y][x] = '7'
                empty_grid[y + 1][x] = '|'
            else:
                empty_grid[y][x - 1] = 'S'
                empty_grid[y][x + 1] = 'S'
                empty_grid[y - 1][x] = 'S'
                empty_grid[y][x] = 'S'
                empty_grid[y + 1][x] = 'S'

        nodes = [(0, 0)]

        while len(nodes) > 0:
            x, y = nodes.pop()

            if x + 1 < len(empty_grid[0]) and empty_grid[y][x + 1] == ' ':
                empty_grid[y][x + 1] = 'O'
                nodes.append((x + 1, y))
            if x - 1 >= 0 and empty_grid[y][x - 1] == ' ':
                empty_grid[y][x - 1] = 'O'
                nodes.append((x - 1, y))
            if y + 1 < len(empty_grid) and empty_grid[y + 1][x] == ' ':
                empty_grid[y + 1][x] = 'O'
                nodes.append((x, y + 1))
            if y - 1 >= 0 and empty_grid[y - 1][x] == ' ':
                empty_grid[y - 1][x] = 'O'
                nodes.append((x, y - 1))

        # [print("".join(row)) for row in empty_grid]

        count_outer = 0

        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                _x = (x * 3) + 1
                _y = (y * 3) + 1

                if empty_grid[_y][_x] == 'O':
                    count_outer += 1

        grid_elements = len(self.grid) * len(self.grid[0])

        return str(grid_elements - len(self.visited_nodes) - count_outer)
        pass    

if __name__ == '__main__':
    Day10().run(False, True, True)