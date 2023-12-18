from aoc import Day
import heapq

class Day17(Day):

    def __init__(self):
        super().__init__(17)

    def part_one(self, raw_data: str) -> str:
        grid = [[int(x) for x in row] for row in raw_data.splitlines()]

        queue = [(0, 0, 0, '', -1)]
        storage = {}

        while len(queue) > 0:
            distance, x, y, direction, in_direction = heapq.heappop(queue)

            if (x, y, direction, in_direction) in storage:
                continue
            storage[(x, y, direction, in_direction)] = distance

            for _direction, _x, _y in [('R', 1, 0), ('D', 0, 1), ('L', -1, 0), ('U', 0, -1)]:
                new_x = x + _x
                new_y = y + _y
                new_direction = _direction

                is_backward = ((new_direction == 'R' and direction == 'L') or
                               (new_direction == 'L' and direction == 'R') or
                               (new_direction == 'U' and direction == 'D') or
                               (new_direction == 'D' and direction == 'U'))

                new_in_direction = 1 if new_direction != direction else in_direction + 1
                if 0 <= new_x < len(grid[0]) and 0 <= new_y < len(grid) and new_in_direction <= 3 and not is_backward:
                    cost = grid[new_y][new_x]
                    if new_x == len(grid[0]) - 1 and new_y == len(grid) - 1:
                        return str(distance + cost)
                    heapq.heappush(queue, (distance + cost, new_x, new_y, new_direction, new_in_direction))
        return 'No answer found!'

    def part_two(self, raw_data: str) -> str:
        grid = [[int(x) for x in row] for row in raw_data.splitlines()]

        # (Distance, x, y, direction, steps in direction)
        queue = [(0, 0, 0, '', -1)]
        # Stores values for visited nodes
        storage = {}

        while len(queue) > 0:
            distance, x, y, direction, in_direction = heapq.heappop(queue)

            if (x, y, direction, in_direction) in storage:
                continue
            storage[(x, y, direction, in_direction)] = distance

            for _direction, _x, _y in [('R', 1, 0), ('D', 0, 1), ('L', -1, 0), ('U', 0, -1)]:
                new_x = x + _x
                new_y = y + _y
                new_direction = _direction

                is_backward = ((new_direction == 'R' and direction == 'L') or
                               (new_direction == 'L' and direction == 'R') or
                               (new_direction == 'U' and direction == 'D') or
                               (new_direction == 'D' and direction == 'U'))

                new_in_direction = 1 if new_direction != direction else in_direction + 1

                valid_move = new_in_direction <= 10 and (new_direction == direction or in_direction >= 4 or in_direction == -1)

                if 0 <= new_x < len(grid[0]) and 0 <= new_y < len(grid) and valid_move and not is_backward:
                    cost = grid[new_y][new_x]
                    if new_x == len(grid[0]) - 1 and new_y == len(grid) - 1:
                        return str(distance + cost)
                    heapq.heappush(queue, (distance + cost, new_x, new_y, new_direction, new_in_direction))

        return 'No answer found!'


if __name__ == '__main__':
    Day17().run(False, True, True)