from colorsys import TWO_THIRD
from ctypes import c_int

from aoc import Day
import re

class Day03(Day):

    def __init__(self):
        super().__init__(year=2024, day=3)

    def part_one(self, data: str):
        resp =re.findall(r'mul\(\d{1,3},\d{1,3}\)', data)

        result = 0

        for element in resp:
            result += self._multiply(element)

        return f"{result}"

    def _multiply(self, input_str: str) -> int:

        elements = input_str.replace("mul(", "").replace(")", "").split(",")

        numbers = list(map(int, elements))

        return numbers[0] * numbers[1]

    def part_two(self, data: str):
        mul_elements = re.findall(r'mul\(\d{1,3},\d{1,3}\)', data)
        do_elements = re.findall(r'don\'t\(\)|do\(\)', data)

        elem_list = []

        for element in mul_elements:
            elem_list.append((data.index(element), True, element))

        last_do_dont_idx = 0
        do_dont_list = []

        for element in do_elements:
            idx = data.index(element, last_do_dont_idx)
            last_do_dont_idx = idx + len(element)
            do_dont_list.append((idx, False, element))

        active = True

        elem_list += do_dont_list

        elem_list.sort(key=lambda x: x[0])

        result = 0

        for idx, is_multi, element in elem_list:
            if is_multi and active:
                result += self._multiply(element)
                continue

            if not is_multi:
                active = element.__contains__('do()')

        return f"{result}"

if __name__ == '__main__':
    Day03().run(demo=False, part_one=True, part_two=True)
