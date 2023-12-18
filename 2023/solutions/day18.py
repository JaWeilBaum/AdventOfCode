from aoc import Day


class Day18(Day):

    def __init__(self):
        super().__init__(18)

    def part_one(self, raw_data: str) -> str:
        rows = [(row.split()[0], int(row.split()[1]))for row in raw_data.splitlines()]

        points = [(0, 0)]
        x, y = 0, 0
        for direction, distance in rows:

            if direction == 'D':
                _x, _y = 0, 1
            elif direction == 'R':
                _x, _y = 1, 0
            elif direction == 'L':
                _x, _y = -1, 0
            else:
                _x, _y = 0, -1

            for _ in range(distance):
                x += _x
                y += _y
                if (x, y) not in points:
                    points.append((x, y))

        min_x = min(map(lambda x: x[0], points))
        max_x = max(map(lambda x: x[0], points))
        min_y = min(map(lambda x: x[1], points))
        max_y = max(map(lambda x: x[1], points))

        print(min_x, max_x)
        print(min_y, max_y)

        off_set_x = abs(min_x)
        off_set_y = abs(min_y)

        x_len = max_x + off_set_x + 1
        y_len = max_y + off_set_y + 1
        print(x_len, y_len)

        grid = [['.'] * (x_len) for _ in range(y_len)]

        for row_idx in range(min_y, max_y + 1):
            for col_idx in range(min_x, max_x + 1):
                if (col_idx, row_idx) in points:
                    if row_idx == 0 and col_idx == 0:
                        grid[row_idx + off_set_y][col_idx + off_set_x] = 'X'
                    else:
                        grid[row_idx + off_set_y][col_idx + off_set_x] = '#'

        # [print(''.join(row)) for row in grid]

        flood_list = [(2 + off_set_x, 1 + off_set_y)]

        while len(flood_list) > 0:
            x, y = flood_list.pop()
            for _x, _y in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                tmp_x = x + _x
                tmp_y = y + _y
                if 0 <= tmp_x <= x_len and 0 <= tmp_y <= y_len and grid[tmp_y][tmp_x] == '.':
                    grid[tmp_y][tmp_x] = 'O'
                    flood_list.append((tmp_x, tmp_y))


        # [print(''.join(row)) for row in grid]

        values = [len(list(filter(lambda x: x != '.', row))) for row in grid]
        return str(sum(values))
        pass

    def part_two(self, raw_data: str) -> str:
        pass



if __name__ == '__main__':
    Day18().run(False, True, False)