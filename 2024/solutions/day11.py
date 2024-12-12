from anyio import value

from aoc import Day


class Day11(Day):

    def __init__(self):
        super().__init__(year=2024, day=11)

    def _process_number(self, num: int) -> list[int]:
        if num == 0:
            return [1]
        if len(str(num)) % 2 == 0:
            len_num = len(str(num))
            return [int(str(num)[:len_num // 2]), int(str(num)[len_num // 2:])]
        return [num * 2024]


    def part_one(self, data: str):
        numbers = [int(x) for x in data.split(' ')]

        for i in range(25):
            print(f"\r{i}", end="")
            new_numbers = []
            for number in numbers:
                new_numbers.extend(self._process_number(number))
            # print(new_numbers)
            numbers = new_numbers

        return f"{len(numbers)}"

    def add_stones(self, stones: dict, stone_number: int, stone_count: int):
        if stone_number in stones:
            stones[stone_number] += stone_count
        else:
            stones[stone_number] = stone_count

    def part_two(self, data: str):
        stones = {}

        for elem in data.split(' '):
            self.add_stones(stones, int(elem), 1)

        for run in range(75):
            run_stones = {}
            for stone in stones:
                p_stones = self._process_number(stone)
                for p_stone in p_stones:
                    self.add_stones(run_stones, p_stone, stones[stone])

            stones = run_stones
        return f"{sum(stones.values())}"



if __name__ == '__main__':
    Day11().run(demo=False, part_one=False, part_two=True)
