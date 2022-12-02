import pprint
import hashlib

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

class Board:

    def __init__(self, input_data: str):
        self._board = text_to_board(input_data)
        self.width = len(self._board[0])
        self.height = len(self._board)

    def value_at(self, x, y) -> str:
        return self._board[y % self.height][x % self.width]

    def is_free(self, x, y) -> bool:
        return self.value_at(x, y) == '.'

    def move_east(self) -> int:
        skip_idx = []
        # print("--- Possible move east ---")
        for y in range(self.height):
            for x in reversed(range(self.width)):
                if self.value_at(x, y) == '>' and self.is_free(x + 1, y) and Point(x, y) not in skip_idx:
                    self.move(x, y, x + 1, y)
                    # skip_idx.append(Point((x + 1) % self.width, y))
                    # print(f'Move to right {x=} {y=}')
        return len(skip_idx)

    def move_south(self) -> int:
        skip_idx = []
        # print("--- Possible move south ---")
        for y in reversed(range(self.height)):
            for x in range(self.width):
                if self.value_at(x, y) == 'v' and self.is_free(x, y + 1) and Point(x, y) not in skip_idx:
                    self.move(x, y, x, y + 1)
                    skip_idx.append(Point(x, (y + 1) % self.height))
                    # print(f'Move to down {x=} {y=}')
        return len(skip_idx)

    def move(self, x_from, y_from, x_to, y_to):
        key = self.value_at(x_from, y_from)
        self.set_value_at(x_from, y_from, '.')
        self.set_value_at(x_to, y_to, key)

    def set_value_at(self, x, y, key: str):
        self._board[y % self.height][x % self.width] = key

    def step(self) -> bool:
        num_moves_east = self.move_east()
        print(self)
        num_moves_south = self.move_south()
        return num_moves_south + num_moves_east > 0

    def can_move(self, x, y) -> bool:
        key = self.value_at(x, y)
        if key == '>' and self.is_free(x + 1, y):
            # print(f'Move to right {x=} {y=}')
            return True
        elif key == 'v' and self.is_free(x, y + 1):
            # print(f'Move to down {x=} {y=}')
            return True
        return False

    def __str__(self):
        return "\n".join(["".join(x) for x in self._board])

def hash_loc(x, y) -> str:
    return hashlib.sha512(f"{x=}-{y=}".encode("utf-8")).hexdigest()

def demo_input() -> str:
    return """v...>>.vv>
.vv>>.vv..
>>.>v>...v
>>v>>.>.v.
v>v.vv.v..
>.>>..v...
.vv..>.>v.
v.v..>>v.v
....v..v.>"""

def get_input() -> str:
    with open("files/day_25.txt") as f:
        return f.read()

def text_to_board(text: str) -> list[list[str]]:

    lines = text.split("\n")
    return [list(x) for x in lines]

def step():
    b = Board(demo_input())
    print(f"{b.width=} {b.height=}")
    moves = 0
    print(b)
    while b.step():
        moves += 1
    print()
    print(b)
    print(moves)

def main():
    step()


if __name__ == '__main__':
    main()