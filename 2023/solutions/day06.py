from aoc.Math import mul
import math
from aoc import Day

class Day06(Day):

    def __init__(self):
        super().__init__(6)

    def parse_row(self, line: str) -> list[int]:
        _, content = line.split(":")
        content = content.strip()

        return_list = []

        for element in content.split(" "):
            if len(element) == 0:
                continue
            return_list.append(int(element))
        return return_list

    def parse_row_special(self, line: str) -> list[int]:
        _, content = line.split(":")
        content = content.replace(" ", "")

        return_list = []

        for element in content.split(" "):
            if len(element) == 0:
                continue
            return_list.append(int(element))
        return return_list

    def get_xs(self, time, distance) -> tuple:
        """
        x_1/x_2 = (-b +- sqrt(-b^2 - 4 * a * c)) / 2 * a
        a = 1
        b = time * -1
        c = distance
        """
        time *= -1
        dis = math.sqrt((time ** 2) - 4 * distance)
        x_1 = ((-1 * time) - dis) / 2
        x_2 = ((-1 * time) + dis) / 2
        return x_1, x_2

    def part_one(self, raw_data: str):
        times, distances = [self.parse_row(line) for line in raw_data.splitlines()]
        values = []

        for time, distance in zip(times, distances):
            x_1, x_2 = self.get_xs(time, distance)

            lower_bound = int(x_1) + 1
            upper_bound = int(x_2) - (1 if int(x_2) == x_2 else 0)

            possibilities = upper_bound - lower_bound + 1
            values.append(possibilities)
            # print(f"[{lower_bound};{upper_bound}]{possibilities=}")

        return str(mul(values))

    def part_two(self, raw_data: str):
        times, distances = [self.parse_row_special(line) for line in raw_data.splitlines()]
        values = []

        for time, distance in zip(times, distances):
            x_1, x_2 = self.get_xs(time, distance)

            lower_bound = int(x_1) + 1
            upper_bound = int(x_2) - (1 if int(x_2) == x_2 else 0)

            possibilities = upper_bound - lower_bound + 1
            values.append(possibilities)
            # print(f"[{lower_bound};{upper_bound}] {possibilities=}")

        return str(mul(values))


if __name__ == '__main__':
    Day06().run()